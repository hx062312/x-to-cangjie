from __future__ import annotations
import io
import typing
from typing import *
from src.main.org.apache.commons.fileupload.FileItemHeaders import *
import java # type: ignore
from src.main.org.apache.commons.fileupload.java_handler import *
class FileItemHeadersImpl(FileItemHeaders, metaclass=StaticFieldRedirector):
    def getHeaders(self, name: str) -> typing.Iterator[str]:

        idMapPyToJ = self.javaObj.pyToJ()
        translatedArg0 = JavaHandler.valueToObject(name, "String", idMapPyToJ)
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.getHeaders(translatedArg0), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            JavaHandler.mapping(translatedArg0, idMapJToPy, name)
    def getHeaderNames(self) -> typing.Iterator[str]:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.getHeaderNames(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
    def getHeader(self, name: str) -> str:

        idMapPyToJ = self.javaObj.pyToJ()
        translatedArg0 = JavaHandler.valueToObject(name, "String", idMapPyToJ)
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.getHeader(translatedArg0), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            JavaHandler.mapping(translatedArg0, idMapJToPy, name)
    def addHeader(self, name: str, value: str) -> None:

        idMapPyToJ = self.javaObj.pyToJ()
        translatedArg0 = JavaHandler.valueToObject(name, "String", idMapPyToJ)
        translatedArg1 = JavaHandler.valueToObject(value, "String", idMapPyToJ)
        idMapJToPy = dict()
        try:
            self.javaObj.addHeader(translatedArg0, translatedArg1)
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            JavaHandler.mapping(translatedArg0, idMapJToPy, name)
            JavaHandler.mapping(translatedArg1, idMapJToPy, value)
    javaClz = java.type("org.apache.commons.fileupload.util.FileItemHeadersImpl")
    def __getattr__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            pass
        return JavaHandler.mapping(getattr(self.javaClz, StaticFieldRedirector.unmangle_name(name)))