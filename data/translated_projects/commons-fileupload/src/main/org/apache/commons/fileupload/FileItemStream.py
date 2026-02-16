from __future__ import annotations
from abc import ABC
from io import StringIO
import io
from io import BytesIO
import typing
from typing import *
from src.main.org.apache.commons.fileupload.FileItemHeadersSupport import *
import java # type: ignore
from src.main.org.apache.commons.fileupload.java_handler import *
class FileItemStream(ABC, metaclass=StaticFieldRedirector):
    def isFormField(self) -> bool:
        pass


    def getFieldName(self) -> str:
        pass


    def getName(self) -> str:
        pass


    def getContentType(self) -> str:
        pass


    def openStream(self) -> typing.Union[io.BytesIO, io.StringIO, io.BufferedReader]:
        pass


    javaClz = java.type("org.apache.commons.fileupload.FileItemStream")
    def __getattr__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            pass
        return JavaHandler.mapping(getattr(self.javaClz, StaticFieldRedirector.unmangle_name(name)))
class ItemSkippedException(metaclass=StaticFieldRedirector):
    javaClz = java.type("org.apache.commons.fileupload.FileItemStream$ItemSkippedException")
    def __getattr__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            pass
        return JavaHandler.mapping(getattr(self.javaClz, StaticFieldRedirector.unmangle_name(name)))