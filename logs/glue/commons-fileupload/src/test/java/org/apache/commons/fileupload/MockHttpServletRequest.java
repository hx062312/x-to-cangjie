package org.apache.commons.fileupload;

import java.io.BufferedReader;
import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.UnsupportedEncodingException;
import java.util.Enumeration;
import java.util.Locale;
import java.util.Map;
import org.apache.commons.fileupload.ContextInitializer;
import org.apache.commons.fileupload.ExceptionHandler;
import org.apache.commons.fileupload.IntegrationUtils;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public class MockHttpServletRequest {
  public static class MyServletInputStream {
    private transient Value obj =
        IntegrationUtils.createDefaultPythonObject(
            ContextInitializer.getPythonClass(
                "test/org/apache/commons/fileupload/MockHttpServletRequest.py",
                "MyServletInputStream"));
    public InputStream in;
    public final int readLimit;

    public Value getPythonObject() {
      return obj;
    }

    public void setPythonObject(Value obj) {
      this.obj = obj;
    }

    public int read1(byte b[], int off, int len) throws IOException {

      try {

        if (readLimit > 0) {
          return in.read(b, off, Math.min(readLimit, len));
        }
        return in.read(b, off, len);

      } catch (Throwable ExceptionObjectForCaching) {
        ExceptionHandler.ERR = ExceptionObjectForCaching;
        throw ExceptionObjectForCaching;
      }
    }

    public int read0() throws IOException {

      try {

        return in.read();

      } catch (Throwable ExceptionObjectForCaching) {
        ExceptionHandler.ERR = ExceptionObjectForCaching;
        throw ExceptionObjectForCaching;
      }
    }

    public MyServletInputStream(InputStream pStream, int readLimit) {

      in = pStream;
      this.readLimit = readLimit;
    }

    public java.util.Map pyToJ() {
      java.util.Map idMap = new java.util.HashMap();
      return pyToJ(idMap);
    }

    public java.util.Map pyToJ(java.util.Map idMap) {

      this.in =
          (InputStream)
              IntegrationUtils.valueToObject(
                  this.obj.getMember("_MyServletInputStream__in"), "InputStream", idMap, in);
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
          "_MyServletInputStream__in",
          IntegrationUtils.mapToPython(in, idMap, this.obj.getMember("_MyServletInputStream__in")));
      this.obj.invokeMember(
          "__setattr__",
          "_MyServletInputStream__readLimit",
          IntegrationUtils.mapToPython(
              readLimit, idMap, this.obj.getMember("_MyServletInputStream__readLimit")));
      return idMap;
    }
  }

  private transient Value obj =
      IntegrationUtils.createDefaultPythonObject(
          ContextInitializer.getPythonClass(
              "test/org/apache/commons/fileupload/MockHttpServletRequest.py",
              "MockHttpServletRequest"));
  public InputStream m_requestData;
  public long length;
  public final String m_strContentType;
  public int readLimit = -1;
  public Map<String, String> m_headers = new java.util.HashMap<String, String>();

  public Value getPythonObject() {
    return obj;
  }

  public void setPythonObject(Value obj) {
    this.obj = obj;
  }

  public String getRealPath(String arg0) {

    return null;
  }

  public String getLocalAddr() {

    return null;
  }

  public int getRemotePort() {

    return 0;
  }

  public int getLocalPort() {

    return 0;
  }

  public String getLocalName() {

    return null;
  }

  public boolean isRequestedSessionIdFromUrl() {

    return false;
  }

  public boolean isSecure() {

    return false;
  }

  public Enumeration<Locale> getLocales() {

    return null;
  }

  public Locale getLocale() {

    return null;
  }

  public void removeAttribute(String arg0) {}

  public void setAttribute(String arg0, Object arg1) {}

  public String getRemoteHost() {

    return null;
  }

  public String getRemoteAddr() {

    return null;
  }

  public BufferedReader getReader() throws IOException {

    try {

      return null;

    } catch (Throwable ExceptionObjectForCaching) {
      ExceptionHandler.ERR = ExceptionObjectForCaching;
      throw ExceptionObjectForCaching;
    }
  }

  public int getServerPort() {

    return 0;
  }

  public String getServerName() {

    return null;
  }

  public String getScheme() {

    return null;
  }

  public String getProtocol() {

    return null;
  }

  public Map<String, String[]> getParameterMap() {

    return null;
  }

  public String[] getParameterValues(String arg0) {

    return null;
  }

  public Enumeration<String> getParameterNames() {

    return null;
  }

  public String getParameter(String arg0) {

    return null;
  }

  public void setReadLimit(int readLimit) {

    this.readLimit = readLimit;
  }

  public String getContentType() {

    return m_strContentType;
  }

  public void setContentLength(long length) {

    this.length = length;
  }

  public int getContentLength() {

    try {

      int iLength = 0;

      if (null == m_requestData) {
        iLength = -1;
      } else {
        if (length > Integer.MAX_VALUE) {
          throw new RuntimeException("Value '" + length + "' is too large to be converted to int");
        }
        iLength = (int) length;
      }
      return iLength;

    } catch (Throwable ExceptionObjectForCaching) {
      ExceptionHandler.ERR = ExceptionObjectForCaching;
      throw ExceptionObjectForCaching;
    }
  }

  public void setCharacterEncoding(String arg0) throws UnsupportedEncodingException {

    try {

    } catch (Throwable ExceptionObjectForCaching) {
      ExceptionHandler.ERR = ExceptionObjectForCaching;
      throw ExceptionObjectForCaching;
    }
  }

  public String getCharacterEncoding() {

    return null;
  }

  public Enumeration<String> getAttributeNames() {

    return null;
  }

  public Object getAttribute(String arg0) {

    return null;
  }

  public boolean isRequestedSessionIdFromURL() {

    return false;
  }

  public boolean isRequestedSessionIdFromCookie() {

    return false;
  }

  public boolean isRequestedSessionIdValid() {

    return false;
  }

  public String getServletPath() {

    return null;
  }

  public StringBuffer getRequestURL() {

    return null;
  }

  public String getRequestURI() {

    return null;
  }

  public String getRequestedSessionId() {

    return null;
  }

  public boolean isUserInRole(String arg0) {

    return false;
  }

  public String getRemoteUser() {

    return null;
  }

  public String getQueryString() {

    return null;
  }

  public String getContextPath() {

    return null;
  }

  public String getPathTranslated() {

    return null;
  }

  public String getPathInfo() {

    return null;
  }

  public String getMethod() {

    return null;
  }

  public Enumeration<String> getHeaderNames() {

    return null;
  }

  public Enumeration<String> getHeaders(String arg0) {

    return null;
  }

  public String getHeader(String headerName) {

    return m_headers.get(headerName);
  }

  public long getDateHeader(String arg0) {

    return 0;
  }

  public String getAuthType() {

    return null;
  }

  public static MockHttpServletRequest MockHttpServletRequest1(
      final byte[] requestData, final String strContentType) {

    return new MockHttpServletRequest(
        0, new ByteArrayInputStream(requestData), strContentType, requestData.length);
  }

  public MockHttpServletRequest(
      int constructorId,
      final InputStream requestData,
      final String strContentType,
      final long requestLength) {

    if (constructorId == 0) {
      m_requestData = requestData;
      length = requestLength;
      m_strContentType = strContentType;
      m_headers.put(FileUploadBase.CONTENT_TYPE, strContentType);
    } else {
      m_requestData = requestData;
      length = requestLength;
      m_strContentType = strContentType;
      m_headers.put(FileUploadBase.CONTENT_TYPE, strContentType);
    }
  }

  public java.util.Map pyToJ() {
    java.util.Map idMap = new java.util.HashMap();
    return pyToJ(idMap);
  }

  public java.util.Map pyToJ(java.util.Map idMap) {

    this.m_requestData =
        (InputStream)
            IntegrationUtils.valueToObject(
                this.obj.getMember("_MockHttpServletRequest__m_requestData"),
                "InputStream",
                idMap,
                m_requestData);
    this.length =
        (long)
            IntegrationUtils.valueToObject(
                this.obj.getMember("_MockHttpServletRequest__length"), "long", idMap, length);
    this.readLimit =
        (int)
            IntegrationUtils.valueToObject(
                this.obj.getMember("_MockHttpServletRequest__readLimit"), "int", idMap, readLimit);
    this.m_headers =
        (Map<String, String>)
            IntegrationUtils.valueToObject(
                this.obj.getMember("_MockHttpServletRequest__m_headers"),
                "Map<String,String>",
                idMap,
                m_headers);
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
        "_MockHttpServletRequest__m_requestData",
        IntegrationUtils.mapToPython(
            m_requestData, idMap, this.obj.getMember("_MockHttpServletRequest__m_requestData")));
    this.obj.invokeMember(
        "__setattr__",
        "_MockHttpServletRequest__length",
        IntegrationUtils.mapToPython(
            length, idMap, this.obj.getMember("_MockHttpServletRequest__length")));
    this.obj.invokeMember(
        "__setattr__",
        "_MockHttpServletRequest__m_strContentType",
        IntegrationUtils.mapToPython(
            m_strContentType,
            idMap,
            this.obj.getMember("_MockHttpServletRequest__m_strContentType")));
    this.obj.invokeMember(
        "__setattr__",
        "_MockHttpServletRequest__readLimit",
        IntegrationUtils.mapToPython(
            readLimit, idMap, this.obj.getMember("_MockHttpServletRequest__readLimit")));
    this.obj.invokeMember(
        "__setattr__",
        "_MockHttpServletRequest__m_headers",
        IntegrationUtils.mapToPython(
            m_headers, idMap, this.obj.getMember("_MockHttpServletRequest__m_headers")));
    return idMap;
  }
}
