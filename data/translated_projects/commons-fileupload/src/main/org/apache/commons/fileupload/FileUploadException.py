from __future__ import annotations
from io import StringIO
import io
import typing
from typing import *
import java # type: ignore
from src.main.org.apache.commons.fileupload.java_handler import *
class FileUploadException(Exception, metaclass=StaticFieldRedirector):
    def getCause(self) -> BaseException:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.getCause(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
    def printStackTrace1(self, writer: typing.Union[io.TextIOWrapper, io.StringIO]) -> None:

        idMapPyToJ = self.javaObj.pyToJ()
        translatedArg0 = JavaHandler.valueToObject(writer, "PrintWriter", idMapPyToJ)
        idMapJToPy = dict()
        try:
            self.javaObj.printStackTrace1(translatedArg0)
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            JavaHandler.mapping(translatedArg0, idMapJToPy, writer)
    def printStackTrace0(self, stream: typing.IO) -> None:

        idMapPyToJ = self.javaObj.pyToJ()
        translatedArg0 = JavaHandler.valueToObject(stream, "PrintStream", idMapPyToJ)
        idMapJToPy = dict()
        try:
            self.javaObj.printStackTrace0(translatedArg0)
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            JavaHandler.mapping(translatedArg0, idMapJToPy, stream)
    def __init__(self, msg: str, cause: BaseException) -> None:

        idMapPyToJ = JavaHandler.valueToObject(dict(), "Map")
        translatedArg0 = JavaHandler.valueToObject(msg, "String", idMapPyToJ)
        translatedArg1 = JavaHandler.valueToObject(cause, "Throwable", idMapPyToJ)
        idMapJToPy = dict()
        try:
            self.javaObj = FileUploadException.javaClz(translatedArg0, translatedArg1)
            self.javaObj.setPythonObject(self)
            self.javaObj.jToPy(idMapJToPy)
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            JavaHandler.mapping(translatedArg0, idMapJToPy, msg)
            JavaHandler.mapping(translatedArg1, idMapJToPy, cause)
    @staticmethod

    def FileUploadException1(msg: str) -> FileUploadException:

        idMapPyToJ = JavaHandler.valueToObject(dict(), "Map")
        translatedArg0 = JavaHandler.valueToObject(msg, "String", idMapPyToJ)
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(FileUploadException.javaClz.FileUploadException1(translatedArg0), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass

            JavaHandler.mapping(translatedArg0, idMapJToPy, msg)
    @staticmethod

    def FileUploadException0() -> FileUploadException:

        idMapPyToJ = JavaHandler.valueToObject(dict(), "Map")
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(FileUploadException.javaClz.FileUploadException0(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass

            
    javaClz = java.type("org.apache.commons.fileupload.FileUploadException")
    def __getattr__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            pass
        return JavaHandler.mapping(getattr(self.javaClz, StaticFieldRedirector.unmangle_name(name)))