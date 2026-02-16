package org.apache.commons.fileupload.util;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Iterator;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Locale;
import java.util.Map;
import org.apache.commons.fileupload.ContextInitializer;
import org.apache.commons.fileupload.ExceptionHandler;
import org.apache.commons.fileupload.FileItemHeaders;
import org.apache.commons.fileupload.IntegrationUtils;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public class FileItemHeadersImpl implements FileItemHeaders, Serializable {
  private transient Value obj =
      IntegrationUtils.createDefaultPythonObject(
          ContextInitializer.getPythonClass(
              "main/org/apache/commons/fileupload/util/FileItemHeadersImpl.py",
              "FileItemHeadersImpl"));
  public static final long serialVersionUID = -4455695752627032559L;
  public Map<String, List<String>> headerNameToValueListMap =
      new LinkedHashMap<String, List<String>>();

  public Value getPythonObject() {
    return obj;
  }

  public void setPythonObject(Value obj) {
    this.obj = obj;
  }

  @Override
  public Iterator<String> getHeaders(String name) {

    String nameLower = name.toLowerCase(Locale.ENGLISH);
    List<String> headerValueList = headerNameToValueListMap.get(nameLower);
    if (null == headerValueList) {
      headerValueList = Collections.emptyList();
    }
    return headerValueList.iterator();
  }

  @Override
  public Iterator<String> getHeaderNames() {

    return headerNameToValueListMap.keySet().iterator();
  }

  @Override
  public String getHeader(String name) {

    String nameLower = name.toLowerCase(Locale.ENGLISH);
    List<String> headerValueList = headerNameToValueListMap.get(nameLower);
    if (null == headerValueList) {
      return null;
    }
    return headerValueList.get(0);
  }

  public synchronized void addHeader(String name, String value) {

    String nameLower = name.toLowerCase(Locale.ENGLISH);
    List<String> headerValueList = headerNameToValueListMap.get(nameLower);
    if (null == headerValueList) {
      headerValueList = new ArrayList<String>();
      headerNameToValueListMap.put(nameLower, headerValueList);
    }
    headerValueList.add(value);
  }

  public java.util.Map pyToJ() {
    java.util.Map idMap = new java.util.HashMap();
    return pyToJ(idMap);
  }

  public java.util.Map pyToJ(java.util.Map idMap) {

    this.headerNameToValueListMap =
        (Map<String, List<String>>)
            IntegrationUtils.valueToObject(
                this.obj.getMember("_FileItemHeadersImpl__headerNameToValueListMap"),
                "Map<String,List<String>>",
                idMap,
                headerNameToValueListMap);
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
        "_FileItemHeadersImpl__headerNameToValueListMap",
        IntegrationUtils.mapToPython(
            headerNameToValueListMap,
            idMap,
            this.obj.getMember("_FileItemHeadersImpl__headerNameToValueListMap")));
    return idMap;
  }
}
