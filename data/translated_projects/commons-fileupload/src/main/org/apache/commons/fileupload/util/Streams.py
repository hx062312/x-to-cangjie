from __future__ import annotations
import io
from src.main.org.apache.commons.fileupload.InvalidFileNameException import *
import java # type: ignore
from src.main.org.apache.commons.fileupload.java_handler import *
class Streams(metaclass=StaticFieldRedirector):
    @staticmethod

    def checkFileName(fileName: str) -> str:

        idMapPyToJ = JavaHandler.valueToObject(dict(), "Map")
        translatedArg0 = JavaHandler.valueToObject(fileName, "String", idMapPyToJ)
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(Streams.javaClz.checkFileName(translatedArg0), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass

            JavaHandler.mapping(translatedArg0, idMapJToPy, fileName)
    def __init__(self) -> None:

        idMapPyToJ = JavaHandler.valueToObject(dict(), "Map")
        
        idMapJToPy = dict()
        try:
            self.javaObj = Streams.javaClz()
            self.javaObj.setPythonObject(self)
            self.javaObj.jToPy(idMapJToPy)
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            
    javaClz = java.type("org.apache.commons.fileupload.util.Streams")
    def __getattr__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            pass
        return JavaHandler.mapping(getattr(self.javaClz, StaticFieldRedirector.unmangle_name(name)))