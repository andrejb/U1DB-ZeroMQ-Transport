# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='message.proto',
  package='zmq_transport.common',
  serialized_pb='\n\rmessage.proto\x12\x14zmq_transport.common\"\r\n\x0bPingRequest\"\x1f\n\x10SubscribeRequest\x12\x0b\n\x03key\x18\x01 \x02(\t\"!\n\x12UnsubscribeRequest\x12\x0b\n\x03key\x18\x01 \x02(\t\"\x1d\n\x08SyncType\x12\x11\n\tsync_type\x18\x01 \x02(\t\"k\n\x07ZMQVerb\x12\x30\n\x04verb\x18\x01 \x02(\x0e\x32\".zmq_transport.common.ZMQVerb.Verb\".\n\x04Verb\x12\x07\n\x03GET\x10\x00\x12\x08\n\x04POST\x10\x01\x12\x07\n\x03PUT\x10\x02\x12\n\n\x06\x44\x45LETE\x10\x03\"A\n\x12GetSyncInfoRequest\x12\x1a\n\x12source_replica_uid\x18\x01 \x02(\t\x12\x0f\n\x07sync_id\x18\x02 \x02(\t\"\xbf\x01\n\x13GetSyncInfoResponse\x12\x1a\n\x12target_replica_uid\x18\x01 \x02(\t\x12!\n\x19target_replica_generation\x18\x02 \x02(\x05\x12\x1f\n\x17target_replica_trans_id\x18\x03 \x02(\t\x12$\n\x1csource_last_known_generation\x18\x04 \x02(\x05\x12\"\n\x1asource_last_known_trans_id\x18\x05 \x02(\t\"\xb9\x01\n\x13SendDocumentRequest\x12\x1a\n\x12source_replica_uid\x18\x01 \x02(\t\x12\x0f\n\x07sync_id\x18\x02 \x02(\t\x12\x0e\n\x06\x64oc_id\x18\x03 \x02(\t\x12\x16\n\x0e\x64oc_generation\x18\x04 \x02(\x05\x12\x13\n\x0b\x64oc_content\x18\x05 \x02(\t\x12\x19\n\x11source_generation\x18\x06 \x02(\x05\x12\x1d\n\x15source_transaction_id\x18\x07 \x02(\t\"G\n\x14SendDocumentResponse\x12\x1d\n\x15source_transaction_id\x18\x01 \x02(\t\x12\x10\n\x08inserted\x18\x02 \x02(\x08\"^\n\x12GetDocumentRequest\x12\x1a\n\x12source_replica_uid\x18\x01 \x02(\t\x12\x0f\n\x07sync_id\x18\x02 \x02(\t\x12\x1b\n\x13\x64ocs_received_count\x18\x03 \x02(\x05\"\x97\x01\n\x13GetDocumentResponse\x12\x0e\n\x06\x64oc_id\x18\x01 \x02(\t\x12\x0f\n\x07\x64oc_rev\x18\x02 \x02(\x05\x12\x16\n\x0e\x64oc_generation\x18\x03 \x02(\x05\x12\x13\n\x0b\x64oc_content\x18\x04 \x02(\t\x12\x19\n\x11target_generation\x18\x05 \x01(\x05\x12\x17\n\x0ftarget_trans_id\x18\x06 \x01(\t\"\x83\x01\n\x12PutSyncInfoRequest\x12\x0f\n\x07sync_id\x18\x01 \x02(\t\x12\x1a\n\x12source_replica_uid\x18\x02 \x02(\t\x12!\n\x19source_replica_generation\x18\x03 \x02(\x05\x12\x1d\n\x15source_transaction_id\x18\x04 \x02(\t\"F\n\x13PutSyncInfoResponse\x12\x1d\n\x15source_transaction_id\x18\x01 \x02(\t\x12\x10\n\x08inserted\x18\x02 \x02(\x08\"\xaf\t\n\nIdentifier\x12\x33\n\x04type\x18\x01 \x02(\x0e\x32%.zmq_transport.common.Identifier.Type\x12\x41\n\x11subscribe_request\x18\x02 \x01(\x0b\x32&.zmq_transport.common.SubscribeRequest\x12\x45\n\x13unsubscribe_request\x18\x03 \x01(\x0b\x32(.zmq_transport.common.UnsubscribeRequest\x12\x31\n\tsync_type\x18\x04 \x01(\x0b\x32\x1e.zmq_transport.common.SyncType\x12/\n\x08zmq_verb\x18\x05 \x01(\x0b\x32\x1d.zmq_transport.common.ZMQVerb\x12G\n\x15get_sync_info_request\x18\x06 \x01(\x0b\x32(.zmq_transport.common.GetSyncInfoRequest\x12I\n\x16get_sync_info_response\x18\x07 \x01(\x0b\x32).zmq_transport.common.GetSyncInfoResponse\x12H\n\x15send_document_request\x18\x08 \x01(\x0b\x32).zmq_transport.common.SendDocumentRequest\x12J\n\x16send_document_response\x18\t \x01(\x0b\x32*.zmq_transport.common.SendDocumentResponse\x12\x46\n\x14get_document_request\x18\n \x01(\x0b\x32(.zmq_transport.common.GetDocumentRequest\x12H\n\x15get_document_response\x18\x0b \x01(\x0b\x32).zmq_transport.common.GetDocumentResponse\x12G\n\x15put_sync_info_request\x18\x0c \x01(\x0b\x32(.zmq_transport.common.PutSyncInfoRequest\x12I\n\x16put_sync_info_response\x18\r \x01(\x0b\x32).zmq_transport.common.PutSyncInfoResponse\"\xad\x02\n\x04Type\x12\x15\n\x11SUBSCRIBE_REQUEST\x10\x01\x12\x17\n\x13UNSUBSCRIBE_REQUEST\x10\x02\x12\r\n\tSYNC_TYPE\x10\x03\x12\x0c\n\x08ZMQ_VERB\x10\x04\x12\x19\n\x15GET_SYNC_INFO_REQUEST\x10\x05\x12\x1a\n\x16GET_SYNC_INFO_RESPONSE\x10\x06\x12\x19\n\x15SEND_DOCUMENT_REQUEST\x10\x07\x12\x1a\n\x16SEND_DOCUMENT_RESPONSE\x10\x08\x12\x18\n\x14GET_DOCUMENT_REQUEST\x10\t\x12\x19\n\x15GET_DOCUMENT_RESPONSE\x10\n\x12\x19\n\x15PUT_SYNC_INFO_REQUEST\x10\x0b\x12\x1a\n\x16PUT_SYNC_INFO_RESPONSE\x10\x0c')



_ZMQVERB_VERB = _descriptor.EnumDescriptor(
  name='Verb',
  full_name='zmq_transport.common.ZMQVerb.Verb',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POST', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PUT', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELETE', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=214,
  serialized_end=260,
)

_IDENTIFIER_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='zmq_transport.common.Identifier.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SUBSCRIBE_REQUEST', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNSUBSCRIBE_REQUEST', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYNC_TYPE', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ZMQ_VERB', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_SYNC_INFO_REQUEST', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_SYNC_INFO_RESPONSE', index=5, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEND_DOCUMENT_REQUEST', index=6, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEND_DOCUMENT_RESPONSE', index=7, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_DOCUMENT_REQUEST', index=8, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_DOCUMENT_RESPONSE', index=9, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PUT_SYNC_INFO_REQUEST', index=10, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PUT_SYNC_INFO_RESPONSE', index=11, number=12,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2139,
  serialized_end=2440,
)


_PINGREQUEST = _descriptor.Descriptor(
  name='PingRequest',
  full_name='zmq_transport.common.PingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=39,
  serialized_end=52,
)


_SUBSCRIBEREQUEST = _descriptor.Descriptor(
  name='SubscribeRequest',
  full_name='zmq_transport.common.SubscribeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='zmq_transport.common.SubscribeRequest.key', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=54,
  serialized_end=85,
)


_UNSUBSCRIBEREQUEST = _descriptor.Descriptor(
  name='UnsubscribeRequest',
  full_name='zmq_transport.common.UnsubscribeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='zmq_transport.common.UnsubscribeRequest.key', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=87,
  serialized_end=120,
)


_SYNCTYPE = _descriptor.Descriptor(
  name='SyncType',
  full_name='zmq_transport.common.SyncType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sync_type', full_name='zmq_transport.common.SyncType.sync_type', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=122,
  serialized_end=151,
)


_ZMQVERB = _descriptor.Descriptor(
  name='ZMQVerb',
  full_name='zmq_transport.common.ZMQVerb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='verb', full_name='zmq_transport.common.ZMQVerb.verb', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ZMQVERB_VERB,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=153,
  serialized_end=260,
)


_GETSYNCINFOREQUEST = _descriptor.Descriptor(
  name='GetSyncInfoRequest',
  full_name='zmq_transport.common.GetSyncInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='source_replica_uid', full_name='zmq_transport.common.GetSyncInfoRequest.source_replica_uid', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sync_id', full_name='zmq_transport.common.GetSyncInfoRequest.sync_id', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=262,
  serialized_end=327,
)


_GETSYNCINFORESPONSE = _descriptor.Descriptor(
  name='GetSyncInfoResponse',
  full_name='zmq_transport.common.GetSyncInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target_replica_uid', full_name='zmq_transport.common.GetSyncInfoResponse.target_replica_uid', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target_replica_generation', full_name='zmq_transport.common.GetSyncInfoResponse.target_replica_generation', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target_replica_trans_id', full_name='zmq_transport.common.GetSyncInfoResponse.target_replica_trans_id', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source_last_known_generation', full_name='zmq_transport.common.GetSyncInfoResponse.source_last_known_generation', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source_last_known_trans_id', full_name='zmq_transport.common.GetSyncInfoResponse.source_last_known_trans_id', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=330,
  serialized_end=521,
)


_SENDDOCUMENTREQUEST = _descriptor.Descriptor(
  name='SendDocumentRequest',
  full_name='zmq_transport.common.SendDocumentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='source_replica_uid', full_name='zmq_transport.common.SendDocumentRequest.source_replica_uid', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sync_id', full_name='zmq_transport.common.SendDocumentRequest.sync_id', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='doc_id', full_name='zmq_transport.common.SendDocumentRequest.doc_id', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='doc_generation', full_name='zmq_transport.common.SendDocumentRequest.doc_generation', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='doc_content', full_name='zmq_transport.common.SendDocumentRequest.doc_content', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source_generation', full_name='zmq_transport.common.SendDocumentRequest.source_generation', index=5,
      number=6, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source_transaction_id', full_name='zmq_transport.common.SendDocumentRequest.source_transaction_id', index=6,
      number=7, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=524,
  serialized_end=709,
)


_SENDDOCUMENTRESPONSE = _descriptor.Descriptor(
  name='SendDocumentResponse',
  full_name='zmq_transport.common.SendDocumentResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='source_transaction_id', full_name='zmq_transport.common.SendDocumentResponse.source_transaction_id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inserted', full_name='zmq_transport.common.SendDocumentResponse.inserted', index=1,
      number=2, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=711,
  serialized_end=782,
)


_GETDOCUMENTREQUEST = _descriptor.Descriptor(
  name='GetDocumentRequest',
  full_name='zmq_transport.common.GetDocumentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='source_replica_uid', full_name='zmq_transport.common.GetDocumentRequest.source_replica_uid', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sync_id', full_name='zmq_transport.common.GetDocumentRequest.sync_id', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='docs_received_count', full_name='zmq_transport.common.GetDocumentRequest.docs_received_count', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=784,
  serialized_end=878,
)


_GETDOCUMENTRESPONSE = _descriptor.Descriptor(
  name='GetDocumentResponse',
  full_name='zmq_transport.common.GetDocumentResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='doc_id', full_name='zmq_transport.common.GetDocumentResponse.doc_id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='doc_rev', full_name='zmq_transport.common.GetDocumentResponse.doc_rev', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='doc_generation', full_name='zmq_transport.common.GetDocumentResponse.doc_generation', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='doc_content', full_name='zmq_transport.common.GetDocumentResponse.doc_content', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target_generation', full_name='zmq_transport.common.GetDocumentResponse.target_generation', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target_trans_id', full_name='zmq_transport.common.GetDocumentResponse.target_trans_id', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=881,
  serialized_end=1032,
)


_PUTSYNCINFOREQUEST = _descriptor.Descriptor(
  name='PutSyncInfoRequest',
  full_name='zmq_transport.common.PutSyncInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sync_id', full_name='zmq_transport.common.PutSyncInfoRequest.sync_id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source_replica_uid', full_name='zmq_transport.common.PutSyncInfoRequest.source_replica_uid', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source_replica_generation', full_name='zmq_transport.common.PutSyncInfoRequest.source_replica_generation', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source_transaction_id', full_name='zmq_transport.common.PutSyncInfoRequest.source_transaction_id', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1035,
  serialized_end=1166,
)


_PUTSYNCINFORESPONSE = _descriptor.Descriptor(
  name='PutSyncInfoResponse',
  full_name='zmq_transport.common.PutSyncInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='source_transaction_id', full_name='zmq_transport.common.PutSyncInfoResponse.source_transaction_id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inserted', full_name='zmq_transport.common.PutSyncInfoResponse.inserted', index=1,
      number=2, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1168,
  serialized_end=1238,
)


_IDENTIFIER = _descriptor.Descriptor(
  name='Identifier',
  full_name='zmq_transport.common.Identifier',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='zmq_transport.common.Identifier.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='subscribe_request', full_name='zmq_transport.common.Identifier.subscribe_request', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unsubscribe_request', full_name='zmq_transport.common.Identifier.unsubscribe_request', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sync_type', full_name='zmq_transport.common.Identifier.sync_type', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='zmq_verb', full_name='zmq_transport.common.Identifier.zmq_verb', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='get_sync_info_request', full_name='zmq_transport.common.Identifier.get_sync_info_request', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='get_sync_info_response', full_name='zmq_transport.common.Identifier.get_sync_info_response', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='send_document_request', full_name='zmq_transport.common.Identifier.send_document_request', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='send_document_response', full_name='zmq_transport.common.Identifier.send_document_response', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='get_document_request', full_name='zmq_transport.common.Identifier.get_document_request', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='get_document_response', full_name='zmq_transport.common.Identifier.get_document_response', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='put_sync_info_request', full_name='zmq_transport.common.Identifier.put_sync_info_request', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='put_sync_info_response', full_name='zmq_transport.common.Identifier.put_sync_info_response', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _IDENTIFIER_TYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1241,
  serialized_end=2440,
)

_ZMQVERB.fields_by_name['verb'].enum_type = _ZMQVERB_VERB
_ZMQVERB_VERB.containing_type = _ZMQVERB;
_IDENTIFIER.fields_by_name['type'].enum_type = _IDENTIFIER_TYPE
_IDENTIFIER.fields_by_name['subscribe_request'].message_type = _SUBSCRIBEREQUEST
_IDENTIFIER.fields_by_name['unsubscribe_request'].message_type = _UNSUBSCRIBEREQUEST
_IDENTIFIER.fields_by_name['sync_type'].message_type = _SYNCTYPE
_IDENTIFIER.fields_by_name['zmq_verb'].message_type = _ZMQVERB
_IDENTIFIER.fields_by_name['get_sync_info_request'].message_type = _GETSYNCINFOREQUEST
_IDENTIFIER.fields_by_name['get_sync_info_response'].message_type = _GETSYNCINFORESPONSE
_IDENTIFIER.fields_by_name['send_document_request'].message_type = _SENDDOCUMENTREQUEST
_IDENTIFIER.fields_by_name['send_document_response'].message_type = _SENDDOCUMENTRESPONSE
_IDENTIFIER.fields_by_name['get_document_request'].message_type = _GETDOCUMENTREQUEST
_IDENTIFIER.fields_by_name['get_document_response'].message_type = _GETDOCUMENTRESPONSE
_IDENTIFIER.fields_by_name['put_sync_info_request'].message_type = _PUTSYNCINFOREQUEST
_IDENTIFIER.fields_by_name['put_sync_info_response'].message_type = _PUTSYNCINFORESPONSE
_IDENTIFIER_TYPE.containing_type = _IDENTIFIER;
DESCRIPTOR.message_types_by_name['PingRequest'] = _PINGREQUEST
DESCRIPTOR.message_types_by_name['SubscribeRequest'] = _SUBSCRIBEREQUEST
DESCRIPTOR.message_types_by_name['UnsubscribeRequest'] = _UNSUBSCRIBEREQUEST
DESCRIPTOR.message_types_by_name['SyncType'] = _SYNCTYPE
DESCRIPTOR.message_types_by_name['ZMQVerb'] = _ZMQVERB
DESCRIPTOR.message_types_by_name['GetSyncInfoRequest'] = _GETSYNCINFOREQUEST
DESCRIPTOR.message_types_by_name['GetSyncInfoResponse'] = _GETSYNCINFORESPONSE
DESCRIPTOR.message_types_by_name['SendDocumentRequest'] = _SENDDOCUMENTREQUEST
DESCRIPTOR.message_types_by_name['SendDocumentResponse'] = _SENDDOCUMENTRESPONSE
DESCRIPTOR.message_types_by_name['GetDocumentRequest'] = _GETDOCUMENTREQUEST
DESCRIPTOR.message_types_by_name['GetDocumentResponse'] = _GETDOCUMENTRESPONSE
DESCRIPTOR.message_types_by_name['PutSyncInfoRequest'] = _PUTSYNCINFOREQUEST
DESCRIPTOR.message_types_by_name['PutSyncInfoResponse'] = _PUTSYNCINFORESPONSE
DESCRIPTOR.message_types_by_name['Identifier'] = _IDENTIFIER

class PingRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PINGREQUEST

  # @@protoc_insertion_point(class_scope:zmq_transport.common.PingRequest)

class SubscribeRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SUBSCRIBEREQUEST

  # @@protoc_insertion_point(class_scope:zmq_transport.common.SubscribeRequest)

class UnsubscribeRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _UNSUBSCRIBEREQUEST

  # @@protoc_insertion_point(class_scope:zmq_transport.common.UnsubscribeRequest)

class SyncType(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SYNCTYPE

  # @@protoc_insertion_point(class_scope:zmq_transport.common.SyncType)

class ZMQVerb(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ZMQVERB

  # @@protoc_insertion_point(class_scope:zmq_transport.common.ZMQVerb)

class GetSyncInfoRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETSYNCINFOREQUEST

  # @@protoc_insertion_point(class_scope:zmq_transport.common.GetSyncInfoRequest)

class GetSyncInfoResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETSYNCINFORESPONSE

  # @@protoc_insertion_point(class_scope:zmq_transport.common.GetSyncInfoResponse)

class SendDocumentRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SENDDOCUMENTREQUEST

  # @@protoc_insertion_point(class_scope:zmq_transport.common.SendDocumentRequest)

class SendDocumentResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SENDDOCUMENTRESPONSE

  # @@protoc_insertion_point(class_scope:zmq_transport.common.SendDocumentResponse)

class GetDocumentRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETDOCUMENTREQUEST

  # @@protoc_insertion_point(class_scope:zmq_transport.common.GetDocumentRequest)

class GetDocumentResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETDOCUMENTRESPONSE

  # @@protoc_insertion_point(class_scope:zmq_transport.common.GetDocumentResponse)

class PutSyncInfoRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PUTSYNCINFOREQUEST

  # @@protoc_insertion_point(class_scope:zmq_transport.common.PutSyncInfoRequest)

class PutSyncInfoResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PUTSYNCINFORESPONSE

  # @@protoc_insertion_point(class_scope:zmq_transport.common.PutSyncInfoResponse)

class Identifier(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _IDENTIFIER

  # @@protoc_insertion_point(class_scope:zmq_transport.common.Identifier)


# @@protoc_insertion_point(module_scope)
