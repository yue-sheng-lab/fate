# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pipeline.proto

import sys
_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(name='pipeline.proto', package='com.webank.ai.fate.core.mlmodel.buffer', syntax='proto3', serialized_options=_b('B\rPipelineProto'), serialized_pb=_b(
    '\n\x0epipeline.proto\x12&com.webank.ai.fate.core.mlmodel.buffer\"\xbf\x02\n\x08Pipeline\x12\x15\n\rinference_dsl\x18\x01 \x01(\x0c\x12\x11\n\ttrain_dsl\x18\x02 \x01(\x0c\x12\x1a\n\x12train_runtime_conf\x18\x03 \x01(\x0c\x12\x14\n\x0c\x66\x61te_version\x18\x04 \x01(\t\x12\x10\n\x08model_id\x18\x05 \x01(\t\x12\x15\n\rmodel_version\x18\x06 \x01(\t\x12\x0e\n\x06parent\x18\x07 \x01(\x08\x12\x14\n\x0cloaded_times\x18\x08 \x01(\x05\x12\r\n\x05roles\x18\t \x01(\x0c\x12\x11\n\twork_mode\x18\n \x01(\x05\x12\x16\n\x0einitiator_role\x18\x0b \x01(\t\x12\x1a\n\x12initiator_party_id\x18\x0c \x01(\x05\x12\x1d\n\x15runtime_conf_on_party\x18\r \x01(\x0c\x12\x13\n\x0bparent_info\x18\x0e \x01(\x0c\x42\x0f\x42\rPipelineProtob\x06proto3'))


_PIPELINE = _descriptor.Descriptor(
    name='Pipeline',
    full_name='com.webank.ai.fate.core.mlmodel.buffer.Pipeline',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='inference_dsl', full_name='com.webank.ai.fate.core.mlmodel.buffer.Pipeline.inference_dsl', index=0,
            number=1, type=12, cpp_type=9, label=1,
            has_default_value=False, default_value=_b(""),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='train_dsl', full_name='com.webank.ai.fate.core.mlmodel.buffer.Pipeline.train_dsl', index=1,
            number=2, type=12, cpp_type=9, label=1,
            has_default_value=False, default_value=_b(""),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='train_runtime_conf', full_name='com.webank.ai.fate.core.mlmodel.buffer.Pipeline.train_runtime_conf', index=2,
            number=3, type=12, cpp_type=9, label=1,
            has_default_value=False, default_value=_b(""),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='fate_version', full_name='com.webank.ai.fate.core.mlmodel.buffer.Pipeline.fate_version', index=3,
            number=4, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='model_id', full_name='com.webank.ai.fate.core.mlmodel.buffer.Pipeline.model_id', index=4,
            number=5, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='model_version', full_name='com.webank.ai.fate.core.mlmodel.buffer.Pipeline.model_version', index=5,
            number=6, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='parent', full_name='com.webank.ai.fate.core.mlmodel.buffer.Pipeline.parent', index=6,
            number=7, type=8, cpp_type=7, label=1,
            has_default_value=False, default_value=False,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='loaded_times', full_name='com.webank.ai.fate.core.mlmodel.buffer.Pipeline.loaded_times', index=7,
            number=8, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='roles', full_name='com.webank.ai.fate.core.mlmodel.buffer.Pipeline.roles', index=8,
            number=9, type=12, cpp_type=9, label=1,
            has_default_value=False, default_value=_b(""),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='work_mode', full_name='com.webank.ai.fate.core.mlmodel.buffer.Pipeline.work_mode', index=9,
            number=10, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='initiator_role', full_name='com.webank.ai.fate.core.mlmodel.buffer.Pipeline.initiator_role', index=10,
            number=11, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='initiator_party_id', full_name='com.webank.ai.fate.core.mlmodel.buffer.Pipeline.initiator_party_id', index=11,
            number=12, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='runtime_conf_on_party', full_name='com.webank.ai.fate.core.mlmodel.buffer.Pipeline.runtime_conf_on_party', index=12,
            number=13, type=12, cpp_type=9, label=1,
            has_default_value=False, default_value=_b(""),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='parent_info', full_name='com.webank.ai.fate.core.mlmodel.buffer.Pipeline.parent_info', index=13,
            number=14, type=12, cpp_type=9, label=1,
            has_default_value=False, default_value=_b(""),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
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
    serialized_start=59,
    serialized_end=378,
)

DESCRIPTOR.message_types_by_name['Pipeline'] = _PIPELINE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Pipeline = _reflection.GeneratedProtocolMessageType('Pipeline', (_message.Message,), {
    'DESCRIPTOR': _PIPELINE,
    '__module__': 'pipeline_pb2'
    # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.Pipeline)
})
_sym_db.RegisterMessage(Pipeline)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
