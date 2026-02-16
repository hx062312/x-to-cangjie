package org.apache.commons.fileupload;

import java.io.IOException;
import java.io.InputStream;
import org.apache.commons.fileupload.ContextInitializer;
import org.apache.commons.fileupload.ExceptionHandler;
import org.apache.commons.fileupload.IntegrationUtils;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public interface FileItemStream extends FileItemHeadersSupport {
  public class ItemSkippedException extends IOException {
    private transient Value obj =
        IntegrationUtils.createDefaultPythonObject(
            ContextInitializer.getPythonClass(
                "main/org/apache/commons/fileupload/FileItemStream.py", "ItemSkippedException"));
    public static final long serialVersionUID = -7280778431581963740L;

    public Value getPythonObject() {
      return obj;
    }

    public void setPythonObject(Value obj) {
      this.obj = obj;
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

      return idMap;
    }
  }

  boolean isFormField();

  String getFieldName();

  String getName();

  String getContentType();

  InputStream openStream() throws IOException;
}
