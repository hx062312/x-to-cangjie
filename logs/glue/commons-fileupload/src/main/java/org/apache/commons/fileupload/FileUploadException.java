package org.apache.commons.fileupload;

import java.io.PrintStream;
import java.io.PrintWriter;
import org.apache.commons.fileupload.ContextInitializer;
import org.apache.commons.fileupload.ExceptionHandler;
import org.apache.commons.fileupload.IntegrationUtils;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public class FileUploadException extends Exception {
  private transient Value obj =
      IntegrationUtils.createDefaultPythonObject(
          ContextInitializer.getPythonClass(
              "main/org/apache/commons/fileupload/FileUploadException.py", "FileUploadException"));
  public static final long serialVersionUID = 8881893724388807504L;
  public Throwable cause;

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

  public void printStackTrace1(PrintWriter writer) {

    super.printStackTrace(writer);
    if (cause != null) {
      writer.println("Caused by:");
      cause.printStackTrace(writer);
    }
  }

  public void printStackTrace0(PrintStream stream) {

    super.printStackTrace(stream);
    if (cause != null) {
      stream.println("Caused by:");
      cause.printStackTrace(stream);
    }
  }

  public FileUploadException(String msg, Throwable cause) {

    super(msg);
    this.cause = cause;
  }

  public static FileUploadException FileUploadException1(final String msg) {

    return new FileUploadException(msg, null);
  }

  public static FileUploadException FileUploadException0() {

    return new FileUploadException(null, null);
  }

  public java.util.Map pyToJ() {
    java.util.Map idMap = new java.util.HashMap();
    return pyToJ(idMap);
  }

  public java.util.Map pyToJ(java.util.Map idMap) {

    this.cause =
        (Throwable)
            IntegrationUtils.valueToObject(
                this.obj.getMember("_FileUploadException__cause"), "Throwable", idMap, cause);
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
        "_FileUploadException__cause",
        IntegrationUtils.mapToPython(
            cause, idMap, this.obj.getMember("_FileUploadException__cause")));
    return idMap;
  }
}
