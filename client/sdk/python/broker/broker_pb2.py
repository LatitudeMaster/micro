# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: broker/broker.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='broker/broker.proto',
  package='broker',
  syntax='proto3',
  serialized_options=b'Z-github.com/micro-community/micro/v3/proto/broker;broker',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13\x62roker/broker.proto\x12\x06\x62roker\"\x07\n\x05\x45mpty\"A\n\x0ePublishRequest\x12\r\n\x05topic\x18\x01 \x01(\t\x12 \n\x07message\x18\x02 \x01(\x0b\x32\x0f.broker.Message\"0\n\x10SubscribeRequest\x12\r\n\x05topic\x18\x01 \x01(\t\x12\r\n\x05queue\x18\x02 \x01(\t\"s\n\x07Message\x12+\n\x06header\x18\x01 \x03(\x0b\x32\x1b.broker.Message.HeaderEntry\x12\x0c\n\x04\x62ody\x18\x02 \x01(\x0c\x1a-\n\x0bHeaderEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x32x\n\x06\x42roker\x12\x32\n\x07Publish\x12\x16.broker.PublishRequest\x1a\r.broker.Empty\"\x00\x12:\n\tSubscribe\x12\x18.broker.SubscribeRequest\x1a\x0f.broker.Message\"\x00\x30\x01\x42/Z-github.com/micro-community/micro/v3/proto/broker;brokerb\x06proto3'
)




_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='broker.Empty',
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
  serialized_start=31,
  serialized_end=38,
)


_PUBLISHREQUEST = _descriptor.Descriptor(
  name='PublishRequest',
  full_name='broker.PublishRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='topic', full_name='broker.PublishRequest.topic', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='broker.PublishRequest.message', index=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=40,
  serialized_end=105,
)


_SUBSCRIBEREQUEST = _descriptor.Descriptor(
  name='SubscribeRequest',
  full_name='broker.SubscribeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='topic', full_name='broker.SubscribeRequest.topic', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='queue', full_name='broker.SubscribeRequest.queue', index=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=107,
  serialized_end=155,
)


_MESSAGE_HEADERENTRY = _descriptor.Descriptor(
  name='HeaderEntry',
  full_name='broker.Message.HeaderEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='broker.Message.HeaderEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='broker.Message.HeaderEntry.value', index=1,
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
  serialized_start=227,
  serialized_end=272,
)

_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='broker.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='broker.Message.header', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='body', full_name='broker.Message.body', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_MESSAGE_HEADERENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=157,
  serialized_end=272,
)

_PUBLISHREQUEST.fields_by_name['message'].message_type = _MESSAGE
_MESSAGE_HEADERENTRY.containing_type = _MESSAGE
_MESSAGE.fields_by_name['header'].message_type = _MESSAGE_HEADERENTRY
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['PublishRequest'] = _PUBLISHREQUEST
DESCRIPTOR.message_types_by_name['SubscribeRequest'] = _SUBSCRIBEREQUEST
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'broker.broker_pb2'
  # @@protoc_insertion_point(class_scope:broker.Empty)
  })
_sym_db.RegisterMessage(Empty)

PublishRequest = _reflection.GeneratedProtocolMessageType('PublishRequest', (_message.Message,), {
  'DESCRIPTOR' : _PUBLISHREQUEST,
  '__module__' : 'broker.broker_pb2'
  # @@protoc_insertion_point(class_scope:broker.PublishRequest)
  })
_sym_db.RegisterMessage(PublishRequest)

SubscribeRequest = _reflection.GeneratedProtocolMessageType('SubscribeRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBEREQUEST,
  '__module__' : 'broker.broker_pb2'
  # @@protoc_insertion_point(class_scope:broker.SubscribeRequest)
  })
_sym_db.RegisterMessage(SubscribeRequest)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), {

  'HeaderEntry' : _reflection.GeneratedProtocolMessageType('HeaderEntry', (_message.Message,), {
    'DESCRIPTOR' : _MESSAGE_HEADERENTRY,
    '__module__' : 'broker.broker_pb2'
    # @@protoc_insertion_point(class_scope:broker.Message.HeaderEntry)
    })
  ,
  'DESCRIPTOR' : _MESSAGE,
  '__module__' : 'broker.broker_pb2'
  # @@protoc_insertion_point(class_scope:broker.Message)
  })
_sym_db.RegisterMessage(Message)
_sym_db.RegisterMessage(Message.HeaderEntry)


DESCRIPTOR._options = None
_MESSAGE_HEADERENTRY._options = None

_BROKER = _descriptor.ServiceDescriptor(
  name='Broker',
  full_name='broker.Broker',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=274,
  serialized_end=394,
  methods=[
  _descriptor.MethodDescriptor(
    name='Publish',
    full_name='broker.Broker.Publish',
    index=0,
    containing_service=None,
    input_type=_PUBLISHREQUEST,
    output_type=_EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Subscribe',
    full_name='broker.Broker.Subscribe',
    index=1,
    containing_service=None,
    input_type=_SUBSCRIBEREQUEST,
    output_type=_MESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_BROKER)

DESCRIPTOR.services_by_name['Broker'] = _BROKER

# @@protoc_insertion_point(module_scope)
