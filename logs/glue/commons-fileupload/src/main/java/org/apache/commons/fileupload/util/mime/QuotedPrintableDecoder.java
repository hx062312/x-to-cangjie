package org.apache.commons.fileupload.util.mime;

import java.io.IOException;
import java.io.OutputStream;
import org.apache.commons.fileupload.ContextInitializer;
import org.apache.commons.fileupload.ExceptionHandler;
import org.apache.commons.fileupload.IntegrationUtils;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public final class QuotedPrintableDecoder {
  private transient Value obj =
      IntegrationUtils.createDefaultPythonObject(
          ContextInitializer.getPythonClass(
              "main/org/apache/commons/fileupload/util/mime/QuotedPrintableDecoder.py",
              "QuotedPrintableDecoder"));
  public static final int UPPER_NIBBLE_SHIFT = Byte.SIZE / 2;

  public Value getPythonObject() {
    return obj;
  }

  public void setPythonObject(Value obj) {
    this.obj = obj;
  }

  public static int decode(byte[] data, OutputStream out) throws IOException {
    //
    // int off = 0;
    // int length = data.length;
    // int endOffset = off + length;
    // int bytesWritten = 0;
    //
    // while (off < endOffset) {
    // byte ch = data[off++];
    //
    // if (ch == '_') {
    // out.write(' ');
    // } else if (ch == '=') {
    // if (off + 1 >= endOffset) {
    // throw new IOException(
    // "Invalid quoted printable encoding; truncated escape sequence");
    // }
    //
    // byte b1 = data[off++];
    // byte b2 = data[off++];
    //
    // if (b1 == '\r') {
    // if (b2 != '\n') {
    // throw new IOException(
    // "Invalid quoted printable encoding; CR must be followed by LF");
    // }
    // } else {
    // int c1 = hexToBinary(b1);
    // int c2 = hexToBinary(b2);
    // out.write((c1 << UPPER_NIBBLE_SHIFT) | c2);
    // bytesWritten++;
    // }
    // } else {
    // out.write(ch);
    // bytesWritten++;
    // }
    // }
    //
    // return bytesWritten;
    //

    Value idMapJToPy = IntegrationUtils.mapToPython(new java.util.HashMap());
    Value translatedArg0 = IntegrationUtils.mapToPython(data, idMapJToPy);
    Value translatedArg1 = IntegrationUtils.mapToPython(out, idMapJToPy);
    java.util.Map idMapPyToJ = new java.util.HashMap();
    try {
      int val =
          (int)
              IntegrationUtils.valueToObject(
                  ContextInitializer.getPythonClass(
                          "main/org/apache/commons/fileupload/util/mime/QuotedPrintableDecoder.py",
                          "QuotedPrintableDecoder")
                      .invokeMember("decode", translatedArg0, translatedArg1),
                  "int",
                  idMapPyToJ);
      return val;
    } catch (PolyglotException e) {
      throw (IOException) ExceptionHandler.handle(e, "QuotedPrintableDecoder.decode");
    } finally {
      IntegrationUtils.valueToObject(translatedArg0, "byte[]", idMapPyToJ, byte.class, data);
      IntegrationUtils.valueToObject(translatedArg1, "OutputStream", idMapPyToJ, out);
    }
  }

  public static int hexToBinary(final byte b) throws IOException {

    try {

      final int i = Character.digit((char) b, 16);
      if (i == -1) {
        throw new IOException("Invalid quoted printable encoding: not a valid hex digit: " + b);
      }
      return i;

    } catch (Throwable ExceptionObjectForCaching) {
      ExceptionHandler.ERR = ExceptionObjectForCaching;
      throw ExceptionObjectForCaching;
    }
  }

  public QuotedPrintableDecoder() {}

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
