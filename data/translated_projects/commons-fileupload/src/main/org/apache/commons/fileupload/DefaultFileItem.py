from __future__ import annotations
import pathlib
import io
import typing
from typing import *
import os
from src.main.org.apache.commons.fileupload.disk.DiskFileItem import *
import java # type: ignore
from src.main.org.apache.commons.fileupload.java_handler import *
class DefaultFileItem(DiskFileItem, metaclass=StaticFieldRedirector):
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
            self.javaObj = DefaultFileItem.javaClz(translatedArg0, translatedArg1, translatedArg2, translatedArg3, translatedArg4, translatedArg5)
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
    javaClz = java.type("org.apache.commons.fileupload.DefaultFileItem")
    def __getattr__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            pass
        return JavaHandler.mapping(getattr(self.javaClz, StaticFieldRedirector.unmangle_name(name)))