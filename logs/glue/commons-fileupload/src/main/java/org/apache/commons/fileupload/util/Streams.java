package org.apache.commons.fileupload.util;

import java.io.InputStream;
import java.io.OutputStream;
import org.apache.commons.fileupload.ContextInitializer;
import org.apache.commons.fileupload.ExceptionHandler;
import org.apache.commons.fileupload.IntegrationUtils;
import org.apache.commons.fileupload.InvalidFileNameException;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public final class Streams {
  private transient Value obj =
      IntegrationUtils.createDefaultPythonObject(
          ContextInitializer.getPythonClass(
              "main/org/apache/commons/fileupload/util/Streams.py", "Streams"));
  public static final int DEFAULT_BUFFER_SIZE = 8192;

  public Value getPythonObject() {
    return obj;
  }

  public void setPythonObject(Value obj) {
    this.obj = obj;
  }

  public static String checkFileName(String fileName) {

    try {

      if (fileName != null && fileName.indexOf('\u0000') != -1) {
        final StringBuilder sb = new StringBuilder();
        for (int i = 0; i < fileName.length(); i++) {
          char c = fileName.charAt(i);
          switch (c) {
            case 0:
              sb.append("\\0");
              break;
            default:
              sb.append(c);
              break;
          }
        }
        throw new InvalidFileNameException(fileName, "Invalid file name: " + sb);
      }
      return fileName;

    } catch (Throwable ExceptionObjectForCaching) {
      ExceptionHandler.ERR = ExceptionObjectForCaching;
      throw ExceptionObjectForCaching;
    }
  }

  public Streams() {}

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

    return idMap;
  }
}
