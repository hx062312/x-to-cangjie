package org.apache.commons.fileupload;

import org.apache.commons.fileupload.ContextInitializer;
import org.apache.commons.fileupload.ExceptionHandler;
import org.apache.commons.fileupload.IntegrationUtils;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public class InvalidFileNameException extends RuntimeException {
  private transient Value obj =
      IntegrationUtils.createDefaultPythonObject(
          ContextInitializer.getPythonClass(
              "main/org/apache/commons/fileupload/InvalidFileNameException.py",
              "InvalidFileNameException"));
  public static final long serialVersionUID = 7922042602454350470L;
  public final String name;

  public Value getPythonObject() {
    return obj;
  }

  public void setPythonObject(Value obj) {
    this.obj = obj;
  }

  public String getName() {

    return name;
  }

  public InvalidFileNameException(String pName, String pMessage) {

    super(pMessage);
    name = pName;
  }

  public java.util.Map pyToJ() {
    java.util.Map idMap = new java.util.HashMap();
    return pyToJ(idMap);
  }

  public java.util.Map pyToJ(java.util.Map idMap) {

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
        "_InvalidFileNameException__name",
        IntegrationUtils.mapToPython(
            name, idMap, this.obj.getMember("_InvalidFileNameException__name")));
    return idMap;
  }
}
