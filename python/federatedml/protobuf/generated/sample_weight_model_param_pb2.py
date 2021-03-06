# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sample-weight-model-param.proto

import sys
_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(name='sample-weight-model-param.proto', package='com.webank.ai.fate.core.mlmodel.buffer', syntax='proto3', serialized_options=_b('B\033SampleWeightModelParamProto'), serialized_pb=_b(
    '\n\x1fsample-weight-model-param.proto\x12&com.webank.ai.fate.core.mlmodel.buffer\"\xd8\x01\n\x16SampleWeightModelParam\x12\x0e\n\x06header\x18\x01 \x03(\t\x12\x13\n\x0bweight_mode\x18\x02 \x01(\t\x12\x65\n\x0c\x63lass_weight\x18\x03 \x03(\x0b\x32O.com.webank.ai.fate.core.mlmodel.buffer.SampleWeightModelParam.ClassWeightEntry\x1a\x32\n\x10\x43lassWeightEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01:\x02\x38\x01\x42\x1d\x42\x1bSampleWeightModelParamProtob\x06proto3'))


_SAMPLEWEIGHTMODELPARAM_CLASSWEIGHTENTRY = _descriptor.Descriptor(
    name='ClassWeightEntry',
    full_name='com.webank.ai.fate.core.mlmodel.buffer.SampleWeightModelParam.ClassWeightEntry',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='key',
            full_name='com.webank.ai.fate.core.mlmodel.buffer.SampleWeightModelParam.ClassWeightEntry.key',
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='value',
            full_name='com.webank.ai.fate.core.mlmodel.buffer.SampleWeightModelParam.ClassWeightEntry.value',
            index=1,
            number=2,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=_b('8\001'),
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=242,
    serialized_end=292,
)

_SAMPLEWEIGHTMODELPARAM = _descriptor.Descriptor(
    name='SampleWeightModelParam',
    full_name='com.webank.ai.fate.core.mlmodel.buffer.SampleWeightModelParam',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='header', full_name='com.webank.ai.fate.core.mlmodel.buffer.SampleWeightModelParam.header', index=0,
            number=1, type=9, cpp_type=9, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='weight_mode', full_name='com.webank.ai.fate.core.mlmodel.buffer.SampleWeightModelParam.weight_mode', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='class_weight', full_name='com.webank.ai.fate.core.mlmodel.buffer.SampleWeightModelParam.class_weight', index=2,
            number=3, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[_SAMPLEWEIGHTMODELPARAM_CLASSWEIGHTENTRY, ],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=76,
    serialized_end=292,
)

_SAMPLEWEIGHTMODELPARAM_CLASSWEIGHTENTRY.containing_type = _SAMPLEWEIGHTMODELPARAM
_SAMPLEWEIGHTMODELPARAM.fields_by_name['class_weight'].message_type = _SAMPLEWEIGHTMODELPARAM_CLASSWEIGHTENTRY
DESCRIPTOR.message_types_by_name['SampleWeightModelParam'] = _SAMPLEWEIGHTMODELPARAM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SampleWeightModelParam = _reflection.GeneratedProtocolMessageType('SampleWeightModelParam', (_message.Message,), {

    'ClassWeightEntry': _reflection.GeneratedProtocolMessageType('ClassWeightEntry', (_message.Message,), {
        'DESCRIPTOR': _SAMPLEWEIGHTMODELPARAM_CLASSWEIGHTENTRY,
        '__module__': 'sample_weight_model_param_pb2'
        # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.SampleWeightModelParam.ClassWeightEntry)
    }),
    'DESCRIPTOR': _SAMPLEWEIGHTMODELPARAM,
    '__module__': 'sample_weight_model_param_pb2'
    # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.SampleWeightModelParam)
})
_sym_db.RegisterMessage(SampleWeightModelParam)
_sym_db.RegisterMessage(SampleWeightModelParam.ClassWeightEntry)


DESCRIPTOR._options = None
_SAMPLEWEIGHTMODELPARAM_CLASSWEIGHTENTRY._options = None
# @@protoc_insertion_point(module_scope)
