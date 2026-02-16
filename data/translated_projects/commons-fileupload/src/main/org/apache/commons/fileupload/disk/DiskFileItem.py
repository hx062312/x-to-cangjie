from __future__ import annotations
import pathlib
import io
import typing
from typing import *
import os
from src.main.org.apache.commons.fileupload.FileItemHeaders import *
from src.main.org.apache.commons.fileupload.ParameterParser import *
from src.main.org.apache.commons.fileupload.util.Streams import *
import java # type: ignore
from src.main.org.apache.commons.fileupload.java_handler import *
class DiskFileItem(metaclass=StaticFieldRedirector):
    def setDefaultCharset(self, charset: str) -> None:

        idMapPyToJ = self.javaObj.pyToJ()
        translatedArg0 = JavaHandler.valueToObject(charset, "String", idMapPyToJ)
        idMapJToPy = dict()
        try:
            self.javaObj.setDefaultCharset(translatedArg0)
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            JavaHandler.mapping(translatedArg0, idMapJToPy, charset)
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
            
    def setHeaders(self, pHeaders: FileItemHeaders) -> None:

        idMapPyToJ = self.javaObj.pyToJ()
        translatedArg0 = JavaHandler.valueToObject(pHeaders, "FileItemHeaders", idMapPyToJ)
        idMapJToPy = dict()
        try:
            self.javaObj.setHeaders(translatedArg0)
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            JavaHandler.mapping(translatedArg0, idMapJToPy, pHeaders)
    def getHeaders(self) -> FileItemHeaders:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.getHeaders(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
    def _getTempFile(self) -> pathlib.Path:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.getTempFile(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
    def setFormField(self, state: bool) -> None:

        idMapPyToJ = self.javaObj.pyToJ()
        translatedArg0 = JavaHandler.valueToObject(state, "boolean", idMapPyToJ)
        idMapJToPy = dict()
        try:
            self.javaObj.setFormField(translatedArg0)
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            JavaHandler.mapping(translatedArg0, idMapJToPy, state)
    def isFormField(self) -> bool:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.isFormField(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
    def setFieldName(self, fieldName: str) -> None:

        idMapPyToJ = self.javaObj.pyToJ()
        translatedArg0 = JavaHandler.valueToObject(fieldName, "String", idMapPyToJ)
        idMapJToPy = dict()
        try:
            self.javaObj.setFieldName(translatedArg0)
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            JavaHandler.mapping(translatedArg0, idMapJToPy, fieldName)
    def getFieldName(self) -> str:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.getFieldName(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
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
            
    def getCharSet(self) -> str:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.getCharSet(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
    def getContentType(self) -> str:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.getContentType(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
    def __init__(self, fieldName: str, contentType: str, isFormField: bool, fileName: str, sizeThreshold: int, repository: pathlib.Path) -> None:

        idMapPyToJ = JavaHandler.valueToObject(dict(), "Map")
        translatedArg0 = JavaHandler.valueToObject(fieldName, "String", idMapPyToJ)
        translatedArg1 = JavaHandler.valueToObject(contentType, "String", idMapPyToJ)
        translatedArg2 = JavaHandler.valueToObject(isFormField, "boolean", idMapPyToJ)
        translatedArg3 = JavaHandler.valueToObject(fileName, "String", idMapPyToJ)
        translatedArg4 = JavaHandler.valueToObject(sizeThreshold, "int", idMapPyToJ)
        translatedArg5 = JavaHandler.valueToObject(repository, "File", idMapPyToJ)
        idMapJToPy = dict()
        try:
            self.javaObj = DiskFileItem.javaClz(translatedArg0, translatedArg1, translatedArg2, translatedArg3, translatedArg4, translatedArg5)
            self.javaObj.setPythonObject(self)
            self.javaObj.jToPy(idMapJToPy)
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            JavaHandler.mapping(translatedArg0, idMapJToPy, fieldName)
            JavaHandler.mapping(translatedArg1, idMapJToPy, contentType)
            JavaHandler.mapping(translatedArg2, idMapJToPy, isFormField)
            JavaHandler.mapping(translatedArg3, idMapJToPy, fileName)
            JavaHandler.mapping(translatedArg4, idMapJToPy, sizeThreshold)
            JavaHandler.mapping(translatedArg5, idMapJToPy, repository)
    @staticmethod

    def __getUniqueId() -> str:

        idMapPyToJ = JavaHandler.valueToObject(dict(), "Map")
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(DiskFileItem.javaClz.getUniqueId(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass

            
    javaClz = java.type("org.apache.commons.fileupload.disk.DiskFileItem")
    def __getattr__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            pass
        return JavaHandler.mapping(getattr(self.javaClz, StaticFieldRedirector.unmangle_name(name)))