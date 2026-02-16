package org.apache.commons.fileupload;

import static java.lang.String.format;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.UnsupportedEncodingException;
import org.apache.commons.fileupload.ContextInitializer;
import org.apache.commons.fileupload.ExceptionHandler;
import org.apache.commons.fileupload.FileUploadBase.FileUploadIOException;
import org.apache.commons.fileupload.IntegrationUtils;
import org.apache.commons.fileupload.util.Closeable;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public class MultipartStream {
  public class ItemInputStream extends InputStream implements Closeable {
    private transient Value obj =
        IntegrationUtils.createDefaultPythonObject(
            ContextInitializer.getPythonClass(
                "main/org/apache/commons/fileupload/MultipartStream.py", "ItemInputStream"));
    public long total;
    public int pad;
    public int pos;
    public boolean closed;
    public static final int BYTE_POSITIVE_OFFSET = 256;

    public Value getPythonObject() {
      return obj;
    }

    public void setPythonObject(Value obj) {
      this.obj = obj;
    }

    @Override
    public boolean isClosed() {

      return closed;
    }

    @Override
    public long skip(long bytes) throws IOException {

      try {

        if (closed) {
          throw new FileItemStream.ItemSkippedException();
        }
        int av = available();
        if (av == 0) {
          av = makeAvailable();
          if (av == 0) {
            return 0;
          }
        }
        long res = Math.min(av, bytes);
        head += res;
        return res;

      } catch (Throwable ExceptionObjectForCaching) {
        ExceptionHandler.ERR = ExceptionObjectForCaching;
        throw ExceptionObjectForCaching;
      }
    }

    @Override
    public int read() throws IOException {

      try {

        return read0();

      } catch (Throwable ExceptionObjectForCaching) {
        ExceptionHandler.ERR = ExceptionObjectForCaching;
        throw ExceptionObjectForCaching;
      }
    }

    @Override
    public int available() throws IOException {

      try {

        if (pos == -1) {
          return tail - head - pad;
        }
        return pos - head;

      } catch (Throwable ExceptionObjectForCaching) {
        ExceptionHandler.ERR = ExceptionObjectForCaching;
        throw ExceptionObjectForCaching;
      }
    }

    public void close1(boolean pCloseUnderlying) throws IOException {

      try {

        if (closed) {
          return;
        }
        if (pCloseUnderlying) {
          closed = true;
          input.close();
        } else {
          for (; ; ) {
            int av = available();
            if (av == 0) {
              av = makeAvailable();
              if (av == 0) {
                break;
              }
            }
            skip(av);
          }
        }
        closed = true;

      } catch (Throwable ExceptionObjectForCaching) {
        ExceptionHandler.ERR = ExceptionObjectForCaching;
        throw ExceptionObjectForCaching;
      }
    }

    public void close0() throws IOException {

      try {

        close1(false);

      } catch (Throwable ExceptionObjectForCaching) {
        ExceptionHandler.ERR = ExceptionObjectForCaching;
        throw ExceptionObjectForCaching;
      }
    }

    public int read1(byte[] b, int off, int len) throws IOException {

      try {

        if (closed) {
          throw new FileItemStream.ItemSkippedException();
        }
        if (len == 0) {
          return 0;
        }
        int res = available();
        if (res == 0) {
          res = makeAvailable();
          if (res == 0) {
            return -1;
          }
        }
        res = Math.min(res, len);
        System.arraycopy(buffer, head, b, off, res);
        head += res;
        total += res;
        return res;

      } catch (Throwable ExceptionObjectForCaching) {
        ExceptionHandler.ERR = ExceptionObjectForCaching;
        throw ExceptionObjectForCaching;
      }
    }

    public int read0() throws IOException {

      try {

        if (closed) {
          throw new FileItemStream.ItemSkippedException();
        }
        if (available() == 0 && makeAvailable() == 0) {
          return -1;
        }
        ++total;
        int b = buffer[head++];
        if (b >= 0) {
          return b;
        }
        return b + BYTE_POSITIVE_OFFSET;

      } catch (Throwable ExceptionObjectForCaching) {
        ExceptionHandler.ERR = ExceptionObjectForCaching;
        throw ExceptionObjectForCaching;
      }
    }

    public long getBytesRead() {

      return total;
    }

    public int makeAvailable() throws IOException {

      try {

        if (pos != -1) {
          return 0;
        }

        total += tail - head - pad;
        System.arraycopy(buffer, tail - pad, buffer, 0, pad);

        head = 0;
        tail = pad;

        for (; ; ) {
          int bytesRead = input.read(buffer, tail, bufSize - tail);
          if (bytesRead == -1) {
            final String msg = "Stream ended unexpectedly";
            throw new MalformedStreamException(msg);
          }
          if (notifier != null) {
            notifier.noteBytesRead(bytesRead);
          }
          tail += bytesRead;

          findSeparator();
          int av = available();

          if (av > 0 || pos != -1) {
            return av;
          }
        }

      } catch (Throwable ExceptionObjectForCaching) {
        ExceptionHandler.ERR = ExceptionObjectForCaching;
        throw ExceptionObjectForCaching;
      }
    }

    public void findSeparator() {

      pos = MultipartStream.this.findSeparator();
      if (pos == -1) {
        if (tail - head > keepRegion) {
          pad = keepRegion;
        } else {
          pad = tail - head;
        }
      }
    }

    public ItemInputStream() {

      findSeparator();
    }

    public java.util.Map pyToJ() {
      java.util.Map idMap = new java.util.HashMap();
      return pyToJ(idMap);
    }

    public java.util.Map pyToJ(java.util.Map idMap) {

      this.total =
          (long)
              IntegrationUtils.valueToObject(
                  this.obj.getMember("_ItemInputStream__total"), "long", idMap, total);
      this.pad =
          (int)
              IntegrationUtils.valueToObject(
                  this.obj.getMember("_ItemInputStream__pad"), "int", idMap, pad);
      this.pos =
          (int)
              IntegrationUtils.valueToObject(
                  this.obj.getMember("_ItemInputStream__pos"), "int", idMap, pos);
      this.closed =
          (boolean)
              IntegrationUtils.valueToObject(
                  this.obj.getMember("_ItemInputStream__closed"), "boolean", idMap, closed);
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
          "_ItemInputStream__total",
          IntegrationUtils.mapToPython(
              total, idMap, this.obj.getMember("_ItemInputStream__total")));
      this.obj.invokeMember(
          "__setattr__",
          "_ItemInputStream__pad",
          IntegrationUtils.mapToPython(pad, idMap, this.obj.getMember("_ItemInputStream__pad")));
      this.obj.invokeMember(
          "__setattr__",
          "_ItemInputStream__pos",
          IntegrationUtils.mapToPython(pos, idMap, this.obj.getMember("_ItemInputStream__pos")));
      this.obj.invokeMember(
          "__setattr__",
          "_ItemInputStream__closed",
          IntegrationUtils.mapToPython(
              closed, idMap, this.obj.getMember("_ItemInputStream__closed")));
      return idMap;
    }
  }

  public static class IllegalBoundaryException extends IOException {
    private transient Value obj =
        IntegrationUtils.createDefaultPythonObject(
            ContextInitializer.getPythonClass(
                "main/org/apache/commons/fileupload/MultipartStream.py",
                "IllegalBoundaryException"));
    public static final long serialVersionUID = -161533165102632918L;

    public Value getPythonObject() {
      return obj;
    }

    public void setPythonObject(Value obj) {
      this.obj = obj;
    }

    public IllegalBoundaryException(String message) {

      super(message);
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

  public static class MalformedStreamException extends IOException {
    private transient Value obj =
        IntegrationUtils.createDefaultPythonObject(
            ContextInitializer.getPythonClass(
                "main/org/apache/commons/fileupload/MultipartStream.py",
                "MalformedStreamException"));
    public static final long serialVersionUID = 6466926458059796677L;

    public Value getPythonObject() {
      return obj;
    }

    public void setPythonObject(Value obj) {
      this.obj = obj;
    }

    public MalformedStreamException(String message) {

      super(message);
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

  public static class ProgressNotifier {
    private transient Value obj =
        IntegrationUtils.createDefaultPythonObject(
            ContextInitializer.getPythonClass(
                "main/org/apache/commons/fileupload/MultipartStream.py", "ProgressNotifier"));
    public ProgressListener listener;
    public final long contentLength;
    public long bytesRead;
    public int items;

    public Value getPythonObject() {
      return obj;
    }

    public void setPythonObject(Value obj) {
      this.obj = obj;
    }

    public void notifyListener() {

      if (listener != null) {
        listener.update(bytesRead, contentLength, items);
      }
    }

    public void noteItem() {

      ++items;
      notifyListener();
    }

    public void noteBytesRead(int pBytes) {

      /* Indicates, that the given number of bytes have been read from
       * the input stream.
       */
      bytesRead += pBytes;
      notifyListener();
    }

    public ProgressNotifier(ProgressListener pListener, long pContentLength) {

      listener = pListener;
      contentLength = pContentLength;
    }

    public java.util.Map pyToJ() {
      java.util.Map idMap = new java.util.HashMap();
      return pyToJ(idMap);
    }

    public java.util.Map pyToJ(java.util.Map idMap) {

      this.listener =
          (ProgressListener)
              IntegrationUtils.valueToObject(
                  this.obj.getMember("_ProgressNotifier__listener"),
                  "ProgressListener",
                  idMap,
                  listener);
      this.bytesRead =
          (long)
              IntegrationUtils.valueToObject(
                  this.obj.getMember("_ProgressNotifier__bytesRead"), "long", idMap, bytesRead);
      this.items =
          (int)
              IntegrationUtils.valueToObject(
                  this.obj.getMember("_ProgressNotifier__items"), "int", idMap, items);
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
          "_ProgressNotifier__listener",
          IntegrationUtils.mapToPython(
              listener, idMap, this.obj.getMember("_ProgressNotifier__listener")));
      this.obj.invokeMember(
          "__setattr__",
          "_ProgressNotifier__contentLength",
          IntegrationUtils.mapToPython(
              contentLength, idMap, this.obj.getMember("_ProgressNotifier__contentLength")));
      this.obj.invokeMember(
          "__setattr__",
          "_ProgressNotifier__bytesRead",
          IntegrationUtils.mapToPython(
              bytesRead, idMap, this.obj.getMember("_ProgressNotifier__bytesRead")));
      this.obj.invokeMember(
          "__setattr__",
          "_ProgressNotifier__items",
          IntegrationUtils.mapToPython(
              items, idMap, this.obj.getMember("_ProgressNotifier__items")));
      return idMap;
    }
  }

  private transient Value obj =
      IntegrationUtils.createDefaultPythonObject(
          ContextInitializer.getPythonClass(
              "main/org/apache/commons/fileupload/MultipartStream.py", "MultipartStream"));
  public static final byte CR = 0x0D;
  public static final byte LF = 0x0A;
  public static final byte DASH = 0x2D;
  public static final int HEADER_PART_SIZE_MAX = 10240;
  public static final int DEFAULT_BUFSIZE = 4096;
  public static final byte[] HEADER_SEPARATOR = {CR, LF, CR, LF};
  public static final byte[] FIELD_SEPARATOR = {CR, LF};
  public static final byte[] STREAM_TERMINATOR = {DASH, DASH};
  public static final byte[] BOUNDARY_PREFIX = {CR, LF, DASH, DASH};
  public InputStream input;
  public int boundaryLength;
  public final int keepRegion;
  public byte[] boundary;
  public int[] boundaryTable;
  public final int bufSize;
  public byte[] buffer;
  public int head;
  public int tail;
  public String headerEncoding;
  public ProgressNotifier notifier;

  public Value getPythonObject() {
    return obj;
  }

  public void setPythonObject(Value obj) {
    this.obj = obj;
  }

  public static MultipartStream MultipartStream3(InputStream input, byte[] boundary) {

    return new MultipartStream(input, boundary, DEFAULT_BUFSIZE, null);
  }

  public static MultipartStream MultipartStream1(InputStream input, byte[] boundary, int bufSize) {

    return new MultipartStream(input, boundary, bufSize, null);
  }

  public static MultipartStream MultipartStream0() {

    return MultipartStream2(null, null, null);
  }

  public int findSeparator() {

    int bufferPos = this.head;
    int tablePos = 0;

    while (bufferPos < this.tail) {
      while (tablePos >= 0 && buffer[bufferPos] != boundary[tablePos]) {
        tablePos = boundaryTable[tablePos];
      }
      bufferPos++;
      tablePos++;
      if (tablePos == boundaryLength) {
        return bufferPos - boundaryLength;
      }
    }
    return -1;
  }

  public int findByte(byte value, int pos) {

    for (int i = pos; i < tail; i++) {
      if (buffer[i] == value) {
        return i;
      }
    }

    return -1;
  }

  public static boolean arrayequals(byte[] a, byte[] b, int count) {

    for (int i = 0; i < count; i++) {
      if (a[i] != b[i]) {
        return false;
      }
    }
    return true;
  }

  public String readHeaders() throws FileUploadIOException, MalformedStreamException {

    try {

      int i = 0;
      byte b;
      ByteArrayOutputStream baos = new ByteArrayOutputStream();
      int size = 0;
      while (i < HEADER_SEPARATOR.length) {
        try {
          b = readByte();
        } catch (FileUploadIOException e) {
          throw e;
        } catch (IOException e) {
          throw new MalformedStreamException("Stream ended unexpectedly");
        }
        if (++size > HEADER_PART_SIZE_MAX) {
          throw new MalformedStreamException(
              format(
                  "Header section has more than %s bytes (maybe it is not properly"
                      + " terminated)",
                  Integer.valueOf(HEADER_PART_SIZE_MAX)));
        }
        if (b == HEADER_SEPARATOR[i]) {
          i++;
        } else {
          i = 0;
        }
        baos.write(b);
      }

      String headers = null;
      if (headerEncoding != null) {
        try {
          headers = baos.toString(headerEncoding);
        } catch (UnsupportedEncodingException e) {
          headers = baos.toString();
        }
      } else {
        headers = baos.toString();
      }

      return headers;

    } catch (Throwable ExceptionObjectForCaching) {
      ExceptionHandler.ERR = ExceptionObjectForCaching;
      throw ExceptionObjectForCaching;
    }
  }

  public void setBoundary(byte[] boundary) throws IllegalBoundaryException {

    try {

      if (boundary.length != boundaryLength - BOUNDARY_PREFIX.length) {
        throw new IllegalBoundaryException("The length of a boundary token cannot be changed");
      }
      System.arraycopy(boundary, 0, this.boundary, BOUNDARY_PREFIX.length, boundary.length);
      computeBoundaryTable();

    } catch (Throwable ExceptionObjectForCaching) {
      ExceptionHandler.ERR = ExceptionObjectForCaching;
      throw ExceptionObjectForCaching;
    }
  }

  public boolean readBoundary() throws FileUploadIOException, MalformedStreamException {

    try {

      byte[] marker = new byte[2];
      boolean nextChunk = false;

      head += boundaryLength;
      try {
        marker[0] = readByte();
        if (marker[0] == LF) {
          return true;
        }

        marker[1] = readByte();
        if (arrayequals(marker, STREAM_TERMINATOR, 2)) {
          nextChunk = false;
        } else if (arrayequals(marker, FIELD_SEPARATOR, 2)) {
          nextChunk = true;
        } else {
          throw new MalformedStreamException("Unexpected characters follow a boundary");
        }
      } catch (FileUploadIOException e) {
        throw e;
      } catch (IOException e) {
        throw new MalformedStreamException("Stream ended unexpectedly");
      }
      return nextChunk;

    } catch (Throwable ExceptionObjectForCaching) {
      ExceptionHandler.ERR = ExceptionObjectForCaching;
      throw ExceptionObjectForCaching;
    }
  }

  public byte readByte() throws IOException {

    try {

      if (head == tail) {
        head = 0;
        tail = input.read(buffer, head, bufSize);
        if (tail == -1) {
          throw new IOException("No more data is available");
        }
        if (notifier != null) {
          notifier.noteBytesRead(tail);
        }
      }
      return buffer[head++];

    } catch (Throwable ExceptionObjectForCaching) {
      ExceptionHandler.ERR = ExceptionObjectForCaching;
      throw ExceptionObjectForCaching;
    }
  }

  public void setHeaderEncoding(String encoding) {

    headerEncoding = encoding;
  }

  public String getHeaderEncoding() {

    return headerEncoding;
  }

  public static MultipartStream MultipartStream2(
      InputStream input, byte[] boundary, ProgressNotifier pNotifier) {

    return new MultipartStream(input, boundary, DEFAULT_BUFSIZE, pNotifier);
  }

  public MultipartStream(
      InputStream input, byte[] boundary, int bufSize, ProgressNotifier pNotifier) {

    try {

      if (boundary == null) {
        throw new IllegalArgumentException("boundary may not be null");
      }
      this.boundaryLength = boundary.length + BOUNDARY_PREFIX.length;
      if (bufSize < this.boundaryLength + 1) {
        throw new IllegalArgumentException(
            "The buffer size specified for the MultipartStream is too small");
      }

      this.input = input;
      this.bufSize = Math.max(bufSize, boundaryLength * 2);
      this.buffer = new byte[this.bufSize];
      this.notifier = pNotifier;

      this.boundary = new byte[this.boundaryLength];
      this.boundaryTable = new int[this.boundaryLength + 1];
      this.keepRegion = this.boundary.length;

      System.arraycopy(BOUNDARY_PREFIX, 0, this.boundary, 0, BOUNDARY_PREFIX.length);
      System.arraycopy(boundary, 0, this.boundary, BOUNDARY_PREFIX.length, boundary.length);
      computeBoundaryTable();

      head = 0;
      tail = 0;

    } catch (Throwable ExceptionObjectForCaching) {
      ExceptionHandler.ERR = ExceptionObjectForCaching;
      throw ExceptionObjectForCaching;
    }
  }

  public void computeBoundaryTable() {

    int position = 2;
    int candidate = 0;

    boundaryTable[0] = -1;
    boundaryTable[1] = 0;

    while (position <= boundaryLength) {
      if (boundary[position - 1] == boundary[candidate]) {
        boundaryTable[position] = candidate + 1;
        candidate++;
        position++;
      } else if (candidate > 0) {
        candidate = boundaryTable[candidate];
      } else {
        boundaryTable[position] = 0;
        position++;
      }
    }
  }

  public ItemInputStream newInputStream() {

    return new ItemInputStream();
  }

  public java.util.Map pyToJ() {
    java.util.Map idMap = new java.util.HashMap();
    return pyToJ(idMap);
  }

  public java.util.Map pyToJ(java.util.Map idMap) {

    this.input =
        (InputStream)
            IntegrationUtils.valueToObject(
                this.obj.getMember("_MultipartStream__input"), "InputStream", idMap, input);
    this.boundaryLength =
        (int)
            IntegrationUtils.valueToObject(
                this.obj.getMember("_MultipartStream__boundaryLength"),
                "int",
                idMap,
                boundaryLength);
    this.boundary =
        (byte[])
            IntegrationUtils.valueToObject(
                this.obj.getMember("_MultipartStream__boundary"),
                "byte[]",
                idMap,
                byte.class,
                boundary);
    this.boundaryTable =
        (int[])
            IntegrationUtils.valueToObject(
                this.obj.getMember("_MultipartStream__boundaryTable"),
                "int[]",
                idMap,
                int.class,
                boundaryTable);
    this.buffer =
        (byte[])
            IntegrationUtils.valueToObject(
                this.obj.getMember("_MultipartStream__buffer"),
                "byte[]",
                idMap,
                byte.class,
                buffer);
    this.head =
        (int)
            IntegrationUtils.valueToObject(
                this.obj.getMember("_MultipartStream__head"), "int", idMap, head);
    this.tail =
        (int)
            IntegrationUtils.valueToObject(
                this.obj.getMember("_MultipartStream__tail"), "int", idMap, tail);
    this.headerEncoding =
        (String)
            IntegrationUtils.valueToObject(
                this.obj.getMember("_MultipartStream__headerEncoding"),
                "String",
                idMap,
                headerEncoding);
    this.notifier =
        (ProgressNotifier)
            IntegrationUtils.valueToObject(
                this.obj.getMember("_MultipartStream__notifier"),
                "ProgressNotifier",
                idMap,
                notifier);
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
        "_MultipartStream__input",
        IntegrationUtils.mapToPython(input, idMap, this.obj.getMember("_MultipartStream__input")));
    this.obj.invokeMember(
        "__setattr__",
        "_MultipartStream__boundaryLength",
        IntegrationUtils.mapToPython(
            boundaryLength, idMap, this.obj.getMember("_MultipartStream__boundaryLength")));
    this.obj.invokeMember(
        "__setattr__",
        "_MultipartStream__keepRegion",
        IntegrationUtils.mapToPython(
            keepRegion, idMap, this.obj.getMember("_MultipartStream__keepRegion")));
    this.obj.invokeMember(
        "__setattr__",
        "_MultipartStream__boundary",
        IntegrationUtils.mapToPython(
            boundary, idMap, this.obj.getMember("_MultipartStream__boundary")));
    this.obj.invokeMember(
        "__setattr__",
        "_MultipartStream__boundaryTable",
        IntegrationUtils.mapToPython(
            boundaryTable, idMap, this.obj.getMember("_MultipartStream__boundaryTable")));
    this.obj.invokeMember(
        "__setattr__",
        "_MultipartStream__bufSize",
        IntegrationUtils.mapToPython(
            bufSize, idMap, this.obj.getMember("_MultipartStream__bufSize")));
    this.obj.invokeMember(
        "__setattr__",
        "_MultipartStream__buffer",
        IntegrationUtils.mapToPython(
            buffer, idMap, this.obj.getMember("_MultipartStream__buffer")));
    this.obj.invokeMember(
        "__setattr__",
        "_MultipartStream__head",
        IntegrationUtils.mapToPython(head, idMap, this.obj.getMember("_MultipartStream__head")));
    this.obj.invokeMember(
        "__setattr__",
        "_MultipartStream__tail",
        IntegrationUtils.mapToPython(tail, idMap, this.obj.getMember("_MultipartStream__tail")));
    this.obj.invokeMember(
        "__setattr__",
        "_MultipartStream__headerEncoding",
        IntegrationUtils.mapToPython(
            headerEncoding, idMap, this.obj.getMember("_MultipartStream__headerEncoding")));
    this.obj.invokeMember(
        "__setattr__",
        "_MultipartStream__notifier",
        IntegrationUtils.mapToPython(
            notifier, idMap, this.obj.getMember("_MultipartStream__notifier")));
    return idMap;
  }
}
