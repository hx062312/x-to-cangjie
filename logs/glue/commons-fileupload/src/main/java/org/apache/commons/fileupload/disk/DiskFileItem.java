package org.apache.commons.fileupload.disk;

import static java.lang.String.format;

import java.io.File;
import java.util.Map;
import java.util.UUID;
import java.util.concurrent.atomic.AtomicInteger;
import org.apache.commons.fileupload.ContextInitializer;
import org.apache.commons.fileupload.ExceptionHandler;
import org.apache.commons.fileupload.FileItemHeaders;
import org.apache.commons.fileupload.IntegrationUtils;
import org.apache.commons.fileupload.ParameterParser;
import org.apache.commons.fileupload.util.Streams;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public class DiskFileItem {
  private transient Value obj =
      IntegrationUtils.createDefaultPythonObject(
          ContextInitializer.getPythonClass(
              "main/org/apache/commons/fileupload/disk/DiskFileItem.py", "DiskFileItem"));
  public static final String DEFAULT_CHARSET = "ISO-8859-1";
  public static final String UID = UUID.randomUUID().toString().replace('-', '_');
  public static final AtomicInteger COUNTER = new AtomicInteger(0);
  public String fieldName;
  public final String contentType;
  public boolean isFormField;
  public final String fileName;
  public long size = -1;
  public final int sizeThreshold;
  public File repository;
  public byte[] cachedContent;
  public transient File tempFile;
  public FileItemHeaders headers;
  public String defaultCharset = DEFAULT_CHARSET;

  public Value getPythonObject() {
    return obj;
  }

  public void setPythonObject(Value obj) {
    this.obj = obj;
  }

  public void setDefaultCharset(String charset) {

    defaultCharset = charset;
  }

  public String getDefaultCharset() {

    return defaultCharset;
  }

  public void setHeaders(FileItemHeaders pHeaders) {

    headers = pHeaders;
  }

  public FileItemHeaders getHeaders() {

    return headers;
  }

  public File getTempFile() {

    if (tempFile == null) {
      File tempDir = repository;
      if (tempDir == null) {
        tempDir = new File(System.getProperty("java.io.tmpdir"));
      }

      String tempFileName = format("upload_%s_%s.tmp", UID, getUniqueId());

      tempFile = new File(tempDir, tempFileName);
    }
    return tempFile;
  }

  public void setFormField(boolean state) {

    isFormField = state;
  }

  public boolean isFormField() {

    return isFormField;
  }

  public void setFieldName(String fieldName) {

    this.fieldName = fieldName;
  }

  public String getFieldName() {

    return fieldName;
  }

  public String getName() {

    return Streams.checkFileName(fileName);
  }

  public String getCharSet() {

    ParameterParser parser = new ParameterParser();
    parser.setLowerCaseNames(true);
    Map<String, String> params = parser.parse1(getContentType(), ';');
    return params.get("charset");
  }

  public String getContentType() {

    return contentType;
  }

  public DiskFileItem(
      String fieldName,
      String contentType,
      boolean isFormField,
      String fileName,
      int sizeThreshold,
      File repository) {

    this.fieldName = fieldName;
    this.contentType = contentType;
    this.isFormField = isFormField;
    this.fileName = fileName;
    this.sizeThreshold = sizeThreshold;
    this.repository = repository;
  }

  public static String getUniqueId() {

    final int limit = 100000000;
    int current = COUNTER.getAndIncrement();
    String id = Integer.toString(current);

    if (current < limit) {
      id = ("00000000" + id).substring(id.length());
    }
    return id;
  }

  public java.util.Map pyToJ() {
    java.util.Map idMap = new java.util.HashMap();
    return pyToJ(idMap);
  }

  public java.util.Map pyToJ(java.util.Map idMap) {

    this.fieldName =
        (String)
            IntegrationUtils.valueToObject(
                this.obj.getMember("_DiskFileItem__fieldName"), "String", idMap, fieldName);
    this.isFormField =
        (boolean)
            IntegrationUtils.valueToObject(
                this.obj.getMember("_DiskFileItem__isFormField"), "boolean", idMap, isFormField);
    this.size =
        (long)
            IntegrationUtils.valueToObject(
                this.obj.getMember("_DiskFileItem__size"), "long", idMap, size);
    this.repository =
        (File)
            IntegrationUtils.valueToObject(
                this.obj.getMember("_DiskFileItem__repository"), "File", idMap, repository);
    this.cachedContent =
        (byte[])
            IntegrationUtils.valueToObject(
                this.obj.getMember("_DiskFileItem__cachedContent"),
                "byte[]",
                idMap,
                byte.class,
                cachedContent);
    this.tempFile =
        (File)
            IntegrationUtils.valueToObject(
                this.obj.getMember("_DiskFileItem__tempFile"), "File", idMap, tempFile);
    this.headers =
        (FileItemHeaders)
            IntegrationUtils.valueToObject(
                this.obj.getMember("_DiskFileItem__headers"), "FileItemHeaders", idMap, headers);
    this.defaultCharset =
        (String)
            IntegrationUtils.valueToObject(
                this.obj.getMember("_DiskFileItem__defaultCharset"),
                "String",
                idMap,
                defaultCharset);
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
        "_DiskFileItem__fieldName",
        IntegrationUtils.mapToPython(
            fieldName, idMap, this.obj.getMember("_DiskFileItem__fieldName")));
    this.obj.invokeMember(
        "__setattr__",
        "_DiskFileItem__contentType",
        IntegrationUtils.mapToPython(
            contentType, idMap, this.obj.getMember("_DiskFileItem__contentType")));
    this.obj.invokeMember(
        "__setattr__",
        "_DiskFileItem__isFormField",
        IntegrationUtils.mapToPython(
            isFormField, idMap, this.obj.getMember("_DiskFileItem__isFormField")));
    this.obj.invokeMember(
        "__setattr__",
        "_DiskFileItem__fileName",
        IntegrationUtils.mapToPython(
            fileName, idMap, this.obj.getMember("_DiskFileItem__fileName")));
    this.obj.invokeMember(
        "__setattr__",
        "_DiskFileItem__size",
        IntegrationUtils.mapToPython(size, idMap, this.obj.getMember("_DiskFileItem__size")));
    this.obj.invokeMember(
        "__setattr__",
        "_DiskFileItem__sizeThreshold",
        IntegrationUtils.mapToPython(
            sizeThreshold, idMap, this.obj.getMember("_DiskFileItem__sizeThreshold")));
    this.obj.invokeMember(
        "__setattr__",
        "_DiskFileItem__repository",
        IntegrationUtils.mapToPython(
            repository, idMap, this.obj.getMember("_DiskFileItem__repository")));
    this.obj.invokeMember(
        "__setattr__",
        "_DiskFileItem__cachedContent",
        IntegrationUtils.mapToPython(
            cachedContent, idMap, this.obj.getMember("_DiskFileItem__cachedContent")));
    this.obj.invokeMember(
        "__setattr__",
        "_DiskFileItem__tempFile",
        IntegrationUtils.mapToPython(
            tempFile, idMap, this.obj.getMember("_DiskFileItem__tempFile")));
    this.obj.invokeMember(
        "__setattr__",
        "_DiskFileItem__headers",
        IntegrationUtils.mapToPython(headers, idMap, this.obj.getMember("_DiskFileItem__headers")));
    this.obj.invokeMember(
        "__setattr__",
        "_DiskFileItem__defaultCharset",
        IntegrationUtils.mapToPython(
            defaultCharset, idMap, this.obj.getMember("_DiskFileItem__defaultCharset")));
    return idMap;
  }
}
