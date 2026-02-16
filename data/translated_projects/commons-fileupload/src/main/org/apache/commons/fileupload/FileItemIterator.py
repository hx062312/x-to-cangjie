from __future__ import annotations
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.fileupload.FileItemStream import *
from src.main.org.apache.commons.fileupload.FileUploadException import *
import java # type: ignore
from src.main.org.apache.commons.fileupload.java_handler import *
class FileItemIterator(ABC, metaclass=StaticFieldRedirector):
    def next_(self) -> FileItemStream:
        pass


    def hasNext(self) -> bool:
        pass


    javaClz = java.type("org.apache.commons.fileupload.FileItemIterator")
    def __getattr__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            pass
        return JavaHandler.mapping(getattr(self.javaClz, StaticFieldRedirector.unmangle_name(name)))