package org.apache.commons.fileupload.disk;

import java.io.File;
import org.apache.commons.fileupload.ContextInitializer;
import org.apache.commons.fileupload.ExceptionHandler;
import org.apache.commons.fileupload.IntegrationUtils;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public class DiskFileItemFactory {
  private transient Value obj =
      IntegrationUtils.createDefaultPythonObject(
          ContextInitializer.getPythonClass(
              "main/org/apache/commons/fileupload/disk/DiskFileItemFactory.py",
              "DiskFileItemFactory"));
  public static final int DEFAULT_SIZE_THRESHOLD = 10240;
  public File repository;
  public int sizeThreshold = DEFAULT_SIZE_THRESHOLD;
  public String defaultCharset = DiskFileItem.DEFAULT_CHARSET;

  public Value getPythonObject() {
    return obj;
  }

  public void setPythonObject(Value obj) {
    this.obj = obj;
  }

  public void setDefaultCharset(String pCharset) {

    defaultCharset = pCharset;
  }

  public String getDefaultCharset() {

    return defaultCharset;
  }

  public void setSizeThreshold(int sizeThreshold) {

    this.sizeThreshold = sizeThreshold;
  }

  public int getSizeThreshold() {

    return sizeThreshold;
  }

  public void setRepository(File repository) {

    this.repository = repository;
  }

  public File getRepository() {

    return repository;
  }

  public static DiskFileItemFactory DiskFileItemFactory1() {

    return new DiskFileItemFactory(DEFAULT_SIZE_THRESHOLD, null);
  }

  public DiskFileItemFactory(int sizeThreshold, File repository) {

    this.sizeThreshold = sizeThreshold;
    this.repository = repository;
  }

  public java.util.Map pyToJ() {
    java.util.Map idMap = new java.util.HashMap();
    return pyToJ(idMap);
  }

  public java.util.Map pyToJ(java.util.Map idMap) {

    this.repository =
        (File)
            IntegrationUtils.valueToObject(
                this.obj.getMember("_DiskFileItemFactory__repository"), "File", idMap, repository);
    this.sizeThreshold =
        (int)
            IntegrationUtils.valueToObject(
                this.obj.getMember("_DiskFileItemFactory__sizeThreshold"),
                "int",
                idMap,
                sizeThreshold);
    this.defaultCharset =
        (String)
            IntegrationUtils.valueToObject(
                this.obj.getMember("_DiskFileItemFactory__defaultCharset"),
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
        "_DiskFileItemFactory__repository",
        IntegrationUtils.mapToPython(
            repository, idMap, this.obj.getMember("_DiskFileItemFactory__repository")));
    this.obj.invokeMember(
        "__setattr__",
        "_DiskFileItemFactory__sizeThreshold",
        IntegrationUtils.mapToPython(
            sizeThreshold, idMap, this.obj.getMember("_DiskFileItemFactory__sizeThreshold")));
    this.obj.invokeMember(
        "__setattr__",
        "_DiskFileItemFactory__defaultCharset",
        IntegrationUtils.mapToPython(
            defaultCharset, idMap, this.obj.getMember("_DiskFileItemFactory__defaultCharset")));
    return idMap;
  }
}
