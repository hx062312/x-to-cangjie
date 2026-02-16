from __future__ import annotations
import io
import java # type: ignore
from src.main.org.apache.commons.fileupload.java_handler import *
class InvalidFileNameException(RuntimeError, metaclass=StaticFieldRedirector):
    def getName(self) -> str:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.getName(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
    def __init__(self, pName: str, pMessage: str) -> None:

        idMapPyToJ = JavaHandler.valueToObject(dict(), "Map")
        translatedArg0 = JavaHandler.valueToObject(pName, "String", idMapPyToJ)
        translatedArg1 = JavaHandler.valueToObject(pMessage, "String", idMapPyToJ)
        idMapJToPy = dict()
        try:
            self.javaObj = InvalidFileNameException.javaClz(translatedArg0, translatedArg1)
            self.javaObj.setPythonObject(self)
            self.javaObj.jToPy(idMapJToPy)
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            JavaHandler.mapping(translatedArg0, idMapJToPy, pName)
            JavaHandler.mapping(translatedArg1, idMapJToPy, pMessage)
    javaClz = java.type("org.apache.commons.fileupload.InvalidFileNameException")
    def __getattr__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            pass
        return JavaHandler.mapping(getattr(self.javaClz, StaticFieldRedirector.unmangle_name(name)))