from __future__ import annotations
import io
from src.main.org.apache.commons.fileupload.FileItemFactory import *
from src.main.org.apache.commons.fileupload.FileUpload import *
import java # type: ignore
from src.main.org.apache.commons.fileupload.java_handler import *
class PortletFileUpload(FileUpload, metaclass=StaticFieldRedirector):
    @staticmethod

    def PortletFileUpload1() -> PortletFileUpload:

        idMapPyToJ = JavaHandler.valueToObject(dict(), "Map")
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(PortletFileUpload.javaClz.PortletFileUpload1(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass

            
    def __init__(self, fileItemFactory: FileItemFactory) -> None:

        idMapPyToJ = JavaHandler.valueToObject(dict(), "Map")
        translatedArg0 = JavaHandler.valueToObject(fileItemFactory, "FileItemFactory", idMapPyToJ)
        idMapJToPy = dict()
        try:
            self.javaObj = PortletFileUpload.javaClz(translatedArg0)
            self.javaObj.setPythonObject(self)
            self.javaObj.jToPy(idMapJToPy)
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            JavaHandler.mapping(translatedArg0, idMapJToPy, fileItemFactory)
    javaClz = java.type("org.apache.commons.fileupload.portlet.PortletFileUpload")
    def __getattr__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            pass
        return JavaHandler.mapping(getattr(self.javaClz, StaticFieldRedirector.unmangle_name(name)))