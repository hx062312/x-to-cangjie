package org.apache.commons.fileupload;

import org.apache.commons.fileupload.ContextInitializer;
import org.apache.commons.fileupload.ExceptionHandler;
import org.apache.commons.fileupload.IntegrationUtils;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public class FileCountLimitExceededException extends FileUploadException {
  private transient Value obj =
      IntegrationUtils.createDefaultPythonObject(
          ContextInitializer.getPythonClass(
              "main/org/apache/commons/fileupload/FileCountLimitExceededException.py",
              "FileCountLimitExceededException"));
  public static final long serialVersionUID = 6904179610227521789L;
  public final long limit;

  public Value getPythonObject() {
    return obj;
  }

  public void setPythonObject(Value obj) {
    this.obj = obj;
  }

  public long getLimit() {

    return limit;
  }

  public FileCountLimitExceededException(final String message, final long limit) {

    super(message, null);
    this.limit = limit;
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
        "_FileCountLimitExceededException__limit",
        IntegrationUtils.mapToPython(
            limit, idMap, this.obj.getMember("_FileCountLimitExceededException__limit")));
    return idMap;
  }
}
