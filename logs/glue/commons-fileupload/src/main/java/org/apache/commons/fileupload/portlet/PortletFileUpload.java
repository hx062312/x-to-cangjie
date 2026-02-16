package org.apache.commons.fileupload.portlet;

import org.apache.commons.fileupload.ContextInitializer;
import org.apache.commons.fileupload.ExceptionHandler;
import org.apache.commons.fileupload.FileItemFactory;
import org.apache.commons.fileupload.FileUpload;
import org.apache.commons.fileupload.IntegrationUtils;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public class PortletFileUpload extends FileUpload {
  private transient Value obj =
      IntegrationUtils.createDefaultPythonObject(
          ContextInitializer.getPythonClass(
              "main/org/apache/commons/fileupload/portlet/PortletFileUpload.py",
              "PortletFileUpload"));

  public Value getPythonObject() {
    return obj;
  }

  public void setPythonObject(Value obj) {
    this.obj = obj;
  }

  public static PortletFileUpload PortletFileUpload1() {

    return new PortletFileUpload(null);
  }

  public PortletFileUpload(FileItemFactory fileItemFactory) {

    super(0, fileItemFactory);
  }

  public java.util.Map pyToJ() {
    java.util.Map idMap = new java.util.HashMap();
    return pyToJ(idMap);
  }

  public java.util.Map pyToJ(java.util.Map idMap) {
    super.pyToJ(idMap);

    return idMap;
  }

  public Value jToPy() {
    Value idMap = IntegrationUtils.mapToPython(new java.util.HashMap());
    return jToPy(idMap);
  }

  public Value jToPy(Value idMap) {
    super.jToPy(idMap);
    this.obj.invokeMember("__setattr__", "javaObj", this);

    return idMap;
  }
}
