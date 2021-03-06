# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ftl-model-meta.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name='ftl-model-meta.proto',
    package='com.webank.ai.fate.core.mlmodel.buffer',
    syntax='proto3',
    serialized_options=b'B\021FTLModelMetaProto',
    serialized_pb=b'\n\x14\x66tl-model-meta.proto\x12&com.webank.ai.fate.core.mlmodel.buffer\"6\n\x11\x46TLOptimizerParam\x12\x11\n\toptimizer\x18\x01 \x01(\t\x12\x0e\n\x06kwargs\x18\x02 \x01(\t\"$\n\x0f\x46TLPredictParam\x12\x11\n\tthreshold\x18\x01 \x01(\x01\"\x9e\x02\n\x0c\x46TLModelMeta\x12\x13\n\x0b\x63onfig_type\x18\x01 \x01(\t\x12\x11\n\tnn_define\x18\x02 \x01(\t\x12\x12\n\nbatch_size\x18\x03 \x01(\x05\x12\x0e\n\x06\x65pochs\x18\x04 \x01(\x05\x12\x0b\n\x03tol\x18\x05 \x01(\x01\x12R\n\x0foptimizer_param\x18\x06 \x01(\x0b\x32\x39.com.webank.ai.fate.core.mlmodel.buffer.FTLOptimizerParam\x12N\n\rpredict_param\x18\x07 \x01(\x0b\x32\x37.com.webank.ai.fate.core.mlmodel.buffer.FTLPredictParam\x12\x11\n\tinput_dim\x18\x08 \x01(\x05\x42\x13\x42\x11\x46TLModelMetaProtob\x06proto3'
)


_FTLOPTIMIZERPARAM = _descriptor.Descriptor(
    name='FTLOptimizerParam',
    full_name='com.webank.ai.fate.core.mlmodel.buffer.FTLOptimizerParam',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='optimizer', full_name='com.webank.ai.fate.core.mlmodel.buffer.FTLOptimizerParam.optimizer', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='kwargs', full_name='com.webank.ai.fate.core.mlmodel.buffer.FTLOptimizerParam.kwargs', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
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
    serialized_start=64,
    serialized_end=118,
)


_FTLPREDICTPARAM = _descriptor.Descriptor(
    name='FTLPredictParam',
    full_name='com.webank.ai.fate.core.mlmodel.buffer.FTLPredictParam',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='threshold', full_name='com.webank.ai.fate.core.mlmodel.buffer.FTLPredictParam.threshold', index=0,
            number=1, type=1, cpp_type=5, label=1,
            has_default_value=False, default_value=float(0),
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
    serialized_start=120,
    serialized_end=156,
)


_FTLMODELMETA = _descriptor.Descriptor(
    name='FTLModelMeta',
    full_name='com.webank.ai.fate.core.mlmodel.buffer.FTLModelMeta',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='config_type', full_name='com.webank.ai.fate.core.mlmodel.buffer.FTLModelMeta.config_type', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='nn_define', full_name='com.webank.ai.fate.core.mlmodel.buffer.FTLModelMeta.nn_define', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='batch_size', full_name='com.webank.ai.fate.core.mlmodel.buffer.FTLModelMeta.batch_size', index=2,
            number=3, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='epochs', full_name='com.webank.ai.fate.core.mlmodel.buffer.FTLModelMeta.epochs', index=3,
            number=4, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='tol', full_name='com.webank.ai.fate.core.mlmodel.buffer.FTLModelMeta.tol', index=4,
            number=5, type=1, cpp_type=5, label=1,
            has_default_value=False, default_value=float(0),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='optimizer_param', full_name='com.webank.ai.fate.core.mlmodel.buffer.FTLModelMeta.optimizer_param', index=5,
            number=6, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='predict_param', full_name='com.webank.ai.fate.core.mlmodel.buffer.FTLModelMeta.predict_param', index=6,
            number=7, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='input_dim', full_name='com.webank.ai.fate.core.mlmodel.buffer.FTLModelMeta.input_dim', index=7,
            number=8, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
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
    serialized_start=159,
    serialized_end=445,
)

_FTLMODELMETA.fields_by_name['optimizer_param'].message_type = _FTLOPTIMIZERPARAM
_FTLMODELMETA.fields_by_name['predict_param'].message_type = _FTLPREDICTPARAM
DESCRIPTOR.message_types_by_name['FTLOptimizerParam'] = _FTLOPTIMIZERPARAM
DESCRIPTOR.message_types_by_name['FTLPredictParam'] = _FTLPREDICTPARAM
DESCRIPTOR.message_types_by_name['FTLModelMeta'] = _FTLMODELMETA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FTLOptimizerParam = _reflection.GeneratedProtocolMessageType('FTLOptimizerParam', (_message.Message,), {
    'DESCRIPTOR': _FTLOPTIMIZERPARAM,
    '__module__': 'ftl_model_meta_pb2'
    # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.FTLOptimizerParam)
})
_sym_db.RegisterMessage(FTLOptimizerParam)

FTLPredictParam = _reflection.GeneratedProtocolMessageType('FTLPredictParam', (_message.Message,), {
    'DESCRIPTOR': _FTLPREDICTPARAM,
    '__module__': 'ftl_model_meta_pb2'
    # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.FTLPredictParam)
})
_sym_db.RegisterMessage(FTLPredictParam)

FTLModelMeta = _reflection.GeneratedProtocolMessageType('FTLModelMeta', (_message.Message,), {
    'DESCRIPTOR': _FTLMODELMETA,
    '__module__': 'ftl_model_meta_pb2'
    # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.FTLModelMeta)
})
_sym_db.RegisterMessage(FTLModelMeta)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
