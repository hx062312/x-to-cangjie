from __future__ import annotations
from abc import ABC
import io
import typing
from typing import *
import java # type: ignore
from src.main.org.apache.commons.fileupload.java_handler import *
class FileItemHeaders(ABC, metaclass=StaticFieldRedirector):
    def getHeaderNames(self) -> typing.Iterator[str]:
        pass


    def getHeaders(self, name: str) -> typing.Iterator[str]:
        pass


    def getHeader(self, name: str) -> str:
        pass


    javaClz = java.type("org.apache.commons.fileupload.FileItemHeaders")
    def __getattr__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            pass
        return JavaHandler.mapping(getattr(self.javaClz, StaticFieldRedirector.unmangle_name(name)))