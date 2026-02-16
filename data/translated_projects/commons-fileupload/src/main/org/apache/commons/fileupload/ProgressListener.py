from __future__ import annotations
from abc import ABC
import io
import typing
from typing import *
import java # type: ignore
from src.main.org.apache.commons.fileupload.java_handler import *
class ProgressListener(ABC, metaclass=StaticFieldRedirector):
    def update(self, pBytesRead: int, pContentLength: int, pItems: int) -> None:
        pass


    javaClz = java.type("org.apache.commons.fileupload.ProgressListener")
    def __getattr__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            pass
        return JavaHandler.mapping(getattr(self.javaClz, StaticFieldRedirector.unmangle_name(name)))