from __future__ import annotations
from abc import ABC
from io import StringIO
import io
from io import BytesIO
import typing
from typing import *
import java # type: ignore
from src.main.org.apache.commons.fileupload.java_handler import *
class RequestContext(ABC, metaclass=StaticFieldRedirector):
    def getInputStream(self) -> typing.Union[io.BytesIO, io.StringIO, io.BufferedReader]:
        pass


    def getContentLength(self) -> int:
        pass


    def getContentType(self) -> str:
        pass


    def getCharacterEncoding(self) -> str:
        pass


    javaClz = java.type("org.apache.commons.fileupload.RequestContext")
    def __getattr__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            pass
        return JavaHandler.mapping(getattr(self.javaClz, StaticFieldRedirector.unmangle_name(name)))