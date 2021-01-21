package model

import (
	"context"
	"encoding/base32"
	"encoding/json"
	"errors"
	"fmt"
	"math"
	"reflect"
	"strings"
	"unicode/utf8"

	"github.com/micro-community/micro/v3/service/store"
	"github.com/stoewer/go-strcase"
)

type model struct {
	// the primary index using id
	idIndex Index
	// helps logically separate keys in a model where
	// multiple `Model`s share the same underlying
	// physical database.
	namespace string
	// the user defined.options.Indexes maintained for queries
	indexes []Index
	// options accepted for the model
	options *Options
	// the instance of the model
	instance interface{}
}

// NewModel returns a new model with options or uses internal defaults
func NewModel(opts ...Option) Model {
	var options Options

	for _, o := range opts {
		o(&options)
	}

	if options.Store == nil {
		options.Store = store.DefaultStore
	}

	if len(options.Indexes) == 0 {
		options.Indexes = append(options.Indexes, DefaultIndex)
	}

	return New(nil, &options)
}

// New returns a new model with the given values
func New(instance interface{}, options *Options) Model {
	if options == nil {
		options = new(Options)
	}

	var namespace string

	// define namespace based on the value passed in
	if instance != nil {
		namespace = reflect.TypeOf(instance).String()
	}

	if len(options.Namespace) > 0 {
		namespace = options.Namespace
	}

	if options.Store == nil {
		options.Store = store.DefaultStore
	}

	if options.Context == nil {
		options.Context = context.TODO()
	}

	// the default index
	idx := DefaultIndex

	if len(options.Key) > 0 {
		idx = newIndex(options.Key)
	}

	return &model{
		idIndex:   idx,
		instance:  instance,
		namespace: namespace,
		options:   options,
	}
}

// @todo we should correlate the field name with the model
// instead of just blindly converting strings
func getFieldName(field string) string {
	fieldName := ""
	if strings.Contains(field, "_") {
		fieldName = strcase.UpperCamelCase(field)
	} else {
		fieldName = strings.Title(field)
	}
	return strings.Replace(fieldName, "Id", "ID", -1)
}

func getFieldValue(struc interface{}, fieldName string) interface{} {
	fieldName = getFieldName(fieldName)
	r := reflect.ValueOf(struc)
	f := reflect.Indirect(r).FieldByName(fieldName)

	if !f.IsValid() {
		return nil
	}
	return f.Interface()
}

func setFieldValue(struc interface{}, fieldName string, value interface{}) {
	fieldName = getFieldName(fieldName)
	r := reflect.ValueOf(struc)

	f := reflect.Indirect(r).FieldByName(fieldName)
	f.Set(reflect.ValueOf(value))
}

func (d *model) Context(ctx context.Context) Model {
	// dereference the opts
	opts := *d.options
	opts.Context = ctx

	return &model{
		idIndex:   d.idIndex,
		instance:  d.instance,
		namespace: d.namespace,
		options:   &opts,
	}
}

// Register an instance type of a model
func (d *model) Register(v interface{}) error {
	if v == nil {
		return ErrorNilInterface
	}

	// set the namespace
	d.namespace = reflect.TypeOf(v).String()
	// TODO: add.options.Indexes?
	d.instance = v

	return nil
}

func (d *model) Create(instance interface{}) error {
	// @todo replace this hack with reflection
	js, err := json.Marshal(instance)
	if err != nil {
		return err
	}

	// get the old entries so we can compare values
	// @todo consider some kind of locking (even if it's not distributed) by key here
	// to avoid 2 read-writes happening at the same time
	idQuery := d.idIndex.ToQuery(getFieldValue(instance, d.idIndex.FieldName))

	oldEntry := reflect.New(reflect.ValueOf(instance).Type()).Interface()

	err = d.Read(idQuery, &oldEntry)
	if err != nil && err != ErrorNotFound {
		return err
	}

	// Do uniqueness checks before saving any data
	for _, index := range d.options.Indexes {
		if !index.Unique {
			continue
		}
		potentialClash := reflect.New(reflect.ValueOf(instance).Type()).Interface()
		err = d.Read(index.ToQuery(getFieldValue(instance, index.FieldName)), &potentialClash)
		if err != nil && err != ErrorNotFound {
			return err
		}

		if err == nil {
			return errors.New("Unique index violation")
		}
	}

	id := getFieldValue(instance, d.idIndex.FieldName)
	for _, index := range append(d.options.Indexes, d.idIndex) {
		// delete non id index keys to prevent stale index values
		// ie.
		//
		//  # prefix  slug     id
		//  postByTag/hi-there/1
		//  # if slug gets changed to "hello-there" we will have two records
		//  # without removing the old stale index:
		//  postByTag/hi-there/1
		//  postByTag/hello-there/1`
		//
		// @todo this check will only work for POD types, ie no slices or maps
		// but it's not an issue as right now indexes are only supported on POD
		// types anyway
		if !indexesMatch(d.idIndex, index) &&
			oldEntry != nil &&
			!reflect.DeepEqual(getFieldValue(oldEntry, index.FieldName), getFieldValue(instance, index.FieldName)) {
			k := d.indexToKey(index, id, oldEntry, true)
			err = d.options.Store.Delete(k)
			if err != nil {
				return err
			}
		}
		k := d.indexToKey(index, id, instance, true)
		if d.options.Debug {
			fmt.Printf("Saving key '%v', value: '%v'\n", k, string(js))
		}
		err = d.options.Store.Write(&store.Record{
			Key:   k,
			Value: js,
		})
		if err != nil {
			return err
		}
	}
	return nil
}

// TODO: implement the full functionality. Currently offloads to create.
func (d *model) Update(v interface{}) error {
	return d.Create(v)
}

func (d *model) Read(query Query, resultPointer interface{}) error {
	t := reflect.TypeOf(resultPointer)

	// check if it's a pointer
	if v := t.Kind(); v != reflect.Ptr {
		return fmt.Errorf("Require pointer type. Got %v", v)
	}

	// retrieve the non pointer type
	t = t.Elem()

	// if its a slice then use the list query method
	if t.Kind() == reflect.Slice {
		return d.list(query, resultPointer, true)
	}

	read := func(index Index) error {
		k := d.queryToListKey(index, query)
		if d.options.Debug {
			fmt.Printf("Listing key '%v'\n", k)
		}
		recs, err := d.options.Store.Read(k, store.ReadPrefix())
		if err != nil {
			return err
		}
		if len(recs) == 0 {
			return ErrorNotFound
		}
		if len(recs) > 1 {
			return ErrorMultipleRecordsFound
		}
		if d.options.Debug {
			fmt.Printf("Found value '%v'\n", string(recs[0].Value))
		}
		return json.Unmarshal(recs[0].Value, resultPointer)
	}
	// otherwise continue on as normal
	for _, index := range append(d.options.Indexes, d.idIndex) {
		if indexMatchesQuery(index, query) {
			return read(index)
		}
	}

	// find a maching query if non exists, take the first one
	// which applies to the same field regardless of ordering
	// or padding etc.
	for _, index := range append(d.options.Indexes, d.idIndex) {
		fmt.Println(index.FieldName, query.FieldName)
		if index.FieldName == query.FieldName {
			return read(index)
		}
	}
	return fmt.Errorf("Read: for query type '%v', field '%v' does not match any indexes", query.Type, query.FieldName)
}

func (d *model) List(query Query, resultSlicePointer interface{}) error {
	return d.list(query, resultSlicePointer, false)
}

func (d *model) list(query Query, resultSlicePointer interface{}, isRead bool) error {
	list := func(index Index) error {
		k := d.queryToListKey(index, query)
		if d.options.Debug {
			fmt.Printf("Listing key '%v'\n", k)
		}
		recs, err := d.options.Store.Read(k, store.ReadPrefix())
		if err != nil {
			return err
		}
		// @todo speed this up with an actual buffer
		jsBuffer := []byte("[")
		for i, rec := range recs {
			jsBuffer = append(jsBuffer, rec.Value...)
			if i < len(recs)-1 {
				jsBuffer = append(jsBuffer, []byte(",")...)
			}
		}
		jsBuffer = append(jsBuffer, []byte("]")...)
		if d.options.Debug {
			fmt.Printf("Found values '%v'\n", string(jsBuffer))
		}
		return json.Unmarshal(jsBuffer, resultSlicePointer)
	}
	for _, index := range append(d.options.Indexes, d.idIndex) {
		if indexMatchesQuery(index, query) {
			return list(index)
		}
	}

	if isRead {
		// find a maching query if non exists, take the first one
		// which applies to the same field regardless of ordering
		// or padding etc.
		//
		// only do this for reads because ordering doesnt matter with single reads
		for _, index := range append(d.options.Indexes, d.idIndex) {
			if index.FieldName == query.FieldName {
				return list(index)
			}
		}
	}
	return fmt.Errorf("List: for query type '%v', field '%v' does not match any indexes", query.Type, query.FieldName)
}

func (d *model) queryToListKey(i Index, q Query) string {
	if q.Value == nil {
		return fmt.Sprintf("%v:%v", d.namespace, indexPrefix(i))
	}
	if i.FieldName != i.Order.FieldName && i.Order.FieldName != "" {
		return fmt.Sprintf("%v:%v:%v", d.namespace, indexPrefix(i), q.Value)
	}

	val := reflect.New(reflect.ValueOf(d.instance).Type()).Interface()
	if q.Value != nil {
		setFieldValue(val, i.FieldName, q.Value)
	}
	return d.indexToKey(i, "", val, false)
}

// appendID true should be used when saving, false when querying
// appendID false should also be used for 'id' indexes since they already have the unique
// id. The reason id gets appended is make duplicated index keys unique.
// ie.
// # index # age # id
// users/30/1
// users/30/2
// without ids we could only have one 30 year old user in the index
func (d *model) indexToKey(i Index, id interface{}, entry interface{}, appendID bool) string {
	format := "%v:%v"
	values := []interface{}{d.namespace, indexPrefix(i)}
	filterFieldValue := getFieldValue(entry, i.FieldName)
	orderFieldValue := getFieldValue(entry, i.FieldName)
	orderFieldKey := i.FieldName

	if i.FieldName != i.Order.FieldName && i.Order.FieldName != "" {
		orderFieldValue = getFieldValue(entry, i.Order.FieldName)
		orderFieldKey = i.Order.FieldName
	}

	switch i.Type {
	case indexTypeEq:
		// If the filtering field is different than the ordering field,
		// append the filter key to the key.
		if i.FieldName != i.Order.FieldName && i.Order.FieldName != "" {
			format += ":%v"
			values = append(values, filterFieldValue)
		}
	}

	// Handle the ordering part of the key.
	// The filter and the ordering field might be the same
	typ := reflect.TypeOf(orderFieldValue)
	typName := "nil"
	if typ != nil {
		typName = typ.String()
	}
	format += ":%v"

	switch v := orderFieldValue.(type) {
	case string:
		if i.Order.Type != OrderTypeUnordered {
			values = append(values, d.getOrderedStringFieldKey(i, v))
			break
		}
		values = append(values, v)
	case int64:
		// int64 gets padded to 19 characters as the maximum value of an int64
		// is 9223372036854775807
		// @todo handle negative numbers
		if i.Order.Type == OrderTypeDesc {
			values = append(values, fmt.Sprintf("%019d", math.MaxInt64-v))
			break
		}
		values = append(values, fmt.Sprintf("%019d", v))
	case float32:
		// @todo fix display and padding of floats
		if i.Order.Type == OrderTypeDesc {
			values = append(values, fmt.Sprintf(i.FloatFormat, i.Float32Max-v))
			break
		}
		values = append(values, fmt.Sprintf(i.FloatFormat, v))
	case float64:
		// @todo fix display and padding of floats
		if i.Order.Type == OrderTypeDesc {
			values = append(values, fmt.Sprintf(i.FloatFormat, i.Float64Max-v))
			break
		}
		values = append(values, fmt.Sprintf(i.FloatFormat, v))
	case int:
		// int gets padded to the same length as int64 to gain
		// resiliency in case of model type changes.
		// This could be removed once migrations are implemented
		// so savings in space for a type reflect in savings in space in the index too.
		if i.Order.Type == OrderTypeDesc {
			values = append(values, fmt.Sprintf("%019d", math.MaxInt32-v))
			break
		}
		values = append(values, fmt.Sprintf("%019d", v))
	case int32:
		// int gets padded to the same length as int64 to gain
		// resiliency in case of model type changes.
		// This could be removed once migrations are implemented
		// so savings in space for a type reflect in savings in space in the index too.
		if i.Order.Type == OrderTypeDesc {
			values = append(values, fmt.Sprintf("%019d", math.MaxInt32-v))
			break
		}
		values = append(values, fmt.Sprintf("%019d", v))
	case bool:
		if i.Order.Type == OrderTypeDesc {
			v = !v
		}
		values = append(values, v)
	default:
		panic("bug in code, unhandled type: " + typName + " for field '" + orderFieldKey + "' on type '" + reflect.TypeOf(d.instance).String() + "'")
	}

	if appendID {
		format += ":%v"
		values = append(values, id)
	}
	return fmt.Sprintf(format, values...)
}

// pad, reverse and optionally base32 encode string keys
func (d *model) getOrderedStringFieldKey(i Index, fieldValue string) string {
	runes := []rune{}
	if i.Order.Type == OrderTypeDesc {
		for _, char := range fieldValue {
			runes = append(runes, utf8.MaxRune-char)
		}
	} else {
		for _, char := range fieldValue {
			runes = append(runes, char)
		}
	}

	// padding the string to a fixed length
	if len(runes) < i.StringOrderPadLength {
		pad := []rune{}
		for j := 0; j < i.StringOrderPadLength-len(runes); j++ {
			if i.Order.Type == OrderTypeDesc {
				pad = append(pad, utf8.MaxRune)
			} else {
				// space is the first non control operator char in ASCII
				// consequently in Utf8 too so we use it as the minimal character here
				// https://en.wikipedia.org/wiki/ASCII
				//
				// Displays somewhat unfortunately
				// @todo think about a better min rune value to use here.
				pad = append(pad, rune(32))
			}
		}
		runes = append(runes, pad...)
	}

	var keyPart string
	bs := []byte(string(runes))
	if i.Order.Type == OrderTypeDesc {
		if i.Base32Encode {
			// base32 hex should be order preserving
			// https://stackoverflow.com/questions/53301280/does-base64-encoding-preserve-alphabetical-ordering
			dst := make([]byte, base32.HexEncoding.EncodedLen(len(bs)))
			base32.HexEncoding.Encode(dst, bs)
			// The `=` must be replaced with a lower value than the
			// normal alphabet of the encoding since we want reverse order.
			keyPart = strings.ReplaceAll(string(dst), "=", "0")
		} else {
			keyPart = string(bs)
		}
	} else {
		keyPart = string(bs)

	}
	return keyPart
}

func (d *model) Delete(query Query) error {
	oldEntry := reflect.New(reflect.ValueOf(d.instance).Type()).Interface()
	err := d.Read(d.idIndex.ToQuery(query.Value), &oldEntry)
	if err != nil {
		return err
	}

	// first delete maintained.options.Indexes then id index
	// if we delete id index first then the entry wont
	// be deletable by id again but the maintained.options.Indexes
	// will be stuck in limbo
	for _, index := range append(d.options.Indexes, d.idIndex) {
		key := d.indexToKey(index, getFieldValue(oldEntry, d.idIndex.FieldName), oldEntry, true)
		if d.options.Debug {
			fmt.Printf("Deleting key '%v'\n", key)
		}
		err = d.options.Store.Delete(key)
		if err != nil {
			return err
		}
	}
	return nil
}
