from __future__ import annotations
import io
import java # type: ignore
from src.main.org.apache.commons.fileupload.java_handler import *
class ParseException(Exception, metaclass=StaticFieldRedirector):
    def __init__(self, message: str) -> None:

        idMapPyToJ = JavaHandler.valueToObject(dict(), "Map")
        translatedArg0 = JavaHandler.valueToObject(message, "String", idMapPyToJ)
        idMapJToPy = dict()
        try:
            self.javaObj = ParseException.javaClz(translatedArg0)
            self.javaObj.setPythonObject(self)
            self.javaObj.jToPy(idMapJToPy)
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            JavaHandler.mapping(translatedArg0, idMapJToPy, message)
    javaClz = java.type("org.apache.commons.fileupload.util.mime.ParseException")
    def __getattr__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            pass
        return JavaHandler.mapping(getattr(self.javaClz, StaticFieldRedirector.unmangle_name(name)))