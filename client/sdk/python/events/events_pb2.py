# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: events/events.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='events/events.proto',
  package='events',
  syntax='proto3',
  serialized_options=b'Z,github.com/micro-community/micro/v3/proto/event;events',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13\x65vents/events.proto\x12\x06\x65vents\"\xac\x01\n\x0ePublishRequest\x12\r\n\x05topic\x18\x01 \x01(\t\x12\x36\n\x08metadata\x18\x02 \x03(\x0b\x32$.events.PublishRequest.MetadataEntry\x12\x0f\n\x07payload\x18\x03 \x01(\x0c\x12\x11\n\ttimestamp\x18\x04 \x01(\x03\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x11\n\x0fPublishResponse\"w\n\x0e\x43onsumeRequest\x12\r\n\x05group\x18\x01 \x01(\t\x12\r\n\x05topic\x18\x02 \x01(\t\x12\x0e\n\x06offset\x18\x03 \x01(\x03\x12\x10\n\x08\x61uto_ack\x18\x04 \x01(\x08\x12\x10\n\x08\x61\x63k_wait\x18\x05 \x01(\x03\x12\x13\n\x0bretry_limit\x18\x06 \x01(\x03\"\xa6\x01\n\x05\x45vent\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05topic\x18\x02 \x01(\t\x12-\n\x08metadata\x18\x03 \x03(\x0b\x32\x1b.events.Event.MetadataEntry\x12\x0f\n\x07payload\x18\x04 \x01(\x0c\x12\x11\n\ttimestamp\x18\x05 \x01(\x03\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\";\n\x0bReadRequest\x12\r\n\x05topic\x18\x01 \x01(\t\x12\r\n\x05limit\x18\x02 \x01(\x04\x12\x0e\n\x06offset\x18\x03 \x01(\x04\"-\n\x0cReadResponse\x12\x1d\n\x06\x65vents\x18\x01 \x03(\x0b\x32\r.events.Event\"9\n\x0cWriteRequest\x12\x1c\n\x05\x65vent\x18\x01 \x01(\x0b\x32\r.events.Event\x12\x0b\n\x03ttl\x18\x02 \x01(\x03\"\x0f\n\rWriteResponse\")\n\nAckRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07success\x18\x02 \x01(\x08\x32x\n\x06Stream\x12:\n\x07Publish\x12\x16.events.PublishRequest\x1a\x17.events.PublishResponse\x12\x32\n\x07\x43onsume\x12\x16.events.ConsumeRequest\x1a\r.events.Event0\x01\x32p\n\x05Store\x12\x31\n\x04Read\x12\x13.events.ReadRequest\x1a\x14.events.ReadResponse\x12\x34\n\x05Write\x12\x14.events.WriteRequest\x1a\x15.events.WriteResponseB.Z,github.com/micro-community/micro/v3/proto/event;eventsb\x06proto3'
)




_PUBLISHREQUEST_METADATAENTRY = _descriptor.Descriptor(
  name='MetadataEntry',
  full_name='events.PublishRequest.MetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='events.PublishRequest.MetadataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='events.PublishRequest.MetadataEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=157,
  serialized_end=204,
)

_PUBLISHREQUEST = _descriptor.Descriptor(
  name='PublishRequest',
  full_name='events.PublishRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='topic', full_name='events.PublishRequest.topic', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='events.PublishRequest.metadata', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='payload', full_name='events.PublishRequest.payload', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='events.PublishRequest.timestamp', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_PUBLISHREQUEST_METADATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=32,
  serialized_end=204,
)


_PUBLISHRESPONSE = _descriptor.Descriptor(
  name='PublishResponse',
  full_name='events.PublishResponse',
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
  serialized_start=206,
  serialized_end=223,
)


_CONSUMEREQUEST = _descriptor.Descriptor(
  name='ConsumeRequest',
  full_name='events.ConsumeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='group', full_name='events.ConsumeRequest.group', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='topic', full_name='events.ConsumeRequest.topic', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='offset', full_name='events.ConsumeRequest.offset', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='auto_ack', full_name='events.ConsumeRequest.auto_ack', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ack_wait', full_name='events.ConsumeRequest.ack_wait', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='retry_limit', full_name='events.ConsumeRequest.retry_limit', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=225,
  serialized_end=344,
)


_EVENT_METADATAENTRY = _descriptor.Descriptor(
  name='MetadataEntry',
  full_name='events.Event.MetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='events.Event.MetadataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='events.Event.MetadataEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=157,
  serialized_end=204,
)

_EVENT = _descriptor.Descriptor(
  name='Event',
  full_name='events.Event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='events.Event.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='topic', full_name='events.Event.topic', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='events.Event.metadata', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='payload', full_name='events.Event.payload', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='events.Event.timestamp', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_EVENT_METADATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=347,
  serialized_end=513,
)


_READREQUEST = _descriptor.Descriptor(
  name='ReadRequest',
  full_name='events.ReadRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='topic', full_name='events.ReadRequest.topic', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='limit', full_name='events.ReadRequest.limit', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='offset', full_name='events.ReadRequest.offset', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=515,
  serialized_end=574,
)


_READRESPONSE = _descriptor.Descriptor(
  name='ReadResponse',
  full_name='events.ReadResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='events', full_name='events.ReadResponse.events', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=576,
  serialized_end=621,
)


_WRITEREQUEST = _descriptor.Descriptor(
  name='WriteRequest',
  full_name='events.WriteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='event', full_name='events.WriteRequest.event', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ttl', full_name='events.WriteRequest.ttl', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=623,
  serialized_end=680,
)


_WRITERESPONSE = _descriptor.Descriptor(
  name='WriteResponse',
  full_name='events.WriteResponse',
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
  serialized_start=682,
  serialized_end=697,
)


_ACKREQUEST = _descriptor.Descriptor(
  name='AckRequest',
  full_name='events.AckRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='events.AckRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='success', full_name='events.AckRequest.success', index=1,
      number=2, type=8, cpp_type=7, label=1,
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
  serialized_start=699,
  serialized_end=740,
)

_PUBLISHREQUEST_METADATAENTRY.containing_type = _PUBLISHREQUEST
_PUBLISHREQUEST.fields_by_name['metadata'].message_type = _PUBLISHREQUEST_METADATAENTRY
_EVENT_METADATAENTRY.containing_type = _EVENT
_EVENT.fields_by_name['metadata'].message_type = _EVENT_METADATAENTRY
_READRESPONSE.fields_by_name['events'].message_type = _EVENT
_WRITEREQUEST.fields_by_name['event'].message_type = _EVENT
DESCRIPTOR.message_types_by_name['PublishRequest'] = _PUBLISHREQUEST
DESCRIPTOR.message_types_by_name['PublishResponse'] = _PUBLISHRESPONSE
DESCRIPTOR.message_types_by_name['ConsumeRequest'] = _CONSUMEREQUEST
DESCRIPTOR.message_types_by_name['Event'] = _EVENT
DESCRIPTOR.message_types_by_name['ReadRequest'] = _READREQUEST
DESCRIPTOR.message_types_by_name['ReadResponse'] = _READRESPONSE
DESCRIPTOR.message_types_by_name['WriteRequest'] = _WRITEREQUEST
DESCRIPTOR.message_types_by_name['WriteResponse'] = _WRITERESPONSE
DESCRIPTOR.message_types_by_name['AckRequest'] = _ACKREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PublishRequest = _reflection.GeneratedProtocolMessageType('PublishRequest', (_message.Message,), {

  'MetadataEntry' : _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _PUBLISHREQUEST_METADATAENTRY,
    '__module__' : 'events.events_pb2'
    # @@protoc_insertion_point(class_scope:events.PublishRequest.MetadataEntry)
    })
  ,
  'DESCRIPTOR' : _PUBLISHREQUEST,
  '__module__' : 'events.events_pb2'
  # @@protoc_insertion_point(class_scope:events.PublishRequest)
  })
_sym_db.RegisterMessage(PublishRequest)
_sym_db.RegisterMessage(PublishRequest.MetadataEntry)

PublishResponse = _reflection.GeneratedProtocolMessageType('PublishResponse', (_message.Message,), {
  'DESCRIPTOR' : _PUBLISHRESPONSE,
  '__module__' : 'events.events_pb2'
  # @@protoc_insertion_point(class_scope:events.PublishResponse)
  })
_sym_db.RegisterMessage(PublishResponse)

ConsumeRequest = _reflection.GeneratedProtocolMessageType('ConsumeRequest', (_message.Message,), {
  'DESCRIPTOR' : _CONSUMEREQUEST,
  '__module__' : 'events.events_pb2'
  # @@protoc_insertion_point(class_scope:events.ConsumeRequest)
  })
_sym_db.RegisterMessage(ConsumeRequest)

Event = _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), {

  'MetadataEntry' : _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _EVENT_METADATAENTRY,
    '__module__' : 'events.events_pb2'
    # @@protoc_insertion_point(class_scope:events.Event.MetadataEntry)
    })
  ,
  'DESCRIPTOR' : _EVENT,
  '__module__' : 'events.events_pb2'
  # @@protoc_insertion_point(class_scope:events.Event)
  })
_sym_db.RegisterMessage(Event)
_sym_db.RegisterMessage(Event.MetadataEntry)

ReadRequest = _reflection.GeneratedProtocolMessageType('ReadRequest', (_message.Message,), {
  'DESCRIPTOR' : _READREQUEST,
  '__module__' : 'events.events_pb2'
  # @@protoc_insertion_point(class_scope:events.ReadRequest)
  })
_sym_db.RegisterMessage(ReadRequest)

ReadResponse = _reflection.GeneratedProtocolMessageType('ReadResponse', (_message.Message,), {
  'DESCRIPTOR' : _READRESPONSE,
  '__module__' : 'events.events_pb2'
  # @@protoc_insertion_point(class_scope:events.ReadResponse)
  })
_sym_db.RegisterMessage(ReadResponse)

WriteRequest = _reflection.GeneratedProtocolMessageType('WriteRequest', (_message.Message,), {
  'DESCRIPTOR' : _WRITEREQUEST,
  '__module__' : 'events.events_pb2'
  # @@protoc_insertion_point(class_scope:events.WriteRequest)
  })
_sym_db.RegisterMessage(WriteRequest)

WriteResponse = _reflection.GeneratedProtocolMessageType('WriteResponse', (_message.Message,), {
  'DESCRIPTOR' : _WRITERESPONSE,
  '__module__' : 'events.events_pb2'
  # @@protoc_insertion_point(class_scope:events.WriteResponse)
  })
_sym_db.RegisterMessage(WriteResponse)

AckRequest = _reflection.GeneratedProtocolMessageType('AckRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACKREQUEST,
  '__module__' : 'events.events_pb2'
  # @@protoc_insertion_point(class_scope:events.AckRequest)
  })
_sym_db.RegisterMessage(AckRequest)


DESCRIPTOR._options = None
_PUBLISHREQUEST_METADATAENTRY._options = None
_EVENT_METADATAENTRY._options = None

_STREAM = _descriptor.ServiceDescriptor(
  name='Stream',
  full_name='events.Stream',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=742,
  serialized_end=862,
  methods=[
  _descriptor.MethodDescriptor(
    name='Publish',
    full_name='events.Stream.Publish',
    index=0,
    containing_service=None,
    input_type=_PUBLISHREQUEST,
    output_type=_PUBLISHRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Consume',
    full_name='events.Stream.Consume',
    index=1,
    containing_service=None,
    input_type=_CONSUMEREQUEST,
    output_type=_EVENT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_STREAM)

DESCRIPTOR.services_by_name['Stream'] = _STREAM


_STORE = _descriptor.ServiceDescriptor(
  name='Store',
  full_name='events.Store',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=864,
  serialized_end=976,
  methods=[
  _descriptor.MethodDescriptor(
    name='Read',
    full_name='events.Store.Read',
    index=0,
    containing_service=None,
    input_type=_READREQUEST,
    output_type=_READRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Write',
    full_name='events.Store.Write',
    index=1,
    containing_service=None,
    input_type=_WRITEREQUEST,
    output_type=_WRITERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_STORE)

DESCRIPTOR.services_by_name['Store'] = _STORE

# @@protoc_insertion_point(module_scope)
