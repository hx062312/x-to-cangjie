from __future__ import annotations
from abc import ABC
import pathlib
from io import StringIO
import io
from io import BytesIO
import typing
from typing import *
from src.main.org.apache.commons.fileupload.FileItemHeadersSupport import *
import java # type: ignore
from src.main.org.apache.commons.fileupload.java_handler import *
class FileItem(ABC, metaclass=StaticFieldRedirector):
    def getOutputStream(self) -> typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter]:
        pass


    def setFormField(self, state: bool) -> None:
        pass


    def isFormField(self) -> bool:
        pass


    def setFieldName(self, name: str) -> None:
        pass


    def getFieldName(self) -> str:
        pass


    def delete(self) -> None:
        pass


    def write(self, file: pathlib.Path) -> None:
        pass


    def getString1(self) -> str:
        pass


    def getString0(self, encoding: str) -> str:
        pass


    def get(self) -> typing.List[int]:
        pass


    def getSize(self) -> int:
        pass


    def isInMemory(self) -> bool:
        pass


    def getName(self) -> str:
        pass


    def getContentType(self) -> str:
        pass


    def getInputStream(self) -> typing.Union[io.BytesIO, io.StringIO, io.BufferedReader]:
        pass


    javaClz = java.type("org.apache.commons.fileupload.FileItem")
    def __getattr__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            pass
        return JavaHandler.mapping(getattr(self.javaClz, StaticFieldRedirector.unmangle_name(name)))