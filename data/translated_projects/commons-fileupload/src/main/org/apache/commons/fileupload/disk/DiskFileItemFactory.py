from __future__ import annotations
import pathlib
import io
import os
from src.main.org.apache.commons.fileupload.disk.DiskFileItem import *
import java # type: ignore
from src.main.org.apache.commons.fileupload.java_handler import *
class DiskFileItemFactory(metaclass=StaticFieldRedirector):
    def setDefaultCharset(self, pCharset: str) -> None:

        idMapPyToJ = self.javaObj.pyToJ()
        translatedArg0 = JavaHandler.valueToObject(pCharset, "String", idMapPyToJ)
        idMapJToPy = dict()
        try:
            self.javaObj.setDefaultCharset(translatedArg0)
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            JavaHandler.mapping(translatedArg0, idMapJToPy, pCharset)
    def getDefaultCharset(self) -> str:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.getDefaultCharset(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
    def setSizeThreshold(self, sizeThreshold: int) -> None:

        idMapPyToJ = self.javaObj.pyToJ()
        translatedArg0 = JavaHandler.valueToObject(sizeThreshold, "int", idMapPyToJ)
        idMapJToPy = dict()
        try:
            self.javaObj.setSizeThreshold(translatedArg0)
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            JavaHandler.mapping(translatedArg0, idMapJToPy, sizeThreshold)
    def getSizeThreshold(self) -> int:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.getSizeThreshold(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
    def setRepository(self, repository: pathlib.Path) -> None:

        idMapPyToJ = self.javaObj.pyToJ()
        translatedArg0 = JavaHandler.valueToObject(repository, "File", idMapPyToJ)
        idMapJToPy = dict()
        try:
            self.javaObj.setRepository(translatedArg0)
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            JavaHandler.mapping(translatedArg0, idMapJToPy, repository)
    def getRepository(self) -> pathlib.Path:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.getRepository(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
    @staticmethod

    def DiskFileItemFactory1() -> DiskFileItemFactory:

        idMapPyToJ = JavaHandler.valueToObject(dict(), "Map")
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(DiskFileItemFactory.javaClz.DiskFileItemFactory1(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass

            
    def __init__(self, sizeThreshold: int, repository: pathlib.Path) -> None:

        idMapPyToJ = JavaHandler.valueToObject(dict(), "Map")
        translatedArg0 = JavaHandler.valueToObject(sizeThreshold, "int", idMapPyToJ)
        translatedArg1 = JavaHandler.valueToObject(repository, "File", idMapPyToJ)
        idMapJToPy = dict()
        try:
            self.javaObj = DiskFileItemFactory.javaClz(translatedArg0, translatedArg1)
            self.javaObj.setPythonObject(self)
            self.javaObj.jToPy(idMapJToPy)
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            JavaHandler.mapping(translatedArg0, idMapJToPy, sizeThreshold)
            JavaHandler.mapping(translatedArg1, idMapJToPy, repository)
    javaClz = java.type("org.apache.commons.fileupload.disk.DiskFileItemFactory")
    def __getattr__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            pass
        return JavaHandler.mapping(getattr(self.javaClz, StaticFieldRedirector.unmangle_name(name)))