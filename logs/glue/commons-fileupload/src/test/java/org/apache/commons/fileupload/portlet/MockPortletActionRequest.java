package org.apache.commons.fileupload.portlet;

import java.io.BufferedReader;
import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.UnsupportedEncodingException;
import java.util.Arrays;
import java.util.Collections;
import java.util.Enumeration;
import java.util.HashMap;
import java.util.Hashtable;
import java.util.Locale;
import java.util.Map;
import org.apache.commons.fileupload.ContextInitializer;
import org.apache.commons.fileupload.ExceptionHandler;
import org.apache.commons.fileupload.FileUploadBase;
import org.apache.commons.fileupload.IntegrationUtils;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public class MockPortletActionRequest {
  private transient Value obj =
      IntegrationUtils.createDefaultPythonObject(
          ContextInitializer.getPythonClass(
              "test/org/apache/commons/fileupload/portlet/MockPortletActionRequest.py",
              "MockPortletActionRequest"));
  public Hashtable<String, Object> attributes = new Hashtable<String, Object>();
  public Map<String, String> parameters = new HashMap<String, String>();
  public String characterEncoding;
  public final int length;
  public final String contentType;
  public InputStream requestData;

  public Value getPythonObject() {
    return obj;
  }

  public void setPythonObject(Value obj) {
    this.obj = obj;
  }

  public void setCharacterEncoding(String characterEncoding) throws UnsupportedEncodingException {

    try {

      this.characterEncoding = characterEncoding;

    } catch (Throwable ExceptionObjectForCaching) {
      ExceptionHandler.ERR = ExceptionObjectForCaching;
      throw ExceptionObjectForCaching;
    }
  }

  public BufferedReader getReader() throws UnsupportedEncodingException, IOException {

    try {

      return null;

    } catch (Throwable ExceptionObjectForCaching) {
      ExceptionHandler.ERR = ExceptionObjectForCaching;
      throw ExceptionObjectForCaching;
    }
  }

  public InputStream getPortletInputStream() throws IOException {

    try {

      return requestData;

    } catch (Throwable ExceptionObjectForCaching) {
      ExceptionHandler.ERR = ExceptionObjectForCaching;
      throw ExceptionObjectForCaching;
    }
  }

  public String getContentType() {

    return contentType;
  }

  public int getContentLength() {

    return length;
  }

  public String getCharacterEncoding() {

    return characterEncoding;
  }

  public void setAttribute(String key, Object value) {

    attributes.put(key, value);
  }

  public void removeAttribute(String key) {

    attributes.remove(key);
  }

  public boolean isUserInRole(String arg0) {

    return false;
  }

  public boolean isSecure() {

    return false;
  }

  public boolean isRequestedSessionIdValid() {

    return false;
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

  public Enumeration getResponseContentTypes() {

    return null;
  }

  public String getResponseContentType() {

    return null;
  }

  public String getRequestedSessionId() {

    return null;
  }

  public String getRemoteUser() {

    return null;
  }

  public Enumeration getPropertyNames() {

    return null;
  }

  public String getProperty(String arg0) {

    return null;
  }

  public Enumeration getProperties(String arg0) {

    return null;
  }

  public String[] getParameterValues(String arg0) {

    return null;
  }

  public Enumeration getParameterNames() {

    return Collections.enumeration(parameters.keySet());
  }

  public Map getParameterMap() {

    return Collections.unmodifiableMap(parameters);
  }

  public String getParameter(String key) {

    return parameters.get(key);
  }

  public Enumeration getLocales() {

    return Collections.enumeration(Arrays.asList(Locale.getAvailableLocales()));
  }

  public Locale getLocale() {

    return Locale.getDefault();
  }

  public String getContextPath() {

    return null;
  }

  public String getAuthType() {

    return null;
  }

  public Enumeration getAttributeNames() {

    return attributes.keys();
  }

  public Object getAttribute(String key) {

    return attributes.get(key);
  }

  public static MockPortletActionRequest MockPortletActionRequest1(
      final byte[] requestData, final String contentType) {

    return new MockPortletActionRequest(
        requestData.length, new ByteArrayInputStream(requestData), contentType);
  }

  public MockPortletActionRequest(
      int requestLength, ByteArrayInputStream byteArrayInputStream, String contentType) {

    this.requestData = byteArrayInputStream;
    length = requestLength;
    this.contentType = contentType;
    attributes.put(FileUploadBase.CONTENT_TYPE, contentType);
  }

  public java.util.Map pyToJ() {
    java.util.Map idMap = new java.util.HashMap();
    return pyToJ(idMap);
  }

  public java.util.Map pyToJ(java.util.Map idMap) {

    this.attributes =
        (Hashtable<String, Object>)
            IntegrationUtils.valueToObject(
                this.obj.getMember("_MockPortletActionRequest__attributes"),
                "Hashtable<String,Object>",
                idMap,
                attributes);
    this.parameters =
        (Map<String, String>)
            IntegrationUtils.valueToObject(
                this.obj.getMember("_MockPortletActionRequest__parameters"),
                "Map<String,String>",
                idMap,
                parameters);
    this.characterEncoding =
        (String)
            IntegrationUtils.valueToObject(
                this.obj.getMember("_MockPortletActionRequest__characterEncoding"),
                "String",
                idMap,
                characterEncoding);
    this.requestData =
        (InputStream)
            IntegrationUtils.valueToObject(
                this.obj.getMember("_MockPortletActionRequest__requestData"),
                "InputStream",
                idMap,
                requestData);
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
        "_MockPortletActionRequest__attributes",
        IntegrationUtils.mapToPython(
            attributes, idMap, this.obj.getMember("_MockPortletActionRequest__attributes")));
    this.obj.invokeMember(
        "__setattr__",
        "_MockPortletActionRequest__parameters",
        IntegrationUtils.mapToPython(
            parameters, idMap, this.obj.getMember("_MockPortletActionRequest__parameters")));
    this.obj.invokeMember(
        "__setattr__",
        "_MockPortletActionRequest__characterEncoding",
        IntegrationUtils.mapToPython(
            characterEncoding,
            idMap,
            this.obj.getMember("_MockPortletActionRequest__characterEncoding")));
    this.obj.invokeMember(
        "__setattr__",
        "_MockPortletActionRequest__length",
        IntegrationUtils.mapToPython(
            length, idMap, this.obj.getMember("_MockPortletActionRequest__length")));
    this.obj.invokeMember(
        "__setattr__",
        "_MockPortletActionRequest__contentType",
        IntegrationUtils.mapToPython(
            contentType, idMap, this.obj.getMember("_MockPortletActionRequest__contentType")));
    this.obj.invokeMember(
        "__setattr__",
        "_MockPortletActionRequest__requestData",
        IntegrationUtils.mapToPython(
            requestData, idMap, this.obj.getMember("_MockPortletActionRequest__requestData")));
    return idMap;
  }
}
