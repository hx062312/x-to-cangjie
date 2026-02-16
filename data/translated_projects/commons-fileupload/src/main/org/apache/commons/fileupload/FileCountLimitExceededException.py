from __future__ import annotations
import io
from src.main.org.apache.commons.fileupload.FileUploadException import *
import java # type: ignore
from src.main.org.apache.commons.fileupload.java_handler import *
class FileCountLimitExceededException(FileUploadException, metaclass=StaticFieldRedirector):
    def getLimit(self) -> int:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.getLimit(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
    def __init__(self, message: str, limit: int) -> None:

        idMapPyToJ = JavaHandler.valueToObject(dict(), "Map")
        translatedArg0 = JavaHandler.valueToObject(message, "String", idMapPyToJ)
        translatedArg1 = JavaHandler.valueToObject(limit, "long", idMapPyToJ)
        idMapJToPy = dict()
        try:
            self.javaObj = FileCountLimitExceededException.javaClz(translatedArg0, translatedArg1)
            self.javaObj.setPythonObject(self)
            self.javaObj.jToPy(idMapJToPy)
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            JavaHandler.mapping(translatedArg0, idMapJToPy, message)
            JavaHandler.mapping(translatedArg1, idMapJToPy, limit)
    javaClz = java.type("org.apache.commons.fileupload.FileCountLimitExceededException")
    def __getattr__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            pass
        return JavaHandler.mapping(getattr(self.javaClz, StaticFieldRedirector.unmangle_name(name)))