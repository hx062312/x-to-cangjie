from __future__ import annotations
from abc import ABC
import io
import os
import java # type: ignore
from src.main.org.apache.commons.fileupload.java_handler import *
class Closeable(ABC, metaclass=StaticFieldRedirector):
    def isClosed(self) -> bool:
        pass


    def close(self) -> None:
        pass


    javaClz = java.type("org.apache.commons.fileupload.util.Closeable")
    def __getattr__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            pass
        return JavaHandler.mapping(getattr(self.javaClz, StaticFieldRedirector.unmangle_name(name)))