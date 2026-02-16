from __future__ import annotations
from abc import ABC
import io
import typing
from typing import *
import os
from src.main.org.apache.commons.fileupload.FileItem import *
from src.main.org.apache.commons.fileupload.FileItemFactory import *
from src.main.org.apache.commons.fileupload.FileItemHeaders import *
from src.main.org.apache.commons.fileupload.FileUploadException import *
from src.main.org.apache.commons.fileupload.ParameterParser import *
from src.main.org.apache.commons.fileupload.ProgressListener import *
from src.main.org.apache.commons.fileupload.RequestContext import *
from src.main.org.apache.commons.fileupload.util.FileItemHeadersImpl import *
import java # type: ignore
from src.main.org.apache.commons.fileupload.java_handler import *
class FileUploadBase(ABC, metaclass=StaticFieldRedirector):
    def _getHeader(self, headers: typing.Dict[str, str], name: str) -> str:

        idMapPyToJ = self.javaObj.pyToJ()
        translatedArg0 = JavaHandler.valueToObject(headers, "Map<String,String>", idMapPyToJ)
        translatedArg1 = JavaHandler.valueToObject(name, "String", idMapPyToJ)
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.getHeader(translatedArg0, translatedArg1), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            JavaHandler.mapping(translatedArg0, idMapJToPy, headers)
            JavaHandler.mapping(translatedArg1, idMapJToPy, name)
    def _parseHeaders(self, headerPart: str) -> typing.Dict[str, str]:

        idMapPyToJ = self.javaObj.pyToJ()
        translatedArg0 = JavaHandler.valueToObject(headerPart, "String", idMapPyToJ)
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.parseHeaders(translatedArg0), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            JavaHandler.mapping(translatedArg0, idMapJToPy, headerPart)
    def _createItem(self, headers: typing.Dict[str, str], isFormField: bool) -> FileItem:

        idMapPyToJ = self.javaObj.pyToJ()
        translatedArg0 = JavaHandler.valueToObject(headers, "Map<String,String>", idMapPyToJ)
        translatedArg1 = JavaHandler.valueToObject(isFormField, "boolean", idMapPyToJ)
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.createItem(translatedArg0, translatedArg1), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            JavaHandler.mapping(translatedArg0, idMapJToPy, headers)
            JavaHandler.mapping(translatedArg1, idMapJToPy, isFormField)
    def _getFieldName2(self, headers: typing.Dict[str, str]) -> str:

        idMapPyToJ = self.javaObj.pyToJ()
        translatedArg0 = JavaHandler.valueToObject(headers, "Map<String,String>", idMapPyToJ)
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.getFieldName2(translatedArg0), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            JavaHandler.mapping(translatedArg0, idMapJToPy, headers)
    def _getFileName0(self, headers: typing.Dict[str, str]) -> str:

        idMapPyToJ = self.javaObj.pyToJ()
        translatedArg0 = JavaHandler.valueToObject(headers, "Map<String,String>", idMapPyToJ)
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.getFileName0(translatedArg0), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            JavaHandler.mapping(translatedArg0, idMapJToPy, headers)
    def setProgressListener(self, pListener: ProgressListener) -> None:

        idMapPyToJ = self.javaObj.pyToJ()
        translatedArg0 = JavaHandler.valueToObject(pListener, "ProgressListener", idMapPyToJ)
        idMapJToPy = dict()
        try:
            self.javaObj.setProgressListener(translatedArg0)
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            JavaHandler.mapping(translatedArg0, idMapJToPy, pListener)
    def getProgressListener(self) -> ProgressListener:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.getProgressListener(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
    def _newFileItemHeaders(self) -> FileItemHeadersImpl:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.newFileItemHeaders(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
    def _getParsedHeaders(self, headerPart: str) -> FileItemHeaders:

        idMapPyToJ = self.javaObj.pyToJ()
        translatedArg0 = JavaHandler.valueToObject(headerPart, "String", idMapPyToJ)
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.getParsedHeaders(translatedArg0), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            JavaHandler.mapping(translatedArg0, idMapJToPy, headerPart)
    def _getFieldName0(self, headers: FileItemHeaders) -> str:

        idMapPyToJ = self.javaObj.pyToJ()
        translatedArg0 = JavaHandler.valueToObject(headers, "FileItemHeaders", idMapPyToJ)
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.getFieldName0(translatedArg0), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            JavaHandler.mapping(translatedArg0, idMapJToPy, headers)
    def _getFileName1(self, headers: FileItemHeaders) -> str:

        idMapPyToJ = self.javaObj.pyToJ()
        translatedArg0 = JavaHandler.valueToObject(headers, "FileItemHeaders", idMapPyToJ)
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.getFileName1(translatedArg0), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            JavaHandler.mapping(translatedArg0, idMapJToPy, headers)
    def _getBoundary(self, contentType: str) -> typing.List[int]:

        idMapPyToJ = self.javaObj.pyToJ()
        translatedArg0 = JavaHandler.valueToObject(contentType, "String", idMapPyToJ)
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.getBoundary(translatedArg0), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            JavaHandler.mapping(translatedArg0, idMapJToPy, contentType)
    def setHeaderEncoding(self, encoding: str) -> None:

        idMapPyToJ = self.javaObj.pyToJ()
        translatedArg0 = JavaHandler.valueToObject(encoding, "String", idMapPyToJ)
        idMapJToPy = dict()
        try:
            self.javaObj.setHeaderEncoding(translatedArg0)
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            JavaHandler.mapping(translatedArg0, idMapJToPy, encoding)
    def getHeaderEncoding(self) -> str:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.getHeaderEncoding(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
    def setFileCountMax(self, fileCountMax: int) -> None:

        idMapPyToJ = self.javaObj.pyToJ()
        translatedArg0 = JavaHandler.valueToObject(fileCountMax, "long", idMapPyToJ)
        idMapJToPy = dict()
        try:
            self.javaObj.setFileCountMax(translatedArg0)
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            JavaHandler.mapping(translatedArg0, idMapJToPy, fileCountMax)
    def getFileCountMax(self) -> int:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.getFileCountMax(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
    def setFileSizeMax(self, fileSizeMax: int) -> None:

        idMapPyToJ = self.javaObj.pyToJ()
        translatedArg0 = JavaHandler.valueToObject(fileSizeMax, "long", idMapPyToJ)
        idMapJToPy = dict()
        try:
            self.javaObj.setFileSizeMax(translatedArg0)
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            JavaHandler.mapping(translatedArg0, idMapJToPy, fileSizeMax)
    def getFileSizeMax(self) -> int:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.getFileSizeMax(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
    def setSizeMax(self, sizeMax: int) -> None:

        idMapPyToJ = self.javaObj.pyToJ()
        translatedArg0 = JavaHandler.valueToObject(sizeMax, "long", idMapPyToJ)
        idMapJToPy = dict()
        try:
            self.javaObj.setSizeMax(translatedArg0)
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            JavaHandler.mapping(translatedArg0, idMapJToPy, sizeMax)
    def getSizeMax(self) -> int:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.getSizeMax(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
    @staticmethod

    def isMultipartContent(ctx: RequestContext) -> bool:

        idMapPyToJ = JavaHandler.valueToObject(dict(), "Map")
        translatedArg0 = JavaHandler.valueToObject(ctx, "RequestContext", idMapPyToJ)
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(FileUploadBase.javaClz.isMultipartContent(translatedArg0), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass

            JavaHandler.mapping(translatedArg0, idMapJToPy, ctx)
    def __parseHeaderLine(self, headers: FileItemHeadersImpl, header: str) -> None:

        idMapPyToJ = self.javaObj.pyToJ()
        translatedArg0 = JavaHandler.valueToObject(headers, "FileItemHeadersImpl", idMapPyToJ)
        translatedArg1 = JavaHandler.valueToObject(header, "String", idMapPyToJ)
        idMapJToPy = dict()
        try:
            self.javaObj.parseHeaderLine(translatedArg0, translatedArg1)
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            JavaHandler.mapping(translatedArg0, idMapJToPy, headers)
            JavaHandler.mapping(translatedArg1, idMapJToPy, header)
    def __parseEndOfLine(self, headerPart: str, end: int) -> int:

        idMapPyToJ = self.javaObj.pyToJ()
        translatedArg0 = JavaHandler.valueToObject(headerPart, "String", idMapPyToJ)
        translatedArg1 = JavaHandler.valueToObject(end, "int", idMapPyToJ)
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.parseEndOfLine(translatedArg0, translatedArg1), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            JavaHandler.mapping(translatedArg0, idMapJToPy, headerPart)
            JavaHandler.mapping(translatedArg1, idMapJToPy, end)
    def __getFieldName1(self, pContentDisposition: str) -> str:

        idMapPyToJ = self.javaObj.pyToJ()
        translatedArg0 = JavaHandler.valueToObject(pContentDisposition, "String", idMapPyToJ)
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.getFieldName1(translatedArg0), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            JavaHandler.mapping(translatedArg0, idMapJToPy, pContentDisposition)
    def __getFileName2(self, pContentDisposition: str) -> str:

        idMapPyToJ = self.javaObj.pyToJ()
        translatedArg0 = JavaHandler.valueToObject(pContentDisposition, "String", idMapPyToJ)
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.getFileName2(translatedArg0), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            JavaHandler.mapping(translatedArg0, idMapJToPy, pContentDisposition)
    def setFileItemFactory(self, factory: FileItemFactory) -> None:
        pass


    def getFileItemFactory(self) -> FileItemFactory:
        pass


    javaClz = java.type("org.apache.commons.fileupload.FileUploadBase")
    def __getattr__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            pass
        return JavaHandler.mapping(getattr(self.javaClz, StaticFieldRedirector.unmangle_name(name)))
class SizeException(FileUploadException, ABC, metaclass=StaticFieldRedirector):
    def getPermittedSize(self) -> int:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.getPermittedSize(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
    def getActualSize(self) -> int:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.getActualSize(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
    def __init__(self, message: str, actual: int, permitted: int) -> None:

        idMapPyToJ = JavaHandler.valueToObject(dict(), "Map")
        translatedArg0 = JavaHandler.valueToObject(message, "String", idMapPyToJ)
        translatedArg1 = JavaHandler.valueToObject(actual, "long", idMapPyToJ)
        translatedArg2 = JavaHandler.valueToObject(permitted, "long", idMapPyToJ)
        idMapJToPy = dict()
        try:
            self.javaObj = SizeException.javaClz(translatedArg0, translatedArg1, translatedArg2)
            self.javaObj.setPythonObject(self)
            self.javaObj.jToPy(idMapJToPy)
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            JavaHandler.mapping(translatedArg0, idMapJToPy, message)
            JavaHandler.mapping(translatedArg1, idMapJToPy, actual)
            JavaHandler.mapping(translatedArg2, idMapJToPy, permitted)
    javaClz = java.type("org.apache.commons.fileupload.FileUploadBase$SizeException")
    def __getattr__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            pass
        return JavaHandler.mapping(getattr(self.javaClz, StaticFieldRedirector.unmangle_name(name)))
class FileSizeLimitExceededException(SizeException, metaclass=StaticFieldRedirector):
    def setFieldName(self, pFieldName: str) -> None:

        idMapPyToJ = self.javaObj.pyToJ()
        translatedArg0 = JavaHandler.valueToObject(pFieldName, "String", idMapPyToJ)
        idMapJToPy = dict()
        try:
            self.javaObj.setFieldName(translatedArg0)
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            JavaHandler.mapping(translatedArg0, idMapJToPy, pFieldName)
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
            
    def setFileName(self, pFileName: str) -> None:

        idMapPyToJ = self.javaObj.pyToJ()
        translatedArg0 = JavaHandler.valueToObject(pFileName, "String", idMapPyToJ)
        idMapJToPy = dict()
        try:
            self.javaObj.setFileName(translatedArg0)
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            JavaHandler.mapping(translatedArg0, idMapJToPy, pFileName)
    def getFileName(self) -> str:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.getFileName(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
    def __init__(self, message: str, actual: int, permitted: int) -> None:

        idMapPyToJ = JavaHandler.valueToObject(dict(), "Map")
        translatedArg0 = JavaHandler.valueToObject(message, "String", idMapPyToJ)
        translatedArg1 = JavaHandler.valueToObject(actual, "long", idMapPyToJ)
        translatedArg2 = JavaHandler.valueToObject(permitted, "long", idMapPyToJ)
        idMapJToPy = dict()
        try:
            self.javaObj = FileSizeLimitExceededException.javaClz(translatedArg0, translatedArg1, translatedArg2)
            self.javaObj.setPythonObject(self)
            self.javaObj.jToPy(idMapJToPy)
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            JavaHandler.mapping(translatedArg0, idMapJToPy, message)
            JavaHandler.mapping(translatedArg1, idMapJToPy, actual)
            JavaHandler.mapping(translatedArg2, idMapJToPy, permitted)
    javaClz = java.type("org.apache.commons.fileupload.FileUploadBase$FileSizeLimitExceededException")
    def __getattr__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            pass
        return JavaHandler.mapping(getattr(self.javaClz, StaticFieldRedirector.unmangle_name(name)))
class InvalidContentTypeException(FileUploadException, metaclass=StaticFieldRedirector):
    def __init__(self, msg: str, cause: BaseException) -> None:

        idMapPyToJ = JavaHandler.valueToObject(dict(), "Map")
        translatedArg0 = JavaHandler.valueToObject(msg, "String", idMapPyToJ)
        translatedArg1 = JavaHandler.valueToObject(cause, "Throwable", idMapPyToJ)
        idMapJToPy = dict()
        try:
            self.javaObj = InvalidContentTypeException.javaClz(translatedArg0, translatedArg1)
            self.javaObj.setPythonObject(self)
            self.javaObj.jToPy(idMapJToPy)
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            JavaHandler.mapping(translatedArg0, idMapJToPy, msg)
            JavaHandler.mapping(translatedArg1, idMapJToPy, cause)
    javaClz = java.type("org.apache.commons.fileupload.FileUploadBase$InvalidContentTypeException")
    def __getattr__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            pass
        return JavaHandler.mapping(getattr(self.javaClz, StaticFieldRedirector.unmangle_name(name)))
class IOFileUploadException(FileUploadException, metaclass=StaticFieldRedirector):
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
            
    def __init__(self, pMsg: str, pException: typing.Union[IOError, OSError]) -> None:

        idMapPyToJ = JavaHandler.valueToObject(dict(), "Map")
        translatedArg0 = JavaHandler.valueToObject(pMsg, "String", idMapPyToJ)
        translatedArg1 = JavaHandler.valueToObject(pException, "IOException", idMapPyToJ)
        idMapJToPy = dict()
        try:
            self.javaObj = IOFileUploadException.javaClz(translatedArg0, translatedArg1)
            self.javaObj.setPythonObject(self)
            self.javaObj.jToPy(idMapJToPy)
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            JavaHandler.mapping(translatedArg0, idMapJToPy, pMsg)
            JavaHandler.mapping(translatedArg1, idMapJToPy, pException)
    javaClz = java.type("org.apache.commons.fileupload.FileUploadBase$IOFileUploadException")
    def __getattr__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            pass
        return JavaHandler.mapping(getattr(self.javaClz, StaticFieldRedirector.unmangle_name(name)))
class SizeLimitExceededException(SizeException, metaclass=StaticFieldRedirector):
    @staticmethod

    def SizeLimitExceededException1(message: str) -> SizeLimitExceededException:

        idMapPyToJ = JavaHandler.valueToObject(dict(), "Map")
        translatedArg0 = JavaHandler.valueToObject(message, "String", idMapPyToJ)
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(SizeLimitExceededException.javaClz.SizeLimitExceededException1(translatedArg0), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass

            JavaHandler.mapping(translatedArg0, idMapJToPy, message)
    @staticmethod

    def SizeLimitExceededException0() -> SizeLimitExceededException:

        idMapPyToJ = JavaHandler.valueToObject(dict(), "Map")
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(SizeLimitExceededException.javaClz.SizeLimitExceededException0(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass

            
    def __init__(self, message: str, actual: int, permitted: int) -> None:

        idMapPyToJ = JavaHandler.valueToObject(dict(), "Map")
        translatedArg0 = JavaHandler.valueToObject(message, "String", idMapPyToJ)
        translatedArg1 = JavaHandler.valueToObject(actual, "long", idMapPyToJ)
        translatedArg2 = JavaHandler.valueToObject(permitted, "long", idMapPyToJ)
        idMapJToPy = dict()
        try:
            self.javaObj = SizeLimitExceededException.javaClz(translatedArg0, translatedArg1, translatedArg2)
            self.javaObj.setPythonObject(self)
            self.javaObj.jToPy(idMapJToPy)
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            JavaHandler.mapping(translatedArg0, idMapJToPy, message)
            JavaHandler.mapping(translatedArg1, idMapJToPy, actual)
            JavaHandler.mapping(translatedArg2, idMapJToPy, permitted)
    javaClz = java.type("org.apache.commons.fileupload.FileUploadBase$SizeLimitExceededException")
    def __getattr__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            pass
        return JavaHandler.mapping(getattr(self.javaClz, StaticFieldRedirector.unmangle_name(name)))
class FileItemIteratorImpl(metaclass=StaticFieldRedirector):
    def __getContentLength(self, pHeaders: FileItemHeaders) -> int:

        idMapPyToJ = self.javaObj.pyToJ()
        translatedArg0 = JavaHandler.valueToObject(pHeaders, "FileItemHeaders", idMapPyToJ)
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.getContentLength(translatedArg0), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            JavaHandler.mapping(translatedArg0, idMapJToPy, pHeaders)
    javaClz = java.type("org.apache.commons.fileupload.FileUploadBase$FileItemIteratorImpl")
    def __getattr__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            pass
        return JavaHandler.mapping(getattr(self.javaClz, StaticFieldRedirector.unmangle_name(name)))
class FileItemStreamImpl(metaclass=StaticFieldRedirector):
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
            
    javaClz = java.type("org.apache.commons.fileupload.FileUploadBase$FileItemIteratorImpl$FileItemStreamImpl")
    def __getattr__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            pass
        return JavaHandler.mapping(getattr(self.javaClz, StaticFieldRedirector.unmangle_name(name)))
class UnknownSizeException(FileUploadException, metaclass=StaticFieldRedirector):
    def __init__(self, message: str) -> None:

        idMapPyToJ = JavaHandler.valueToObject(dict(), "Map")
        translatedArg0 = JavaHandler.valueToObject(message, "String", idMapPyToJ)
        idMapJToPy = dict()
        try:
            self.javaObj = UnknownSizeException.javaClz(translatedArg0)
            self.javaObj.setPythonObject(self)
            self.javaObj.jToPy(idMapJToPy)
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            JavaHandler.mapping(translatedArg0, idMapJToPy, message)
    javaClz = java.type("org.apache.commons.fileupload.FileUploadBase$UnknownSizeException")
    def __getattr__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            pass
        return JavaHandler.mapping(getattr(self.javaClz, StaticFieldRedirector.unmangle_name(name)))
class FileUploadIOException(metaclass=StaticFieldRedirector):
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
            
    def __init__(self, pCause: FileUploadException) -> None:

        idMapPyToJ = JavaHandler.valueToObject(dict(), "Map")
        translatedArg0 = JavaHandler.valueToObject(pCause, "FileUploadException", idMapPyToJ)
        idMapJToPy = dict()
        try:
            self.javaObj = FileUploadIOException.javaClz(translatedArg0)
            self.javaObj.setPythonObject(self)
            self.javaObj.jToPy(idMapJToPy)
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            JavaHandler.mapping(translatedArg0, idMapJToPy, pCause)
    javaClz = java.type("org.apache.commons.fileupload.FileUploadBase$FileUploadIOException")
    def __getattr__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            pass
        return JavaHandler.mapping(getattr(self.javaClz, StaticFieldRedirector.unmangle_name(name)))