from __future__ import annotations
from abc import ABC
import io
from src.main.org.apache.commons.fileupload.RequestContext import *
import java # type: ignore
from src.main.org.apache.commons.fileupload.java_handler import *
class UploadContext(ABC, metaclass=StaticFieldRedirector):
    def contentLength(self) -> int:
        pass


    javaClz = java.type("org.apache.commons.fileupload.UploadContext")
    def __getattr__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            pass
        return JavaHandler.mapping(getattr(self.javaClz, StaticFieldRedirector.unmangle_name(name)))