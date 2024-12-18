# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: glossary.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eglossary.proto\x12\x08glossary\"5\n\x04Term\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04term\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\"/\n\x10ListTermsRequest\x12\x0c\n\x04skip\x18\x01 \x01(\x05\x12\r\n\x05limit\x18\x02 \x01(\x05\"A\n\x11ListTermsResponse\x12\x1d\n\x05terms\x18\x01 \x03(\x0b\x32\x0e.glossary.Term\x12\r\n\x05total\x18\x02 \x01(\x05\"\x1e\n\x0eGetTermRequest\x12\x0c\n\x04term\x18\x01 \x01(\t\"6\n\x11\x43reateTermRequest\x12\x0c\n\x04term\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\"6\n\x11UpdateTermRequest\x12\x0c\n\x04term\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\"!\n\x11\x44\x65leteTermRequest\x12\x0c\n\x04term\x18\x01 \x01(\t\"6\n\x12\x44\x65leteTermResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"#\n\x12SearchTermsRequest\x12\r\n\x05query\x18\x01 \x01(\t2\x96\x03\n\x0fGlossaryService\x12\x46\n\tListTerms\x12\x1a.glossary.ListTermsRequest\x1a\x1b.glossary.ListTermsResponse\"\x00\x12\x35\n\x07GetTerm\x12\x18.glossary.GetTermRequest\x1a\x0e.glossary.Term\"\x00\x12;\n\nCreateTerm\x12\x1b.glossary.CreateTermRequest\x1a\x0e.glossary.Term\"\x00\x12;\n\nUpdateTerm\x12\x1b.glossary.UpdateTermRequest\x1a\x0e.glossary.Term\"\x00\x12I\n\nDeleteTerm\x12\x1b.glossary.DeleteTermRequest\x1a\x1c.glossary.DeleteTermResponse\"\x00\x12?\n\x0bSearchTerms\x12\x1c.glossary.SearchTermsRequest\x1a\x0e.glossary.Term\"\x00\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'glossary_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_TERM']._serialized_start=28
  _globals['_TERM']._serialized_end=81
  _globals['_LISTTERMSREQUEST']._serialized_start=83
  _globals['_LISTTERMSREQUEST']._serialized_end=130
  _globals['_LISTTERMSRESPONSE']._serialized_start=132
  _globals['_LISTTERMSRESPONSE']._serialized_end=197
  _globals['_GETTERMREQUEST']._serialized_start=199
  _globals['_GETTERMREQUEST']._serialized_end=229
  _globals['_CREATETERMREQUEST']._serialized_start=231
  _globals['_CREATETERMREQUEST']._serialized_end=285
  _globals['_UPDATETERMREQUEST']._serialized_start=287
  _globals['_UPDATETERMREQUEST']._serialized_end=341
  _globals['_DELETETERMREQUEST']._serialized_start=343
  _globals['_DELETETERMREQUEST']._serialized_end=376
  _globals['_DELETETERMRESPONSE']._serialized_start=378
  _globals['_DELETETERMRESPONSE']._serialized_end=432
  _globals['_SEARCHTERMSREQUEST']._serialized_start=434
  _globals['_SEARCHTERMSREQUEST']._serialized_end=469
  _globals['_GLOSSARYSERVICE']._serialized_start=472
  _globals['_GLOSSARYSERVICE']._serialized_end=878
# @@protoc_insertion_point(module_scope)
