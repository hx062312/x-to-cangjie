package org.apache.commons.fileupload;

import org.apache.commons.fileupload.ContextInitializer;
import org.apache.commons.fileupload.ExceptionHandler;
import org.apache.commons.fileupload.IntegrationUtils;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public class FileUpload extends FileUploadBase {
  private transient Value obj =
      IntegrationUtils.createDefaultPythonObject(
          ContextInitializer.getPythonClass(
              "main/org/apache/commons/fileupload/FileUpload.py", "FileUpload"));
  public FileItemFactory fileItemFactory;

  public Value getPythonObject() {
    return obj;
  }

  public void setPythonObject(Value obj) {
    this.obj = obj;
  }

  @Override
  public void setFileItemFactory(FileItemFactory factory) {

    this.fileItemFactory = factory;
  }

  @Override
  public FileItemFactory getFileItemFactory() {

    return fileItemFactory;
  }

  public FileUpload(int constructorId, FileItemFactory fileItemFactory) {

    super();
    if (constructorId == 1) {
      this.fileItemFactory = fileItemFactory;
    }
  }

  public java.util.Map pyToJ() {
    java.util.Map idMap = new java.util.HashMap();
    return pyToJ(idMap);
  }

  public java.util.Map pyToJ(java.util.Map idMap) {
    super.pyToJ(idMap);
    this.fileItemFactory =
        (FileItemFactory)
            IntegrationUtils.valueToObject(
                this.obj.getMember("_FileUpload__fileItemFactory"),
                "FileItemFactory",
                idMap,
                fileItemFactory);
    return idMap;
  }

  public Value jToPy() {
    Value idMap = IntegrationUtils.mapToPython(new java.util.HashMap());
    return jToPy(idMap);
  }

  public Value jToPy(Value idMap) {
    super.jToPy(idMap);
    this.obj.invokeMember("__setattr__", "javaObj", this);
    this.obj.invokeMember(
        "__setattr__",
        "_FileUpload__fileItemFactory",
        IntegrationUtils.mapToPython(
            fileItemFactory, idMap, this.obj.getMember("_FileUpload__fileItemFactory")));
    return idMap;
  }
}
