package org.apache.commons.fileupload;

import java.io.File;
import org.apache.commons.fileupload.ContextInitializer;
import org.apache.commons.fileupload.ExceptionHandler;
import org.apache.commons.fileupload.IntegrationUtils;
import org.apache.commons.fileupload.disk.DiskFileItem;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public class DefaultFileItem extends DiskFileItem {
  private transient Value obj =
      IntegrationUtils.createDefaultPythonObject(
          ContextInitializer.getPythonClass(
              "main/org/apache/commons/fileupload/DefaultFileItem.py", "DefaultFileItem"));

  public Value getPythonObject() {
    return obj;
  }

  public void setPythonObject(Value obj) {
    this.obj = obj;
  }

  public DefaultFileItem(
      String fieldName,
      String contentType,
      boolean isFormField,
      String fileName,
      int sizeThreshold,
      File repository) {

    super(fieldName, contentType, isFormField, fileName, sizeThreshold, repository);
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
