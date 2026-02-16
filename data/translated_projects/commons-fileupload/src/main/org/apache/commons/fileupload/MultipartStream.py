from __future__ import annotations
from io import StringIO
import io
from io import BytesIO
import typing
from typing import *
import os
from src.main.org.apache.commons.fileupload.FileUploadBase import *
from src.main.org.apache.commons.fileupload.FileItemStream import *
from src.main.org.apache.commons.fileupload.util.Closeable import *
from src.main.org.apache.commons.fileupload.ProgressListener import *
import java # type: ignore
from src.main.org.apache.commons.fileupload.java_handler import *
class MultipartStream(metaclass=StaticFieldRedirector):
    @staticmethod

    def MultipartStream3(input_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader], boundary: typing.List[int]) -> MultipartStream:

        idMapPyToJ = JavaHandler.valueToObject(dict(), "Map")
        translatedArg0 = JavaHandler.valueToObject(input_, "InputStream", idMapPyToJ)
        translatedArg1 = boundary
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(MultipartStream.javaClz.MultipartStream3(translatedArg0, translatedArg1), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass

            JavaHandler.mapping(translatedArg0, idMapJToPy, input_)
            JavaHandler.mapping(translatedArg1, idMapJToPy, boundary)
    @staticmethod

    def MultipartStream1(input_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader], boundary: typing.List[int], bufSize: int) -> MultipartStream:

        idMapPyToJ = JavaHandler.valueToObject(dict(), "Map")
        translatedArg0 = JavaHandler.valueToObject(input_, "InputStream", idMapPyToJ)
        translatedArg1 = boundary
        translatedArg2 = JavaHandler.valueToObject(bufSize, "int", idMapPyToJ)
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(MultipartStream.javaClz.MultipartStream1(translatedArg0, translatedArg1, translatedArg2), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass

            JavaHandler.mapping(translatedArg0, idMapJToPy, input_)
            JavaHandler.mapping(translatedArg1, idMapJToPy, boundary)
            JavaHandler.mapping(translatedArg2, idMapJToPy, bufSize)
    @staticmethod

    def MultipartStream0() -> MultipartStream:

        idMapPyToJ = JavaHandler.valueToObject(dict(), "Map")
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(MultipartStream.javaClz.MultipartStream0(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass

            
    def _findSeparator(self) -> int:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.findSeparator(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
    def _findByte(self, value: int, pos: int) -> int:

        idMapPyToJ = self.javaObj.pyToJ()
        translatedArg0 = JavaHandler.valueToObject(value, "byte", idMapPyToJ)
        translatedArg1 = JavaHandler.valueToObject(pos, "int", idMapPyToJ)
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.findByte(translatedArg0, translatedArg1), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            JavaHandler.mapping(translatedArg0, idMapJToPy, value)
            JavaHandler.mapping(translatedArg1, idMapJToPy, pos)
    @staticmethod

    def arrayequals(a: typing.List[int], b: typing.List[int], count: int) -> bool:

        idMapPyToJ = JavaHandler.valueToObject(dict(), "Map")
        translatedArg0 = a
        translatedArg1 = b
        translatedArg2 = JavaHandler.valueToObject(count, "int", idMapPyToJ)
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(MultipartStream.javaClz.arrayequals(translatedArg0, translatedArg1, translatedArg2), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass

            JavaHandler.mapping(translatedArg0, idMapJToPy, a)
            JavaHandler.mapping(translatedArg1, idMapJToPy, b)
            JavaHandler.mapping(translatedArg2, idMapJToPy, count)
    def readHeaders(self) -> str:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.readHeaders(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
    def setBoundary(self, boundary: typing.List[int]) -> None:

        idMapPyToJ = self.javaObj.pyToJ()
        translatedArg0 = boundary
        idMapJToPy = dict()
        try:
            self.javaObj.setBoundary(translatedArg0)
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            JavaHandler.mapping(translatedArg0, idMapJToPy, boundary)
    def readBoundary(self) -> bool:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.readBoundary(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
    def readByte(self) -> int:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.readByte(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
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
            
    @staticmethod

    def MultipartStream2(input_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader], boundary: typing.List[int], pNotifier: ProgressNotifier) -> MultipartStream:

        idMapPyToJ = JavaHandler.valueToObject(dict(), "Map")
        translatedArg0 = JavaHandler.valueToObject(input_, "InputStream", idMapPyToJ)
        translatedArg1 = boundary
        translatedArg2 = JavaHandler.valueToObject(pNotifier, "ProgressNotifier", idMapPyToJ)
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(MultipartStream.javaClz.MultipartStream2(translatedArg0, translatedArg1, translatedArg2), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass

            JavaHandler.mapping(translatedArg0, idMapJToPy, input_)
            JavaHandler.mapping(translatedArg1, idMapJToPy, boundary)
            JavaHandler.mapping(translatedArg2, idMapJToPy, pNotifier)
    def __init__(self, input_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader], boundary: typing.List[int], bufSize: int, pNotifier: ProgressNotifier) -> None:

        idMapPyToJ = JavaHandler.valueToObject(dict(), "Map")
        translatedArg0 = JavaHandler.valueToObject(input_, "InputStream", idMapPyToJ)
        translatedArg1 = boundary
        translatedArg2 = JavaHandler.valueToObject(bufSize, "int", idMapPyToJ)
        translatedArg3 = JavaHandler.valueToObject(pNotifier, "ProgressNotifier", idMapPyToJ)
        idMapJToPy = dict()
        try:
            self.javaObj = MultipartStream.javaClz(translatedArg0, translatedArg1, translatedArg2, translatedArg3)
            self.javaObj.setPythonObject(self)
            self.javaObj.jToPy(idMapJToPy)
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            JavaHandler.mapping(translatedArg0, idMapJToPy, input_)
            JavaHandler.mapping(translatedArg1, idMapJToPy, boundary)
            JavaHandler.mapping(translatedArg2, idMapJToPy, bufSize)
            JavaHandler.mapping(translatedArg3, idMapJToPy, pNotifier)
    def __computeBoundaryTable(self) -> None:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            self.javaObj.computeBoundaryTable()
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
    def newInputStream(self) -> ItemInputStream:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.newInputStream(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
    javaClz = java.type("org.apache.commons.fileupload.MultipartStream")
    def __getattr__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            pass
        return JavaHandler.mapping(getattr(self.javaClz, StaticFieldRedirector.unmangle_name(name)))
class ItemInputStream(metaclass=StaticFieldRedirector):
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
            
    def skip(self, bytes_: int) -> int:

        idMapPyToJ = self.javaObj.pyToJ()
        translatedArg0 = JavaHandler.valueToObject(bytes_, "long", idMapPyToJ)
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.skip(translatedArg0), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            JavaHandler.mapping(translatedArg0, idMapJToPy, bytes_)
    def read(self) -> int:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.read(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
    def available(self) -> int:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.available(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
    def close1(self, pCloseUnderlying: bool) -> None:

        idMapPyToJ = self.javaObj.pyToJ()
        translatedArg0 = JavaHandler.valueToObject(pCloseUnderlying, "boolean", idMapPyToJ)
        idMapJToPy = dict()
        try:
            self.javaObj.close1(translatedArg0)
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            JavaHandler.mapping(translatedArg0, idMapJToPy, pCloseUnderlying)
    def close0(self) -> None:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            self.javaObj.close0()
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
            
    def getBytesRead(self) -> int:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.getBytesRead(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
    def __makeAvailable(self) -> int:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            val = JavaHandler.mapping(self.javaObj.makeAvailable(), id_map=idMapJToPy)
            return val
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
    def __findSeparator(self) -> None:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            self.javaObj.findSeparator()
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
    def __init__(self) -> None:

        idMapPyToJ = JavaHandler.valueToObject(dict(), "Map")
        
        idMapJToPy = dict()
        try:
            self.javaObj = ItemInputStream.javaClz()
            self.javaObj.setPythonObject(self)
            self.javaObj.jToPy(idMapJToPy)
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            
    javaClz = java.type("org.apache.commons.fileupload.MultipartStream$ItemInputStream")
    def __getattr__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            pass
        return JavaHandler.mapping(getattr(self.javaClz, StaticFieldRedirector.unmangle_name(name)))
class IllegalBoundaryException(metaclass=StaticFieldRedirector):
    def __init__(self, message: str) -> None:

        idMapPyToJ = JavaHandler.valueToObject(dict(), "Map")
        translatedArg0 = JavaHandler.valueToObject(message, "String", idMapPyToJ)
        idMapJToPy = dict()
        try:
            self.javaObj = IllegalBoundaryException.javaClz(translatedArg0)
            self.javaObj.setPythonObject(self)
            self.javaObj.jToPy(idMapJToPy)
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            JavaHandler.mapping(translatedArg0, idMapJToPy, message)
    javaClz = java.type("org.apache.commons.fileupload.MultipartStream$IllegalBoundaryException")
    def __getattr__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            pass
        return JavaHandler.mapping(getattr(self.javaClz, StaticFieldRedirector.unmangle_name(name)))
class MalformedStreamException(metaclass=StaticFieldRedirector):
    def __init__(self, message: str) -> None:

        idMapPyToJ = JavaHandler.valueToObject(dict(), "Map")
        translatedArg0 = JavaHandler.valueToObject(message, "String", idMapPyToJ)
        idMapJToPy = dict()
        try:
            self.javaObj = MalformedStreamException.javaClz(translatedArg0)
            self.javaObj.setPythonObject(self)
            self.javaObj.jToPy(idMapJToPy)
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            JavaHandler.mapping(translatedArg0, idMapJToPy, message)
    javaClz = java.type("org.apache.commons.fileupload.MultipartStream$MalformedStreamException")
    def __getattr__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            pass
        return JavaHandler.mapping(getattr(self.javaClz, StaticFieldRedirector.unmangle_name(name)))
class ProgressNotifier(metaclass=StaticFieldRedirector):
    def __notifyListener(self) -> None:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            self.javaObj.notifyListener()
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
    def noteItem(self) -> None:

        idMapPyToJ = self.javaObj.pyToJ()
        
        idMapJToPy = dict()
        try:
            self.javaObj.noteItem()
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            
    def noteBytesRead(self, pBytes: int) -> None:

        idMapPyToJ = self.javaObj.pyToJ()
        translatedArg0 = JavaHandler.valueToObject(pBytes, "int", idMapPyToJ)
        idMapJToPy = dict()
        try:
            self.javaObj.noteBytesRead(translatedArg0)
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            self.javaObj.jToPy(idMapJToPy)
            JavaHandler.mapping(translatedArg0, idMapJToPy, pBytes)
    def __init__(self, pListener: ProgressListener, pContentLength: int) -> None:

        idMapPyToJ = JavaHandler.valueToObject(dict(), "Map")
        translatedArg0 = JavaHandler.valueToObject(pListener, "ProgressListener", idMapPyToJ)
        translatedArg1 = JavaHandler.valueToObject(pContentLength, "long", idMapPyToJ)
        idMapJToPy = dict()
        try:
            self.javaObj = ProgressNotifier.javaClz(translatedArg0, translatedArg1)
            self.javaObj.setPythonObject(self)
            self.javaObj.jToPy(idMapJToPy)
        except:
            raise JavaHandler.mapping(java.type("org.apache.commons.fileupload.ExceptionHandler").ERR)
        finally:
            pass
            JavaHandler.mapping(translatedArg0, idMapJToPy, pListener)
            JavaHandler.mapping(translatedArg1, idMapJToPy, pContentLength)
    javaClz = java.type("org.apache.commons.fileupload.MultipartStream$ProgressNotifier")
    def __getattr__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            pass
        return JavaHandler.mapping(getattr(self.javaClz, StaticFieldRedirector.unmangle_name(name)))