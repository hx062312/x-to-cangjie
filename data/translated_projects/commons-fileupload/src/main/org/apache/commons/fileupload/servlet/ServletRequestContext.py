from __future__ import annotations
import io
import java # type: ignore
from src.main.org.apache.commons.fileupload.java_handler import *
class ServletRequestContext(metaclass=StaticFieldRedirector):
    javaClz = java.type("org.apache.commons.fileupload.servlet.ServletRequestContext")
    def __getattr__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            pass
        return JavaHandler.mapping(getattr(self.javaClz, StaticFieldRedirector.unmangle_name(name)))