package org.apache.commons.fileupload.util;

import java.io.FilterInputStream;
import java.io.IOException;
import java.io.InputStream;
import org.apache.commons.fileupload.ContextInitializer;
import org.apache.commons.fileupload.ExceptionHandler;
import org.apache.commons.fileupload.IntegrationUtils;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public abstract class LimitedInputStream extends FilterInputStream implements Closeable {
  private transient Value obj =
      IntegrationUtils.createDefaultPythonObject(
          ContextInitializer.getPythonClass(
              "main/org/apache/commons/fileupload/util/LimitedInputStream.py",
              "LimitedInputStream"));
  public final long sizeMax;
  public long count;
  public boolean closed;

  public Value getPythonObject() {
    return obj;
  }

  public void setPythonObject(Value obj) {
    this.obj = obj;
  }

  @Override
  public void close() throws IOException {

    try {

      closed = true;
      super.close();

    } catch (Throwable ExceptionObjectForCaching) {
      ExceptionHandler.ERR = ExceptionObjectForCaching;
      throw ExceptionObjectForCaching;
    }
  }

  @Override
  public boolean isClosed() throws IOException {

    try {

      return closed;

    } catch (Throwable ExceptionObjectForCaching) {
      ExceptionHandler.ERR = ExceptionObjectForCaching;
      throw ExceptionObjectForCaching;
    }
  }

  public int read1(byte[] b, int off, int len) throws IOException {

    try {

      int res = super.read(b, off, len);
      if (res > 0) {
        count += res;
        checkLimit();
      }
      return res;

    } catch (Throwable ExceptionObjectForCaching) {
      ExceptionHandler.ERR = ExceptionObjectForCaching;
      throw ExceptionObjectForCaching;
    }
  }

  public int read0() throws IOException {

    try {

      int res = super.read();
      if (res != -1) {
        count++;
        checkLimit();
      }
      return res;

    } catch (Throwable ExceptionObjectForCaching) {
      ExceptionHandler.ERR = ExceptionObjectForCaching;
      throw ExceptionObjectForCaching;
    }
  }

  public LimitedInputStream(InputStream inputStream, long pSizeMax) {

    super(inputStream);
    sizeMax = pSizeMax;
  }

  public void checkLimit() throws IOException {

    try {

      if (count > sizeMax) {
        raiseError(sizeMax, count);
      }

    } catch (Throwable ExceptionObjectForCaching) {
      ExceptionHandler.ERR = ExceptionObjectForCaching;
      throw ExceptionObjectForCaching;
    }
  }

  protected abstract void raiseError(long pSizeMax, long pCount) throws IOException;

  public java.util.Map pyToJ() {
    java.util.Map idMap = new java.util.HashMap();
    return pyToJ(idMap);
  }

  public java.util.Map pyToJ(java.util.Map idMap) {

    this.count =
        (long)
            IntegrationUtils.valueToObject(
                this.obj.getMember("_LimitedInputStream__count"), "long", idMap, count);
    this.closed =
        (boolean)
            IntegrationUtils.valueToObject(
                this.obj.getMember("_LimitedInputStream__closed"), "boolean", idMap, closed);
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
        "_LimitedInputStream__sizeMax",
        IntegrationUtils.mapToPython(
            sizeMax, idMap, this.obj.getMember("_LimitedInputStream__sizeMax")));
    this.obj.invokeMember(
        "__setattr__",
        "_LimitedInputStream__count",
        IntegrationUtils.mapToPython(
            count, idMap, this.obj.getMember("_LimitedInputStream__count")));
    this.obj.invokeMember(
        "__setattr__",
        "_LimitedInputStream__closed",
        IntegrationUtils.mapToPython(
            closed, idMap, this.obj.getMember("_LimitedInputStream__closed")));
    return idMap;
  }
}
