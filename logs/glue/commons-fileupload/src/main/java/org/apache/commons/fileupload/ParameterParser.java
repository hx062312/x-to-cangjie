package org.apache.commons.fileupload;

import java.io.UnsupportedEncodingException;
import java.util.HashMap;
import java.util.Locale;
import java.util.Map;
import org.apache.commons.fileupload.ContextInitializer;
import org.apache.commons.fileupload.ExceptionHandler;
import org.apache.commons.fileupload.IntegrationUtils;
import org.apache.commons.fileupload.util.mime.MimeUtility;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public class ParameterParser {
  private transient Value obj =
      IntegrationUtils.createDefaultPythonObject(
          ContextInitializer.getPythonClass(
              "main/org/apache/commons/fileupload/ParameterParser.py", "ParameterParser"));
  public char[] chars = null;
  public int pos = 0;
  public int len = 0;
  public int i1 = 0;
  public int i2 = 0;
  public boolean lowerCaseNames = false;

  public Value getPythonObject() {
    return obj;
  }

  public void setPythonObject(Value obj) {
    this.obj = obj;
  }

  public Map<String, String> parse3(
      final char[] charArray, int offset, int length, char separator) {

    if (charArray == null) {
      return new HashMap<String, String>();
    }
    HashMap<String, String> params = new HashMap<String, String>();
    this.chars = charArray;
    this.pos = offset;
    this.len = length;

    String paramName = null;
    String paramValue = null;
    while (hasChar()) {
      paramName = parseToken(new char[] {'=', separator});
      paramValue = null;
      if (hasChar() && (charArray[pos] == '=')) {
        pos++; // skip '='
        paramValue = parseQuotedToken(new char[] {separator});

        if (paramValue != null) {
          try {
            paramValue = MimeUtility.decodeText(paramValue);
          } catch (UnsupportedEncodingException e) {
          }
        }
      }
      if (hasChar() && (charArray[pos] == separator)) {
        pos++; // skip separator
      }
      if ((paramName != null) && (paramName.length() > 0)) {
        if (this.lowerCaseNames) {
          paramName = paramName.toLowerCase(Locale.ENGLISH);
        }

        params.put(paramName, paramValue);
      }
    }
    return params;
  }

  public Map<String, String> parse2(final char[] charArray, char separator) {

    if (charArray == null) {
      return new HashMap<String, String>();
    }
    return parse3(charArray, 0, charArray.length, separator);
  }

  public Map<String, String> parse1(final String str, char separator) {

    if (str == null) {
      return new HashMap<String, String>();
    }
    return parse2(str.toCharArray(), separator);
  }

  public Map<String, String> parse0(final String str, char[] separators) {

    if (separators == null || separators.length == 0) {
      return new HashMap<String, String>();
    }
    char separator = separators[0];
    if (str != null) {
      int idx = str.length();
      for (char separator2 : separators) {
        int tmp = str.indexOf(separator2);
        if (tmp != -1 && tmp < idx) {
          idx = tmp;
          separator = separator2;
        }
      }
    }
    return parse1(str, separator);
  }

  public void setLowerCaseNames(boolean b) {

    this.lowerCaseNames = b;
  }

  public boolean isLowerCaseNames() {

    return this.lowerCaseNames;
  }

  public ParameterParser() {

    super();
  }

  public String parseQuotedToken(final char[] terminators) {

    char ch;
    i1 = pos;
    i2 = pos;
    boolean quoted = false;
    boolean charEscaped = false;
    while (hasChar()) {
      ch = chars[pos];
      if (!quoted && isOneOf(ch, terminators)) {
        break;
      }
      if (!charEscaped && ch == '"') {
        quoted = !quoted;
      }
      charEscaped = (!charEscaped && ch == '\\');
      i2++;
      pos++;
    }
    return getToken(true);
  }

  public String parseToken(final char[] terminators) {

    char ch;
    i1 = pos;
    i2 = pos;
    while (hasChar()) {
      ch = chars[pos];
      if (isOneOf(ch, terminators)) {
        break;
      }
      i2++;
      pos++;
    }
    return getToken(false);
  }

  public boolean isOneOf(char ch, final char[] charray) {

    boolean result = false;
    for (char element : charray) {
      if (ch == element) {
        result = true;
        break;
      }
    }
    return result;
  }

  public String getToken(boolean quoted) {

    while ((i1 < i2) && (Character.isWhitespace(chars[i1]))) {
      i1++;
    }
    while ((i2 > i1) && (Character.isWhitespace(chars[i2 - 1]))) {
      i2--;
    }
    if (quoted && ((i2 - i1) >= 2) && (chars[i1] == '"') && (chars[i2 - 1] == '"')) {
      i1++;
      i2--;
    }
    String result = null;
    if (i2 > i1) {
      result = new String(chars, i1, i2 - i1);
    }
    return result;
  }

  public boolean hasChar() {

    return this.pos < this.len;
  }

  public java.util.Map pyToJ() {
    java.util.Map idMap = new java.util.HashMap();
    return pyToJ(idMap);
  }

  public java.util.Map pyToJ(java.util.Map idMap) {

    this.chars =
        (char[])
            IntegrationUtils.valueToObject(
                this.obj.getMember("_ParameterParser__chars"), "char[]", idMap, char.class, chars);
    this.pos =
        (int)
            IntegrationUtils.valueToObject(
                this.obj.getMember("_ParameterParser__pos"), "int", idMap, pos);
    this.len =
        (int)
            IntegrationUtils.valueToObject(
                this.obj.getMember("_ParameterParser__len"), "int", idMap, len);
    this.i1 =
        (int)
            IntegrationUtils.valueToObject(
                this.obj.getMember("_ParameterParser__i1"), "int", idMap, i1);
    this.i2 =
        (int)
            IntegrationUtils.valueToObject(
                this.obj.getMember("_ParameterParser__i2"), "int", idMap, i2);
    this.lowerCaseNames =
        (boolean)
            IntegrationUtils.valueToObject(
                this.obj.getMember("_ParameterParser__lowerCaseNames"),
                "boolean",
                idMap,
                lowerCaseNames);
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
        "_ParameterParser__chars",
        IntegrationUtils.mapToPython(chars, idMap, this.obj.getMember("_ParameterParser__chars")));
    this.obj.invokeMember(
        "__setattr__",
        "_ParameterParser__pos",
        IntegrationUtils.mapToPython(pos, idMap, this.obj.getMember("_ParameterParser__pos")));
    this.obj.invokeMember(
        "__setattr__",
        "_ParameterParser__len",
        IntegrationUtils.mapToPython(len, idMap, this.obj.getMember("_ParameterParser__len")));
    this.obj.invokeMember(
        "__setattr__",
        "_ParameterParser__i1",
        IntegrationUtils.mapToPython(i1, idMap, this.obj.getMember("_ParameterParser__i1")));
    this.obj.invokeMember(
        "__setattr__",
        "_ParameterParser__i2",
        IntegrationUtils.mapToPython(i2, idMap, this.obj.getMember("_ParameterParser__i2")));
    this.obj.invokeMember(
        "__setattr__",
        "_ParameterParser__lowerCaseNames",
        IntegrationUtils.mapToPython(
            lowerCaseNames, idMap, this.obj.getMember("_ParameterParser__lowerCaseNames")));
    return idMap;
  }
}
