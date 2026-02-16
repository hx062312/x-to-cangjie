from __future__ import annotations
import pathlib
import io
import os
from src.main.org.apache.commons.fileupload.disk.DiskFileItemFactory import *
import java # type: ignore
from src.main.org.apache.commons.fileupload.java_handler import *
class DefaultFileItemFactory(DiskFileItemFactory, metaclass=StaticFieldRedirector):
    def __init__(self, sizeThreshold: int, repository: pathlib.Path) -> None:

        idMapPyToJ = JavaHandler.valueToObject(dict(), "Map")
        translatedArg0 = JavaHandler.valueToObject(sizeThreshold, "int", idMapPyToJ)
        translatedArg1 = JavaHandler.valueToObject(repository, "File", idMapPyToJ)
        idMapJToPy = dict()
        try:
            self.javaObj = DefaultFileItemFactory.javaClz(translatedArg0, translatedArg1)
            self.javaObj.setPythonObject(self)
            self.javaObj.jToPy(idMapJToPy)
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            JavaHandler.mapping(translatedArg0, idMapJToPy, sizeThreshold)
            JavaHandler.mapping(translatedArg1, idMapJToPy, repository)
    @staticmethod

    def DefaultFileItemFactory1() -> DefaultFileItemFactory:

        idMapPyToJ = JavaHandler.valueToObject(dict(), "Map")
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(DefaultFileItemFactory.javaClz.DefaultFileItemFactory1(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass

            
    javaClz = java.type("org.apache.commons.fileupload.DefaultFileItemFactory")
    def __getattr__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            pass
        return JavaHandler.mapping(getattr(self.javaClz, StaticFieldRedirector.unmangle_name(name)))