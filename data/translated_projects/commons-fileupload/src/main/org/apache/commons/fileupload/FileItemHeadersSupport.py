from __future__ import annotations
from abc import ABC
import io
from src.main.org.apache.commons.fileupload.FileItemHeaders import *
import java # type: ignore
from src.main.org.apache.commons.fileupload.java_handler import *
class FileItemHeadersSupport(ABC, metaclass=StaticFieldRedirector):
    def setHeaders(self, headers: FileItemHeaders) -> None:
        pass


    def getHeaders(self) -> FileItemHeaders:
        pass


    javaClz = java.type("org.apache.commons.fileupload.FileItemHeadersSupport")
    def __getattr__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            pass
        return JavaHandler.mapping(getattr(self.javaClz, StaticFieldRedirector.unmangle_name(name)))