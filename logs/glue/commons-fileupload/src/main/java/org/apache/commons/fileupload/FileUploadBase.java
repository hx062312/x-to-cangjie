package org.apache.commons.fileupload;

import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Locale;
import java.util.Map;
import org.apache.commons.fileupload.ContextInitializer;
import org.apache.commons.fileupload.ExceptionHandler;
import org.apache.commons.fileupload.IntegrationUtils;
import org.apache.commons.fileupload.util.FileItemHeadersImpl;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public abstract class FileUploadBase {
  public static class FileUploadIOException extends IOException {
    private transient Value obj =
        IntegrationUtils.createDefaultPythonObject(
            ContextInitializer.getPythonClass(
                "main/org/apache/commons/fileupload/FileUploadBase.py", "FileUploadIOException"));
    public static final long serialVersionUID = -7047616958165584154L;
    public FileUploadException cause;

    public Value getPythonObject() {
      return obj;
    }

    public void setPythonObject(Value obj) {
      this.obj = obj;
    }

    @Override
    public Throwable getCause() {

      return cause;
    }

    public FileUploadIOException(FileUploadException pCause) {

      cause = pCause;
    }

    public java.util.Map pyToJ() {
      java.util.Map idMap = new java.util.HashMap();
      return pyToJ(idMap);
    }

    public java.util.Map pyToJ(java.util.Map idMap) {

      this.cause =
          (FileUploadException)
              IntegrationUtils.valueToObject(
                  this.obj.getMember("_FileUploadIOException__cause"),
                  "FileUploadException",
                  idMap,
                  cause);
      return idMap;
    }

    public Value jToPy() {
      Value idMap = IntegrationUtils.mapToPython(new java.util.HashMap());
      return jToPy(idMap);
    }

    public Value jToPy(Value idMap) {

      this.obj.invokeMember("__setattr__", "javaObj", this);
      this.obj.invokeMember(
          "__setattr__",
          "_FileUploadIOException__cause",
          IntegrationUtils.mapToPython(
              cause, idMap, this.obj.getMember("_FileUploadIOException__cause")));
      return idMap;
    }
  }

  public static class IOFileUploadException extends FileUploadException {
    private transient Value obj =
        IntegrationUtils.createDefaultPythonObject(
            ContextInitializer.getPythonClass(
                "main/org/apache/commons/fileupload/FileUploadBase.py", "IOFileUploadException"));
    public static final long serialVersionUID = 1749796615868477269L;
    public IOException cause;

    public Value getPythonObject() {
      return obj;
    }

    public void setPythonObject(Value obj) {
      this.obj = obj;
    }

    @Override
    public Throwable getCause() {

      return cause;
    }

    public IOFileUploadException(String pMsg, IOException pException) {

      super(pMsg, null);
      cause = pException;
    }

    public java.util.Map pyToJ() {
      java.util.Map idMap = new java.util.HashMap();
      return pyToJ(idMap);
    }

    public java.util.Map pyToJ(java.util.Map idMap) {
      super.pyToJ(idMap);
      this.cause =
          (IOException)
              IntegrationUtils.valueToObject(
                  this.obj.getMember("_IOFileUploadException__cause"), "IOException", idMap, cause);
      return idMap;
    }

    public Value jToPy() {
      Value idMap = IntegrationUtils.mapToPython(new java.util.HashMap());
      return jToPy(idMap);
    }

    public Value jToPy(Value idMap) {
      super.jToPy(idMap);
      this.obj.invokeMember("__setattr__", "javaObj", this);
      this.obj.invokeMember(
          "__setattr__",
          "_IOFileUploadException__cause",
          IntegrationUtils.mapToPython(
              cause, idMap, this.obj.getMember("_IOFileUploadException__cause")));
      return idMap;
    }
  }

  public static class SizeLimitExceededException extends SizeException {
    private transient Value obj =
        IntegrationUtils.createDefaultPythonObject(
            ContextInitializer.getPythonClass(
                "main/org/apache/commons/fileupload/FileUploadBase.py",
                "SizeLimitExceededException"));
    public static final long serialVersionUID = -2474893167098052828L;

    public Value getPythonObject() {
      return obj;
    }

    public void setPythonObject(Value obj) {
      this.obj = obj;
    }

    public static SizeLimitExceededException SizeLimitExceededException1(String message) {

      return new SizeLimitExceededException(message, 0, 0);
    }

    public static SizeLimitExceededException SizeLimitExceededException0() {

      return new SizeLimitExceededException(null, 0, 0);
    }

    public SizeLimitExceededException(String message, long actual, long permitted) {

      super(message, actual, permitted);
    }

    public java.util.Map pyToJ() {
      java.util.Map idMap = new java.util.HashMap();
      return pyToJ(idMap);
    }

    public java.util.Map pyToJ(java.util.Map idMap) {
      super.pyToJ(idMap);

      return idMap;
    }

    public Value jToPy() {
      Value idMap = IntegrationUtils.mapToPython(new java.util.HashMap());
      return jToPy(idMap);
    }

    public Value jToPy(Value idMap) {
      super.jToPy(idMap);
      this.obj.invokeMember("__setattr__", "javaObj", this);

      return idMap;
    }
  }

  public class FileItemIteratorImpl {
    public class FileItemStreamImpl {
      private transient Value obj =
          IntegrationUtils.createDefaultPythonObject(
              ContextInitializer.getPythonClass(
                  "main/org/apache/commons/fileupload/FileUploadBase.py", "FileItemStreamImpl"));
      public boolean opened;
      public FileItemHeaders headers;

      public Value getPythonObject() {
        return obj;
      }

      public void setPythonObject(Value obj) {
        this.obj = obj;
      }

      public void setHeaders(FileItemHeaders pHeaders) {

        headers = pHeaders;
      }

      public FileItemHeaders getHeaders() {

        return headers;
      }

      public java.util.Map pyToJ() {
        java.util.Map idMap = new java.util.HashMap();
        return pyToJ(idMap);
      }

      public java.util.Map pyToJ(java.util.Map idMap) {

        this.opened =
            (boolean)
                IntegrationUtils.valueToObject(
                    this.obj.getMember("_FileItemStreamImpl__opened"), "boolean", idMap, opened);
        this.headers =
            (FileItemHeaders)
                IntegrationUtils.valueToObject(
                    this.obj.getMember("_FileItemStreamImpl__headers"),
                    "FileItemHeaders",
                    idMap,
                    headers);
        return idMap;
      }

      public Value jToPy() {
        Value idMap = IntegrationUtils.mapToPython(new java.util.HashMap());
        return jToPy(idMap);
      }

      public Value jToPy(Value idMap) {

        this.obj.invokeMember("__setattr__", "javaObj", this);
        this.obj.invokeMember(
            "__setattr__",
            "_FileItemStreamImpl__opened",
            IntegrationUtils.mapToPython(
                opened, idMap, this.obj.getMember("_FileItemStreamImpl__opened")));
        this.obj.invokeMember(
            "__setattr__",
            "_FileItemStreamImpl__headers",
            IntegrationUtils.mapToPython(
                headers, idMap, this.obj.getMember("_FileItemStreamImpl__headers")));
        return idMap;
      }
    }

    private transient Value obj =
        IntegrationUtils.createDefaultPythonObject(
            ContextInitializer.getPythonClass(
                "main/org/apache/commons/fileupload/FileUploadBase.py", "FileItemIteratorImpl"));
    public FileItemStreamImpl currentItem;
    public String currentFieldName;
    public boolean skipPreamble;
    public boolean itemValid;
    public boolean eof;

    public Value getPythonObject() {
      return obj;
    }

    public void setPythonObject(Value obj) {
      this.obj = obj;
    }

    public long getContentLength(FileItemHeaders pHeaders) {

      try {
        return Long.parseLong(pHeaders.getHeader(CONTENT_LENGTH));
      } catch (Exception e) {
        return -1;
      }
    }

    public java.util.Map pyToJ() {
      java.util.Map idMap = new java.util.HashMap();
      return pyToJ(idMap);
    }

    public java.util.Map pyToJ(java.util.Map idMap) {

      this.currentItem =
          (FileItemStreamImpl)
              IntegrationUtils.valueToObject(
                  this.obj.getMember("_FileItemIteratorImpl__currentItem"),
                  "FileItemStreamImpl",
                  idMap,
                  currentItem);
      this.currentFieldName =
          (String)
              IntegrationUtils.valueToObject(
                  this.obj.getMember("_FileItemIteratorImpl__currentFieldName"),
                  "String",
                  idMap,
                  currentFieldName);
      this.skipPreamble =
          (boolean)
              IntegrationUtils.valueToObject(
                  this.obj.getMember("_FileItemIteratorImpl__skipPreamble"),
                  "boolean",
                  idMap,
                  skipPreamble);
      this.itemValid =
          (boolean)
              IntegrationUtils.valueToObject(
                  this.obj.getMember("_FileItemIteratorImpl__itemValid"),
                  "boolean",
                  idMap,
                  itemValid);
      this.eof =
          (boolean)
              IntegrationUtils.valueToObject(
                  this.obj.getMember("_FileItemIteratorImpl__eof"), "boolean", idMap, eof);
      return idMap;
    }

    public Value jToPy() {
      Value idMap = IntegrationUtils.mapToPython(new java.util.HashMap());
      return jToPy(idMap);
    }

    public Value jToPy(Value idMap) {

      this.obj.invokeMember("__setattr__", "javaObj", this);
      this.obj.invokeMember(
          "__setattr__",
          "_FileItemIteratorImpl__currentItem",
          IntegrationUtils.mapToPython(
              currentItem, idMap, this.obj.getMember("_FileItemIteratorImpl__currentItem")));
      this.obj.invokeMember(
          "__setattr__",
          "_FileItemIteratorImpl__currentFieldName",
          IntegrationUtils.mapToPython(
              currentFieldName,
              idMap,
              this.obj.getMember("_FileItemIteratorImpl__currentFieldName")));
      this.obj.invokeMember(
          "__setattr__",
          "_FileItemIteratorImpl__skipPreamble",
          IntegrationUtils.mapToPython(
              skipPreamble, idMap, this.obj.getMember("_FileItemIteratorImpl__skipPreamble")));
      this.obj.invokeMember(
          "__setattr__",
          "_FileItemIteratorImpl__itemValid",
          IntegrationUtils.mapToPython(
              itemValid, idMap, this.obj.getMember("_FileItemIteratorImpl__itemValid")));
      this.obj.invokeMember(
          "__setattr__",
          "_FileItemIteratorImpl__eof",
          IntegrationUtils.mapToPython(
              eof, idMap, this.obj.getMember("_FileItemIteratorImpl__eof")));
      return idMap;
    }
  }

  public static class FileSizeLimitExceededException extends SizeException {
    private transient Value obj =
        IntegrationUtils.createDefaultPythonObject(
            ContextInitializer.getPythonClass(
                "main/org/apache/commons/fileupload/FileUploadBase.py",
                "FileSizeLimitExceededException"));
    public static final long serialVersionUID = 8150776562029630058L;
    public String fileName;
    public String fieldName;

    public Value getPythonObject() {
      return obj;
    }

    public void setPythonObject(Value obj) {
      this.obj = obj;
    }

    public void setFieldName(String pFieldName) {

      fieldName = pFieldName;
    }

    public String getFieldName() {

      return fieldName;
    }

    public void setFileName(String pFileName) {

      fileName = pFileName;
    }

    public String getFileName() {

      return fileName;
    }

    public FileSizeLimitExceededException(String message, long actual, long permitted) {

      super(message, actual, permitted);
    }

    public java.util.Map pyToJ() {
      java.util.Map idMap = new java.util.HashMap();
      return pyToJ(idMap);
    }

    public java.util.Map pyToJ(java.util.Map idMap) {
      super.pyToJ(idMap);
      this.fileName =
          (String)
              IntegrationUtils.valueToObject(
                  this.obj.getMember("_FileSizeLimitExceededException__fileName"),
                  "String",
                  idMap,
                  fileName);
      this.fieldName =
          (String)
              IntegrationUtils.valueToObject(
                  this.obj.getMember("_FileSizeLimitExceededException__fieldName"),
                  "String",
                  idMap,
                  fieldName);
      return idMap;
    }

    public Value jToPy() {
      Value idMap = IntegrationUtils.mapToPython(new java.util.HashMap());
      return jToPy(idMap);
    }

    public Value jToPy(Value idMap) {
      super.jToPy(idMap);
      this.obj.invokeMember("__setattr__", "javaObj", this);
      this.obj.invokeMember(
          "__setattr__",
          "_FileSizeLimitExceededException__fileName",
          IntegrationUtils.mapToPython(
              fileName, idMap, this.obj.getMember("_FileSizeLimitExceededException__fileName")));
      this.obj.invokeMember(
          "__setattr__",
          "_FileSizeLimitExceededException__fieldName",
          IntegrationUtils.mapToPython(
              fieldName, idMap, this.obj.getMember("_FileSizeLimitExceededException__fieldName")));
      return idMap;
    }
  }

  public abstract static class SizeException extends FileUploadException {
    private transient Value obj =
        IntegrationUtils.createDefaultPythonObject(
            ContextInitializer.getPythonClass(
                "main/org/apache/commons/fileupload/FileUploadBase.py", "SizeException"));
    public static final long serialVersionUID = -8776225574705254126L;
    public final long actual;
    public final long permitted;

    public Value getPythonObject() {
      return obj;
    }

    public void setPythonObject(Value obj) {
      this.obj = obj;
    }

    public long getPermittedSize() {

      return permitted;
    }

    public long getActualSize() {

      return actual;
    }

    public SizeException(String message, long actual, long permitted) {

      super(message, null);
      this.actual = actual;
      this.permitted = permitted;
    }

    public java.util.Map pyToJ() {
      java.util.Map idMap = new java.util.HashMap();
      return pyToJ(idMap);
    }

    public java.util.Map pyToJ(java.util.Map idMap) {
      super.pyToJ(idMap);

      return idMap;
    }

    public Value jToPy() {
      Value idMap = IntegrationUtils.mapToPython(new java.util.HashMap());
      return jToPy(idMap);
    }

    public Value jToPy(Value idMap) {
      super.jToPy(idMap);
      this.obj.invokeMember("__setattr__", "javaObj", this);
      this.obj.invokeMember(
          "__setattr__",
          "_SizeException__actual",
          IntegrationUtils.mapToPython(
              actual, idMap, this.obj.getMember("_SizeException__actual")));
      this.obj.invokeMember(
          "__setattr__",
          "_SizeException__permitted",
          IntegrationUtils.mapToPython(
              permitted, idMap, this.obj.getMember("_SizeException__permitted")));
      return idMap;
    }
  }

  public static class InvalidContentTypeException extends FileUploadException {
    private transient Value obj =
        IntegrationUtils.createDefaultPythonObject(
            ContextInitializer.getPythonClass(
                "main/org/apache/commons/fileupload/FileUploadBase.py",
                "InvalidContentTypeException"));
    public static final long serialVersionUID = -9073026332015646668L;

    public Value getPythonObject() {
      return obj;
    }

    public void setPythonObject(Value obj) {
      this.obj = obj;
    }

    public InvalidContentTypeException(String msg, Throwable cause) {

      super(msg, cause);
    }

    public java.util.Map pyToJ() {
      java.util.Map idMap = new java.util.HashMap();
      return pyToJ(idMap);
    }

    public java.util.Map pyToJ(java.util.Map idMap) {
      super.pyToJ(idMap);

      return idMap;
    }

    public Value jToPy() {
      Value idMap = IntegrationUtils.mapToPython(new java.util.HashMap());
      return jToPy(idMap);
    }

    public Value jToPy(Value idMap) {
      super.jToPy(idMap);
      this.obj.invokeMember("__setattr__", "javaObj", this);

      return idMap;
    }
  }

  public static class UnknownSizeException extends FileUploadException {
    private transient Value obj =
        IntegrationUtils.createDefaultPythonObject(
            ContextInitializer.getPythonClass(
                "main/org/apache/commons/fileupload/FileUploadBase.py", "UnknownSizeException"));
    public static final long serialVersionUID = 7062279004812015273L;

    public Value getPythonObject() {
      return obj;
    }

    public void setPythonObject(Value obj) {
      this.obj = obj;
    }

    public UnknownSizeException(String message) {

      super(message, null);
    }

    public java.util.Map pyToJ() {
      java.util.Map idMap = new java.util.HashMap();
      return pyToJ(idMap);
    }

    public java.util.Map pyToJ(java.util.Map idMap) {
      super.pyToJ(idMap);

      return idMap;
    }

    public Value jToPy() {
      Value idMap = IntegrationUtils.mapToPython(new java.util.HashMap());
      return jToPy(idMap);
    }

    public Value jToPy(Value idMap) {
      super.jToPy(idMap);
      this.obj.invokeMember("__setattr__", "javaObj", this);

      return idMap;
    }
  }

  private transient Value obj =
      IntegrationUtils.createDefaultPythonObject(
          ContextInitializer.getPythonClass(
              "main/org/apache/commons/fileupload/FileUploadBase.py", "FileUploadBase"));
  public static final String CONTENT_TYPE = "Content-type";
  public static final String CONTENT_DISPOSITION = "Content-disposition";
  public static final String CONTENT_LENGTH = "Content-length";
  public static final String FORM_DATA = "form-data";
  public static final String ATTACHMENT = "attachment";
  public static final String MULTIPART = "multipart/";
  public static final String MULTIPART_FORM_DATA = "multipart/form-data";
  public static final String MULTIPART_MIXED = "multipart/mixed";
  @Deprecated public static final int MAX_HEADER_SIZE = 1024;
  public long sizeMax = -1;
  public long fileSizeMax = -1;
  public long fileCountMax = -1;
  public String headerEncoding;
  public ProgressListener listener;

  public Value getPythonObject() {
    return obj;
  }

  public void setPythonObject(Value obj) {
    this.obj = obj;
  }

  public final String getHeader(Map<String, String> headers, String name) {

    return headers.get(name.toLowerCase(Locale.ENGLISH));
  }

  public Map<String, String> parseHeaders(String headerPart) {

    FileItemHeaders headers = getParsedHeaders(headerPart);
    Map<String, String> result = new HashMap<String, String>();
    for (Iterator<String> iter = headers.getHeaderNames(); iter.hasNext(); ) {
      String headerName = iter.next();
      Iterator<String> iter2 = headers.getHeaders(headerName);
      StringBuilder headerValue = new StringBuilder(iter2.next());
      while (iter2.hasNext()) {
        headerValue.append(",").append(iter2.next());
      }
      result.put(headerName, headerValue.toString());
    }
    return result;
  }

  public FileItem createItem(Map<String, String> headers, boolean isFormField)
      throws FileUploadException {

    try {

      return getFileItemFactory()
          .createItem(
              getFieldName2(headers),
              getHeader(headers, CONTENT_TYPE),
              isFormField,
              getFileName0(headers));

    } catch (Throwable ExceptionObjectForCaching) {
      ExceptionHandler.ERR = ExceptionObjectForCaching;
      throw ExceptionObjectForCaching;
    }
  }

  public String getFieldName2(Map<String, String> headers) {

    return getFieldName1(getHeader(headers, CONTENT_DISPOSITION));
  }

  public String getFileName0(Map<String, String> headers) {

    return getFileName2(getHeader(headers, CONTENT_DISPOSITION));
  }

  public void setProgressListener(ProgressListener pListener) {

    listener = pListener;
  }

  public ProgressListener getProgressListener() {

    return listener;
  }

  public FileItemHeadersImpl newFileItemHeaders() {

    return new FileItemHeadersImpl();
  }

  public FileItemHeaders getParsedHeaders(String headerPart) {

    final int len = headerPart.length();
    FileItemHeadersImpl headers = newFileItemHeaders();
    int start = 0;
    for (; ; ) {
      int end = parseEndOfLine(headerPart, start);
      if (start == end) {
        break;
      }
      StringBuilder header = new StringBuilder(headerPart.substring(start, end));
      start = end + 2;
      while (start < len) {
        int nonWs = start;
        while (nonWs < len) {
          char c = headerPart.charAt(nonWs);
          if (c != ' ' && c != '\t') {
            break;
          }
          ++nonWs;
        }
        if (nonWs == start) {
          break;
        }
        end = parseEndOfLine(headerPart, nonWs);
        header.append(" ").append(headerPart.substring(nonWs, end));
        start = end + 2;
      }
      parseHeaderLine(headers, header.toString());
    }
    return headers;
  }

  public String getFieldName0(FileItemHeaders headers) {

    return getFieldName1(headers.getHeader(CONTENT_DISPOSITION));
  }

  public String getFileName1(FileItemHeaders headers) {

    return getFileName2(headers.getHeader(CONTENT_DISPOSITION));
  }

  public byte[] getBoundary(String contentType) {

    ParameterParser parser = new ParameterParser();
    parser.setLowerCaseNames(true);
    Map<String, String> params = parser.parse0(contentType, new char[] {';', ','});
    String boundaryStr = params.get("boundary");

    if (boundaryStr == null) {
      return null;
    }
    byte[] boundary;
    try {
      boundary = boundaryStr.getBytes("ISO-8859-1");
    } catch (UnsupportedEncodingException e) {
      boundary = boundaryStr.getBytes(); // Intentionally falls back to default charset
    }
    return boundary;
  }

  public void setHeaderEncoding(String encoding) {

    headerEncoding = encoding;
  }

  public String getHeaderEncoding() {

    return headerEncoding;
  }

  public void setFileCountMax(final long fileCountMax) {

    this.fileCountMax = fileCountMax;
  }

  public long getFileCountMax() {

    return fileCountMax;
  }

  public void setFileSizeMax(long fileSizeMax) {

    this.fileSizeMax = fileSizeMax;
  }

  public long getFileSizeMax() {

    return fileSizeMax;
  }

  public void setSizeMax(long sizeMax) {

    this.sizeMax = sizeMax;
  }

  public long getSizeMax() {

    return sizeMax;
  }

  public static final boolean isMultipartContent(RequestContext ctx) {

    String contentType = ctx.getContentType();
    if (contentType == null) {
      return false;
    }
    if (contentType.toLowerCase(Locale.ENGLISH).startsWith(MULTIPART)) {
      return true;
    }
    return false;
  }

  public void parseHeaderLine(FileItemHeadersImpl headers, String header) {

    final int colonOffset = header.indexOf(':');
    if (colonOffset == -1) {
      return;
    }
    String headerName = header.substring(0, colonOffset).trim();
    String headerValue = header.substring(header.indexOf(':') + 1).trim();
    headers.addHeader(headerName, headerValue);
  }

  public int parseEndOfLine(String headerPart, int end) {

    try {

      int index = end;
      for (; ; ) {
        int offset = headerPart.indexOf('\r', index);
        if (offset == -1 || offset + 1 >= headerPart.length()) {
          throw new IllegalStateException("Expected headers to be terminated by an empty line.");
        }
        if (headerPart.charAt(offset + 1) == '\n') {
          return offset;
        }
        index = offset + 1;
      }

    } catch (Throwable ExceptionObjectForCaching) {
      ExceptionHandler.ERR = ExceptionObjectForCaching;
      throw ExceptionObjectForCaching;
    }
  }

  public String getFieldName1(String pContentDisposition) {

    String fieldName = null;
    if (pContentDisposition != null
        && pContentDisposition.toLowerCase(Locale.ENGLISH).startsWith(FORM_DATA)) {
      ParameterParser parser = new ParameterParser();
      parser.setLowerCaseNames(true);
      Map<String, String> params = parser.parse1(pContentDisposition, ';');
      fieldName = params.get("name");
      if (fieldName != null) {
        fieldName = fieldName.trim();
      }
    }
    return fieldName;
  }

  public String getFileName2(String pContentDisposition) {

    String fileName = null;
    if (pContentDisposition != null) {
      String cdl = pContentDisposition.toLowerCase(Locale.ENGLISH);
      if (cdl.startsWith(FORM_DATA) || cdl.startsWith(ATTACHMENT)) {
        ParameterParser parser = new ParameterParser();
        parser.setLowerCaseNames(true);
        Map<String, String> params = parser.parse1(pContentDisposition, ';');
        if (params.containsKey("filename")) {
          fileName = params.get("filename");
          if (fileName != null) {
            fileName = fileName.trim();
          } else {
            fileName = "";
          }
        }
      }
    }
    return fileName;
  }

  public abstract void setFileItemFactory(FileItemFactory factory);

  public abstract FileItemFactory getFileItemFactory();

  public java.util.Map pyToJ() {
    java.util.Map idMap = new java.util.HashMap();
    return pyToJ(idMap);
  }

  public java.util.Map pyToJ(java.util.Map idMap) {

    this.sizeMax =
        (long)
            IntegrationUtils.valueToObject(
                this.obj.getMember("_FileUploadBase__sizeMax"), "long", idMap, sizeMax);
    this.fileSizeMax =
        (long)
            IntegrationUtils.valueToObject(
                this.obj.getMember("_FileUploadBase__fileSizeMax"), "long", idMap, fileSizeMax);
    this.fileCountMax =
        (long)
            IntegrationUtils.valueToObject(
                this.obj.getMember("_FileUploadBase__fileCountMax"), "long", idMap, fileCountMax);
    this.headerEncoding =
        (String)
            IntegrationUtils.valueToObject(
                this.obj.getMember("_FileUploadBase__headerEncoding"),
                "String",
                idMap,
                headerEncoding);
    this.listener =
        (ProgressListener)
            IntegrationUtils.valueToObject(
                this.obj.getMember("_FileUploadBase__listener"),
                "ProgressListener",
                idMap,
                listener);
    return idMap;
  }

  public Value jToPy() {
    Value idMap = IntegrationUtils.mapToPython(new java.util.HashMap());
    return jToPy(idMap);
  }

  public Value jToPy(Value idMap) {

    this.obj.invokeMember("__setattr__", "javaObj", this);
    this.obj.invokeMember(
        "__setattr__",
        "_FileUploadBase__sizeMax",
        IntegrationUtils.mapToPython(
            sizeMax, idMap, this.obj.getMember("_FileUploadBase__sizeMax")));
    this.obj.invokeMember(
        "__setattr__",
        "_FileUploadBase__fileSizeMax",
        IntegrationUtils.mapToPython(
            fileSizeMax, idMap, this.obj.getMember("_FileUploadBase__fileSizeMax")));
    this.obj.invokeMember(
        "__setattr__",
        "_FileUploadBase__fileCountMax",
        IntegrationUtils.mapToPython(
            fileCountMax, idMap, this.obj.getMember("_FileUploadBase__fileCountMax")));
    this.obj.invokeMember(
        "__setattr__",
        "_FileUploadBase__headerEncoding",
        IntegrationUtils.mapToPython(
            headerEncoding, idMap, this.obj.getMember("_FileUploadBase__headerEncoding")));
    this.obj.invokeMember(
        "__setattr__",
        "_FileUploadBase__listener",
        IntegrationUtils.mapToPython(
            listener, idMap, this.obj.getMember("_FileUploadBase__listener")));
    return idMap;
  }
}
