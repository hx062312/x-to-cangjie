from __future__ import annotations
import unittest
import io
import java # type: ignore
from src.main.org.apache.commons.fileupload.java_handler import *
class Constants(metaclass=StaticFieldRedirector):
    def __init__(self) -> None:

        idMapPyToJ = JavaHandler.valueToObject(dict(), "Map")
        
        idMapJToPy = dict()
        try:
            self.javaObj = Constants.javaClz()
            self.javaObj.setPythonObject(self)
            self.javaObj.jToPy(idMapJToPy)
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            
    javaClz = java.type("org.apache.commons.fileupload.Constants")
    def __getattr__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            pass
        return JavaHandler.mapping(getattr(self.javaClz, StaticFieldRedirector.unmangle_name(name)))