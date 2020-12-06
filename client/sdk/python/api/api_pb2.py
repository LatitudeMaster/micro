# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/api.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='api/api.proto',
  package='api',
  syntax='proto3',
  serialized_options=b'Z\'github.com/micro-community/micro/v3/proto/api;api',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rapi/api.proto\x12\x03\x61pi\"T\n\x08\x45ndpoint\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04host\x18\x02 \x03(\t\x12\x0c\n\x04path\x18\x03 \x03(\t\x12\x0e\n\x06method\x18\x04 \x03(\t\x12\x0e\n\x06stream\x18\x05 \x01(\x08\"\x0f\n\rEmptyResponse\"#\n\x04Pair\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0e\n\x06values\x18\x02 \x03(\t\"\xdf\x02\n\x07Request\x12\x0e\n\x06method\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t\x12(\n\x06header\x18\x03 \x03(\x0b\x32\x18.api.Request.HeaderEntry\x12\"\n\x03get\x18\x04 \x03(\x0b\x32\x15.api.Request.GetEntry\x12$\n\x04post\x18\x05 \x03(\x0b\x32\x16.api.Request.PostEntry\x12\x0c\n\x04\x62ody\x18\x06 \x01(\t\x12\x0b\n\x03url\x18\x07 \x01(\t\x1a\x38\n\x0bHeaderEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x18\n\x05value\x18\x02 \x01(\x0b\x32\t.api.Pair:\x02\x38\x01\x1a\x35\n\x08GetEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x18\n\x05value\x18\x02 \x01(\x0b\x32\t.api.Pair:\x02\x38\x01\x1a\x36\n\tPostEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x18\n\x05value\x18\x02 \x01(\x0b\x32\t.api.Pair:\x02\x38\x01\"\x91\x01\n\x08Response\x12\x12\n\nstatusCode\x18\x01 \x01(\x05\x12)\n\x06header\x18\x02 \x03(\x0b\x32\x19.api.Response.HeaderEntry\x12\x0c\n\x04\x62ody\x18\x03 \x01(\t\x1a\x38\n\x0bHeaderEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x18\n\x05value\x18\x02 \x01(\x0b\x32\t.api.Pair:\x02\x38\x01\"\xa4\x01\n\x05\x45vent\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\x03\x12&\n\x06header\x18\x04 \x03(\x0b\x32\x16.api.Event.HeaderEntry\x12\x0c\n\x04\x64\x61ta\x18\x05 \x01(\t\x1a\x38\n\x0bHeaderEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x18\n\x05value\x18\x02 \x01(\x0b\x32\t.api.Pair:\x02\x38\x01\x32i\n\x03\x41pi\x12/\n\x08Register\x12\r.api.Endpoint\x1a\x12.api.EmptyResponse\"\x00\x12\x31\n\nDeregister\x12\r.api.Endpoint\x1a\x12.api.EmptyResponse\"\x00\x42)Z\'github.com/micro-community/micro/v3/proto/api;apib\x06proto3'
)




_ENDPOINT = _descriptor.Descriptor(
  name='Endpoint',
  full_name='api.Endpoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='api.Endpoint.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='host', full_name='api.Endpoint.host', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='path', full_name='api.Endpoint.path', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='method', full_name='api.Endpoint.method', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='stream', full_name='api.Endpoint.stream', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=106,
)


_EMPTYRESPONSE = _descriptor.Descriptor(
  name='EmptyResponse',
  full_name='api.EmptyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=108,
  serialized_end=123,
)


_PAIR = _descriptor.Descriptor(
  name='Pair',
  full_name='api.Pair',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='api.Pair.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='values', full_name='api.Pair.values', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=125,
  serialized_end=160,
)


_REQUEST_HEADERENTRY = _descriptor.Descriptor(
  name='HeaderEntry',
  full_name='api.Request.HeaderEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='api.Request.HeaderEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='api.Request.HeaderEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=347,
  serialized_end=403,
)

_REQUEST_GETENTRY = _descriptor.Descriptor(
  name='GetEntry',
  full_name='api.Request.GetEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='api.Request.GetEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='api.Request.GetEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=405,
  serialized_end=458,
)

_REQUEST_POSTENTRY = _descriptor.Descriptor(
  name='PostEntry',
  full_name='api.Request.PostEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='api.Request.PostEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='api.Request.PostEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=460,
  serialized_end=514,
)

_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='api.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='method', full_name='api.Request.method', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='path', full_name='api.Request.path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='header', full_name='api.Request.header', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='get', full_name='api.Request.get', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='post', full_name='api.Request.post', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='body', full_name='api.Request.body', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='url', full_name='api.Request.url', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_REQUEST_HEADERENTRY, _REQUEST_GETENTRY, _REQUEST_POSTENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=163,
  serialized_end=514,
)


_RESPONSE_HEADERENTRY = _descriptor.Descriptor(
  name='HeaderEntry',
  full_name='api.Response.HeaderEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='api.Response.HeaderEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='api.Response.HeaderEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=347,
  serialized_end=403,
)

_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='api.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='statusCode', full_name='api.Response.statusCode', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='header', full_name='api.Response.header', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='body', full_name='api.Response.body', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_RESPONSE_HEADERENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=517,
  serialized_end=662,
)


_EVENT_HEADERENTRY = _descriptor.Descriptor(
  name='HeaderEntry',
  full_name='api.Event.HeaderEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='api.Event.HeaderEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='api.Event.HeaderEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=347,
  serialized_end=403,
)

_EVENT = _descriptor.Descriptor(
  name='Event',
  full_name='api.Event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='api.Event.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='api.Event.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='api.Event.timestamp', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='header', full_name='api.Event.header', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='api.Event.data', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_EVENT_HEADERENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=665,
  serialized_end=829,
)

_REQUEST_HEADERENTRY.fields_by_name['value'].message_type = _PAIR
_REQUEST_HEADERENTRY.containing_type = _REQUEST
_REQUEST_GETENTRY.fields_by_name['value'].message_type = _PAIR
_REQUEST_GETENTRY.containing_type = _REQUEST
_REQUEST_POSTENTRY.fields_by_name['value'].message_type = _PAIR
_REQUEST_POSTENTRY.containing_type = _REQUEST
_REQUEST.fields_by_name['header'].message_type = _REQUEST_HEADERENTRY
_REQUEST.fields_by_name['get'].message_type = _REQUEST_GETENTRY
_REQUEST.fields_by_name['post'].message_type = _REQUEST_POSTENTRY
_RESPONSE_HEADERENTRY.fields_by_name['value'].message_type = _PAIR
_RESPONSE_HEADERENTRY.containing_type = _RESPONSE
_RESPONSE.fields_by_name['header'].message_type = _RESPONSE_HEADERENTRY
_EVENT_HEADERENTRY.fields_by_name['value'].message_type = _PAIR
_EVENT_HEADERENTRY.containing_type = _EVENT
_EVENT.fields_by_name['header'].message_type = _EVENT_HEADERENTRY
DESCRIPTOR.message_types_by_name['Endpoint'] = _ENDPOINT
DESCRIPTOR.message_types_by_name['EmptyResponse'] = _EMPTYRESPONSE
DESCRIPTOR.message_types_by_name['Pair'] = _PAIR
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.message_types_by_name['Event'] = _EVENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Endpoint = _reflection.GeneratedProtocolMessageType('Endpoint', (_message.Message,), {
  'DESCRIPTOR' : _ENDPOINT,
  '__module__' : 'api.api_pb2'
  # @@protoc_insertion_point(class_scope:api.Endpoint)
  })
_sym_db.RegisterMessage(Endpoint)

EmptyResponse = _reflection.GeneratedProtocolMessageType('EmptyResponse', (_message.Message,), {
  'DESCRIPTOR' : _EMPTYRESPONSE,
  '__module__' : 'api.api_pb2'
  # @@protoc_insertion_point(class_scope:api.EmptyResponse)
  })
_sym_db.RegisterMessage(EmptyResponse)

Pair = _reflection.GeneratedProtocolMessageType('Pair', (_message.Message,), {
  'DESCRIPTOR' : _PAIR,
  '__module__' : 'api.api_pb2'
  # @@protoc_insertion_point(class_scope:api.Pair)
  })
_sym_db.RegisterMessage(Pair)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {

  'HeaderEntry' : _reflection.GeneratedProtocolMessageType('HeaderEntry', (_message.Message,), {
    'DESCRIPTOR' : _REQUEST_HEADERENTRY,
    '__module__' : 'api.api_pb2'
    # @@protoc_insertion_point(class_scope:api.Request.HeaderEntry)
    })
  ,

  'GetEntry' : _reflection.GeneratedProtocolMessageType('GetEntry', (_message.Message,), {
    'DESCRIPTOR' : _REQUEST_GETENTRY,
    '__module__' : 'api.api_pb2'
    # @@protoc_insertion_point(class_scope:api.Request.GetEntry)
    })
  ,

  'PostEntry' : _reflection.GeneratedProtocolMessageType('PostEntry', (_message.Message,), {
    'DESCRIPTOR' : _REQUEST_POSTENTRY,
    '__module__' : 'api.api_pb2'
    # @@protoc_insertion_point(class_scope:api.Request.PostEntry)
    })
  ,
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'api.api_pb2'
  # @@protoc_insertion_point(class_scope:api.Request)
  })
_sym_db.RegisterMessage(Request)
_sym_db.RegisterMessage(Request.HeaderEntry)
_sym_db.RegisterMessage(Request.GetEntry)
_sym_db.RegisterMessage(Request.PostEntry)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {

  'HeaderEntry' : _reflection.GeneratedProtocolMessageType('HeaderEntry', (_message.Message,), {
    'DESCRIPTOR' : _RESPONSE_HEADERENTRY,
    '__module__' : 'api.api_pb2'
    # @@protoc_insertion_point(class_scope:api.Response.HeaderEntry)
    })
  ,
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'api.api_pb2'
  # @@protoc_insertion_point(class_scope:api.Response)
  })
_sym_db.RegisterMessage(Response)
_sym_db.RegisterMessage(Response.HeaderEntry)

Event = _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), {

  'HeaderEntry' : _reflection.GeneratedProtocolMessageType('HeaderEntry', (_message.Message,), {
    'DESCRIPTOR' : _EVENT_HEADERENTRY,
    '__module__' : 'api.api_pb2'
    # @@protoc_insertion_point(class_scope:api.Event.HeaderEntry)
    })
  ,
  'DESCRIPTOR' : _EVENT,
  '__module__' : 'api.api_pb2'
  # @@protoc_insertion_point(class_scope:api.Event)
  })
_sym_db.RegisterMessage(Event)
_sym_db.RegisterMessage(Event.HeaderEntry)


DESCRIPTOR._options = None
_REQUEST_HEADERENTRY._options = None
_REQUEST_GETENTRY._options = None
_REQUEST_POSTENTRY._options = None
_RESPONSE_HEADERENTRY._options = None
_EVENT_HEADERENTRY._options = None

_API = _descriptor.ServiceDescriptor(
  name='Api',
  full_name='api.Api',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=831,
  serialized_end=936,
  methods=[
  _descriptor.MethodDescriptor(
    name='Register',
    full_name='api.Api.Register',
    index=0,
    containing_service=None,
    input_type=_ENDPOINT,
    output_type=_EMPTYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Deregister',
    full_name='api.Api.Deregister',
    index=1,
    containing_service=None,
    input_type=_ENDPOINT,
    output_type=_EMPTYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_API)

DESCRIPTOR.services_by_name['Api'] = _API

# @@protoc_insertion_point(module_scope)
