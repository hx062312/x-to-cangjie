package org.apache.commons.fileupload.util.mime;

import java.io.IOException;
import java.io.OutputStream;
import org.apache.commons.fileupload.ContextInitializer;
import org.apache.commons.fileupload.ExceptionHandler;
import org.apache.commons.fileupload.IntegrationUtils;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public final class Base64Decoder {
  private transient Value obj =
      IntegrationUtils.createDefaultPythonObject(
          ContextInitializer.getPythonClass(
              "main/org/apache/commons/fileupload/util/mime/Base64Decoder.py", "Base64Decoder"));
  public static final int INVALID_BYTE = -1; // must be outside range 0-63
  public static final int PAD_BYTE = -2; // must be outside range 0-63
  public static final int MASK_BYTE_UNSIGNED = 0xFF;
  public static final int INPUT_BYTES_PER_CHUNK = 4;
  public static final byte[] ENCODING_TABLE = {
    (byte) 'A',
    (byte) 'B',
    (byte) 'C',
    (byte) 'D',
    (byte) 'E',
    (byte) 'F',
    (byte) 'G',
    (byte) 'H',
    (byte) 'I',
    (byte) 'J',
    (byte) 'K',
    (byte) 'L',
    (byte) 'M',
    (byte) 'N',
    (byte) 'O',
    (byte) 'P',
    (byte) 'Q',
    (byte) 'R',
    (byte) 'S',
    (byte) 'T',
    (byte) 'U',
    (byte) 'V',
    (byte) 'W',
    (byte) 'X',
    (byte) 'Y',
    (byte) 'Z',
    (byte) 'a',
    (byte) 'b',
    (byte) 'c',
    (byte) 'd',
    (byte) 'e',
    (byte) 'f',
    (byte) 'g',
    (byte) 'h',
    (byte) 'i',
    (byte) 'j',
    (byte) 'k',
    (byte) 'l',
    (byte) 'm',
    (byte) 'n',
    (byte) 'o',
    (byte) 'p',
    (byte) 'q',
    (byte) 'r',
    (byte) 's',
    (byte) 't',
    (byte) 'u',
    (byte) 'v',
    (byte) 'w',
    (byte) 'x',
    (byte) 'y',
    (byte) 'z',
    (byte) '0',
    (byte) '1',
    (byte) '2',
    (byte) '3',
    (byte) '4',
    (byte) '5',
    (byte) '6',
    (byte) '7',
    (byte) '8',
    (byte) '9',
    (byte) '+',
    (byte) '/'
  };
  public static final byte PADDING = (byte) '=';
  public static final byte[] DECODING_TABLE = new byte[Byte.MAX_VALUE - Byte.MIN_VALUE + 1];

  static {
    for (int i = 0; i < DECODING_TABLE.length; i++) {
      DECODING_TABLE[i] = INVALID_BYTE;
    }
    for (int i = 0; i < ENCODING_TABLE.length; i++) {
      DECODING_TABLE[ENCODING_TABLE[i]] = (byte) i;
    }
    DECODING_TABLE[PADDING] = PAD_BYTE;
  }

  public Value getPythonObject() {
    return obj;
  }

  public void setPythonObject(Value obj) {
    this.obj = obj;
  }

  public static int decode(byte[] data, OutputStream out) throws IOException {

    try {

      int outLen = 0;
      byte[] cache = new byte[INPUT_BYTES_PER_CHUNK];
      int cachedBytes = 0;

      for (byte b : data) {
        final byte d = DECODING_TABLE[MASK_BYTE_UNSIGNED & b];
        if (d == INVALID_BYTE) {
          continue; // Ignore invalid bytes
        }
        cache[cachedBytes++] = d;
        if (cachedBytes == INPUT_BYTES_PER_CHUNK) {
          final byte b1 = cache[0];
          final byte b2 = cache[1];
          final byte b3 = cache[2];
          final byte b4 = cache[3];
          if (b1 == PAD_BYTE || b2 == PAD_BYTE) {
            throw new IOException(
                "Invalid Base64 input: incorrect padding, first two bytes cannot be" + " padding");
          }
          out.write((b1 << 2) | (b2 >> 4)); // 6 bits of b1 plus 2 bits of b2
          outLen++;
          if (b3 != PAD_BYTE) {
            out.write((b2 << 4) | (b3 >> 2)); // 4 bits of b2 plus 4 bits of b3
            outLen++;
            if (b4 != PAD_BYTE) {
              out.write((b3 << 6) | b4); // 2 bits of b3 plus 6 bits of b4
              outLen++;
            }
          } else if (b4 != PAD_BYTE) { // if byte 3 is pad, byte 4 must be pad too
            throw new // line wrap to avoid 120 char limit
            IOException(
                "Invalid Base64 input: incorrect padding, 4th byte must be padding if"
                    + " 3rd byte is");
          }
          cachedBytes = 0;
        }
      }
      if (cachedBytes != 0) {
        throw new IOException("Invalid Base64 input: truncated");
      }
      return outLen;

    } catch (Throwable ExceptionObjectForCaching) {
      ExceptionHandler.ERR = ExceptionObjectForCaching;
      throw ExceptionObjectForCaching;
    }
  }

  public Base64Decoder() {}

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
