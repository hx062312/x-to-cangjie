from __future__ import annotations
import io
from src.main.org.apache.commons.fileupload.FileItemFactory import *
from src.main.org.apache.commons.fileupload.FileUploadBase import *
import java # type: ignore
from src.main.org.apache.commons.fileupload.java_handler import *
class FileUpload(FileUploadBase, metaclass=StaticFieldRedirector):
    def setFileItemFactory(self, factory: FileItemFactory) -> None:

        idMapPyToJ = self.javaObj.pyToJ()
        translatedArg0 = JavaHandler.valueToObject(factory, "FileItemFactory", idMapPyToJ)
        idMapJToPy = dict()
        try:
            self.javaObj.setFileItemFactory(translatedArg0)
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            JavaHandler.mapping(translatedArg0, idMapJToPy, factory)
    def getFileItemFactory(self) -> FileItemFactory:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.getFileItemFactory(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
    def __init__(self, constructorId: int, fileItemFactory: FileItemFactory) -> None:

        idMapPyToJ = JavaHandler.valueToObject(dict(), "Map")
        translatedArg0 = JavaHandler.valueToObject(constructorId, "int", idMapPyToJ)
        translatedArg1 = JavaHandler.valueToObject(fileItemFactory, "FileItemFactory", idMapPyToJ)
        idMapJToPy = dict()
        try:
            self.javaObj = FileUpload.javaClz(translatedArg0, translatedArg1)
            self.javaObj.setPythonObject(self)
            self.javaObj.jToPy(idMapJToPy)
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            JavaHandler.mapping(translatedArg0, idMapJToPy, constructorId)
            JavaHandler.mapping(translatedArg1, idMapJToPy, fileItemFactory)
    javaClz = java.type("org.apache.commons.fileupload.FileUpload")
    def __getattr__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            pass
        return JavaHandler.mapping(getattr(self.javaClz, StaticFieldRedirector.unmangle_name(name)))