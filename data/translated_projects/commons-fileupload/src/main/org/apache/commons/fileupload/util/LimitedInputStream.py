from __future__ import annotations
from abc import ABC
from io import StringIO
import io
from io import BytesIO
import typing
from typing import *
import os
from src.main.org.apache.commons.fileupload.util.Closeable import *
import java # type: ignore
from src.main.org.apache.commons.fileupload.java_handler import *
class LimitedInputStream(ABC, metaclass=StaticFieldRedirector):
    def close(self) -> None:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            self.javaObj.close()
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
    def isClosed(self) -> bool:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.isClosed(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
    def read1(self, b: typing.List[int], off: int, len_: int) -> int:

        idMapPyToJ = self.javaObj.pyToJ()
        translatedArg0 = b
        translatedArg1 = JavaHandler.valueToObject(off, "int", idMapPyToJ)
        translatedArg2 = JavaHandler.valueToObject(len_, "int", idMapPyToJ)
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.read1(translatedArg0, translatedArg1, translatedArg2), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            JavaHandler.mapping(translatedArg0, idMapJToPy, b)
            JavaHandler.mapping(translatedArg1, idMapJToPy, off)
            JavaHandler.mapping(translatedArg2, idMapJToPy, len_)
    def read0(self) -> int:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.read0(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
    def __init__(self, inputStream: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader], pSizeMax: int) -> None:

        idMapPyToJ = JavaHandler.valueToObject(dict(), "Map")
        translatedArg0 = JavaHandler.valueToObject(inputStream, "InputStream", idMapPyToJ)
        translatedArg1 = JavaHandler.valueToObject(pSizeMax, "long", idMapPyToJ)
        idMapJToPy = dict()
        try:
            self.javaObj = LimitedInputStream.javaClz(translatedArg0, translatedArg1)
            self.javaObj.setPythonObject(self)
            self.javaObj.jToPy(idMapJToPy)
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            JavaHandler.mapping(translatedArg0, idMapJToPy, inputStream)
            JavaHandler.mapping(translatedArg1, idMapJToPy, pSizeMax)
    def __checkLimit(self) -> None:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            self.javaObj.checkLimit()
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
    def _raiseError(self, pSizeMax: int, pCount: int) -> None:
        pass


    javaClz = java.type("org.apache.commons.fileupload.util.LimitedInputStream")
    def __getattr__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            pass
        return JavaHandler.mapping(getattr(self.javaClz, StaticFieldRedirector.unmangle_name(name)))