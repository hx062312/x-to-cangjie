from __future__ import annotations
import unittest
import pathlib
from io import StringIO
import io
from io import BytesIO
import typing
from typing import *
from src.main.org.apache.commons.fileupload.FileUploadBase import *
import java # type: ignore
from src.main.org.apache.commons.fileupload.java_handler import *
class MockPortletActionRequest(metaclass=StaticFieldRedirector):
    def setCharacterEncoding(self, characterEncoding: str) -> None:

        idMapPyToJ = self.javaObj.pyToJ()
        translatedArg0 = JavaHandler.valueToObject(characterEncoding, "String", idMapPyToJ)
        idMapJToPy = dict()
        try:
            self.javaObj.setCharacterEncoding(translatedArg0)
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            JavaHandler.mapping(translatedArg0, idMapJToPy, characterEncoding)
    def getReader(self) -> io.BufferedReader:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.getReader(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
    def getPortletInputStream(self) -> typing.Union[io.BytesIO, io.StringIO, io.BufferedReader]:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.getPortletInputStream(), id_map=idMapJToPy)
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
            
    def getContentLength(self) -> int:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.getContentLength(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
    def getCharacterEncoding(self) -> str:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.getCharacterEncoding(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
    def setAttribute(self, key: str, value: typing.Any) -> None:

        idMapPyToJ = self.javaObj.pyToJ()
        translatedArg0 = JavaHandler.valueToObject(key, "String", idMapPyToJ)
        translatedArg1 = JavaHandler.valueToObject(value, "Object", idMapPyToJ)
        idMapJToPy = dict()
        try:
            self.javaObj.setAttribute(translatedArg0, translatedArg1)
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            JavaHandler.mapping(translatedArg0, idMapJToPy, key)
            JavaHandler.mapping(translatedArg1, idMapJToPy, value)
    def removeAttribute(self, key: str) -> None:

        idMapPyToJ = self.javaObj.pyToJ()
        translatedArg0 = JavaHandler.valueToObject(key, "String", idMapPyToJ)
        idMapJToPy = dict()
        try:
            self.javaObj.removeAttribute(translatedArg0)
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            JavaHandler.mapping(translatedArg0, idMapJToPy, key)
    def isUserInRole(self, arg0: str) -> bool:

        idMapPyToJ = self.javaObj.pyToJ()
        translatedArg0 = JavaHandler.valueToObject(arg0, "String", idMapPyToJ)
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.isUserInRole(translatedArg0), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            JavaHandler.mapping(translatedArg0, idMapJToPy, arg0)
    def isSecure(self) -> bool:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.isSecure(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
    def isRequestedSessionIdValid(self) -> bool:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.isRequestedSessionIdValid(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
    def getServerPort(self) -> int:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.getServerPort(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
    def getServerName(self) -> str:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.getServerName(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
    def getScheme(self) -> str:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.getScheme(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
    def getResponseContentTypes(self) -> typing.Union[typing.Iterator[typing.Any], typing.Generator[typing.Any, typing.Any, typing.Any]]:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.getResponseContentTypes(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
    def getResponseContentType(self) -> str:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.getResponseContentType(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
    def getRequestedSessionId(self) -> str:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.getRequestedSessionId(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
    def getRemoteUser(self) -> str:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.getRemoteUser(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
    def getPropertyNames(self) -> typing.Union[typing.Iterator[typing.Any], typing.Generator[typing.Any, typing.Any, typing.Any]]:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.getPropertyNames(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
    def getProperty(self, arg0: str) -> str:

        idMapPyToJ = self.javaObj.pyToJ()
        translatedArg0 = JavaHandler.valueToObject(arg0, "String", idMapPyToJ)
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.getProperty(translatedArg0), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            JavaHandler.mapping(translatedArg0, idMapJToPy, arg0)
    def getProperties(self, arg0: str) -> typing.Union[typing.Iterator[typing.Any], typing.Generator[typing.Any, typing.Any, typing.Any]]:

        idMapPyToJ = self.javaObj.pyToJ()
        translatedArg0 = JavaHandler.valueToObject(arg0, "String", idMapPyToJ)
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.getProperties(translatedArg0), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            JavaHandler.mapping(translatedArg0, idMapJToPy, arg0)
    def getParameterValues(self, arg0: str) -> typing.List[typing.List[str]]:

        idMapPyToJ = self.javaObj.pyToJ()
        translatedArg0 = JavaHandler.valueToObject(arg0, "String", idMapPyToJ)
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.getParameterValues(translatedArg0), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            JavaHandler.mapping(translatedArg0, idMapJToPy, arg0)
    def getParameterNames(self) -> typing.Union[typing.Iterator[typing.Any], typing.Generator[typing.Any, typing.Any, typing.Any]]:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.getParameterNames(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
    def getParameterMap(self) -> typing.Dict[typing.Any, typing.Any]:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.getParameterMap(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
    def getParameter(self, key: str) -> str:

        idMapPyToJ = self.javaObj.pyToJ()
        translatedArg0 = JavaHandler.valueToObject(key, "String", idMapPyToJ)
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.getParameter(translatedArg0), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            JavaHandler.mapping(translatedArg0, idMapJToPy, key)
    def getLocales(self) -> typing.Union[typing.Iterator[typing.Any], typing.Generator[typing.Any, typing.Any, typing.Any]]:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.getLocales(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
    def getLocale(self) -> typing.Any:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.getLocale(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
    def getContextPath(self) -> str:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.getContextPath(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
    def getAuthType(self) -> str:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.getAuthType(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
    def getAttributeNames(self) -> typing.Union[typing.Iterator[typing.Any], typing.Generator[typing.Any, typing.Any, typing.Any]]:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.getAttributeNames(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
    def getAttribute(self, key: str) -> typing.Any:

        idMapPyToJ = self.javaObj.pyToJ()
        translatedArg0 = JavaHandler.valueToObject(key, "String", idMapPyToJ)
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.getAttribute(translatedArg0), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            JavaHandler.mapping(translatedArg0, idMapJToPy, key)
    @staticmethod

    def MockPortletActionRequest1(requestData: typing.List[int], contentType: str) -> MockPortletActionRequest:

        idMapPyToJ = JavaHandler.valueToObject(dict(), "Map")
        translatedArg0 = requestData
        translatedArg1 = JavaHandler.valueToObject(contentType, "String", idMapPyToJ)
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(MockPortletActionRequest.javaClz.MockPortletActionRequest1(translatedArg0, translatedArg1), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass

            JavaHandler.mapping(translatedArg0, idMapJToPy, requestData)
            JavaHandler.mapping(translatedArg1, idMapJToPy, contentType)
    def __init__(self, requestLength: int, byteArrayInputStream: typing.Union[io.BytesIO, bytearray], contentType: str) -> None:

        idMapPyToJ = JavaHandler.valueToObject(dict(), "Map")
        translatedArg0 = JavaHandler.valueToObject(requestLength, "int", idMapPyToJ)
        translatedArg1 = JavaHandler.valueToObject(byteArrayInputStream, "ByteArrayInputStream", idMapPyToJ)
        translatedArg2 = JavaHandler.valueToObject(contentType, "String", idMapPyToJ)
        idMapJToPy = dict()
        try:
            self.javaObj = MockPortletActionRequest.javaClz(translatedArg0, translatedArg1, translatedArg2)
            self.javaObj.setPythonObject(self)
            self.javaObj.jToPy(idMapJToPy)
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            JavaHandler.mapping(translatedArg0, idMapJToPy, requestLength)
            JavaHandler.mapping(translatedArg1, idMapJToPy, byteArrayInputStream)
            JavaHandler.mapping(translatedArg2, idMapJToPy, contentType)
    javaClz = java.type("org.apache.commons.fileupload.portlet.MockPortletActionRequest")
    def __getattr__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            pass
        return JavaHandler.mapping(getattr(self.javaClz, StaticFieldRedirector.unmangle_name(name)))