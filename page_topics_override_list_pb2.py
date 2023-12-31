# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: page_topics_override_list.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='page_topics_override_list.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1fpage_topics_override_list.proto\"C\n\x16PageTopicsOverrideList\x12)\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x18.PageTopicsOverrideEntry\"O\n\x17PageTopicsOverrideEntry\x12\x0e\n\x06\x64omain\x18\x01 \x01(\t\x12$\n\x06topics\x18\x02 \x01(\x0b\x32\x14.AnnotatedPageTopics\"(\n\x13\x41nnotatedPageTopics\x12\x11\n\ttopic_ids\x18\x01 \x03(\x05'
)




_PAGETOPICSOVERRIDELIST = _descriptor.Descriptor(
  name='PageTopicsOverrideList',
  full_name='PageTopicsOverrideList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='entries', full_name='PageTopicsOverrideList.entries', index=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=35,
  serialized_end=102,
)


_PAGETOPICSOVERRIDEENTRY = _descriptor.Descriptor(
  name='PageTopicsOverrideEntry',
  full_name='PageTopicsOverrideEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='domain', full_name='PageTopicsOverrideEntry.domain', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='topics', full_name='PageTopicsOverrideEntry.topics', index=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=104,
  serialized_end=183,
)


_ANNOTATEDPAGETOPICS = _descriptor.Descriptor(
  name='AnnotatedPageTopics',
  full_name='AnnotatedPageTopics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='topic_ids', full_name='AnnotatedPageTopics.topic_ids', index=0,
      number=1, type=5, cpp_type=1, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=185,
  serialized_end=225,
)

_PAGETOPICSOVERRIDELIST.fields_by_name['entries'].message_type = _PAGETOPICSOVERRIDEENTRY
_PAGETOPICSOVERRIDEENTRY.fields_by_name['topics'].message_type = _ANNOTATEDPAGETOPICS
DESCRIPTOR.message_types_by_name['PageTopicsOverrideList'] = _PAGETOPICSOVERRIDELIST
DESCRIPTOR.message_types_by_name['PageTopicsOverrideEntry'] = _PAGETOPICSOVERRIDEENTRY
DESCRIPTOR.message_types_by_name['AnnotatedPageTopics'] = _ANNOTATEDPAGETOPICS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PageTopicsOverrideList = _reflection.GeneratedProtocolMessageType('PageTopicsOverrideList', (_message.Message,), {
  'DESCRIPTOR' : _PAGETOPICSOVERRIDELIST,
  '__module__' : 'page_topics_override_list_pb2'
  # @@protoc_insertion_point(class_scope:PageTopicsOverrideList)
  })
_sym_db.RegisterMessage(PageTopicsOverrideList)

PageTopicsOverrideEntry = _reflection.GeneratedProtocolMessageType('PageTopicsOverrideEntry', (_message.Message,), {
  'DESCRIPTOR' : _PAGETOPICSOVERRIDEENTRY,
  '__module__' : 'page_topics_override_list_pb2'
  # @@protoc_insertion_point(class_scope:PageTopicsOverrideEntry)
  })
_sym_db.RegisterMessage(PageTopicsOverrideEntry)

AnnotatedPageTopics = _reflection.GeneratedProtocolMessageType('AnnotatedPageTopics', (_message.Message,), {
  'DESCRIPTOR' : _ANNOTATEDPAGETOPICS,
  '__module__' : 'page_topics_override_list_pb2'
  # @@protoc_insertion_point(class_scope:AnnotatedPageTopics)
  })
_sym_db.RegisterMessage(AnnotatedPageTopics)


# @@protoc_insertion_point(module_scope)
