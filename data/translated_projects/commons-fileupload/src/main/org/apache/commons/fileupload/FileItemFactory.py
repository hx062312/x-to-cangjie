from __future__ import annotations
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.fileupload.FileItem import *
import java # type: ignore
from src.main.org.apache.commons.fileupload.java_handler import *
class FileItemFactory(ABC, metaclass=StaticFieldRedirector):
    def createItem(self, fieldName: str, contentType: str, isFormField: bool, fileName: str) -> FileItem:
        pass


    javaClz = java.type("org.apache.commons.fileupload.FileItemFactory")
    def __getattr__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            pass
        return JavaHandler.mapping(getattr(self.javaClz, StaticFieldRedirector.unmangle_name(name)))