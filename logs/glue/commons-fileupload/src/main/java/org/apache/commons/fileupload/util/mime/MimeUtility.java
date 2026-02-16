package org.apache.commons.fileupload.util.mime;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.util.HashMap;
import java.util.Locale;
import java.util.Map;
import org.apache.commons.fileupload.ContextInitializer;
import org.apache.commons.fileupload.ExceptionHandler;
import org.apache.commons.fileupload.IntegrationUtils;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public final class MimeUtility {
  private transient Value obj =
      IntegrationUtils.createDefaultPythonObject(
          ContextInitializer.getPythonClass(
              "main/org/apache/commons/fileupload/util/mime/MimeUtility.py", "MimeUtility"));
  public static final String US_ASCII_CHARSET = "US-ASCII";
  public static final String BASE64_ENCODING_MARKER = "B";
  public static final String QUOTEDPRINTABLE_ENCODING_MARKER = "Q";
  public static final String ENCODED_TOKEN_MARKER = "=?";
  public static final String ENCODED_TOKEN_FINISHER = "?=";
  public static final String LINEAR_WHITESPACE = " \t\r\n";
  public static final Map<String, String> MIME2JAVA = new HashMap<String, String>();

  static {
    MIME2JAVA.put("iso-2022-cn", "ISO2022CN");
    MIME2JAVA.put("iso-2022-kr", "ISO2022KR");
    MIME2JAVA.put("utf-8", "UTF8");
    MIME2JAVA.put("utf8", "UTF8");
    MIME2JAVA.put("ja_jp.iso2022-7", "ISO2022JP");
    MIME2JAVA.put("ja_jp.eucjp", "EUCJIS");
    MIME2JAVA.put("euc-kr", "KSC5601");
    MIME2JAVA.put("euckr", "KSC5601");
    MIME2JAVA.put("us-ascii", "ISO-8859-1");
    MIME2JAVA.put("x-us-ascii", "ISO-8859-1");
  }

  public Value getPythonObject() {
    return obj;
  }

  public void setPythonObject(Value obj) {
    this.obj = obj;
  }

  public static String decodeText(String text) throws UnsupportedEncodingException {

    try {

      if (text.indexOf(ENCODED_TOKEN_MARKER) < 0) {
        return text;
      }

      int offset = 0;
      int endOffset = text.length();

      int startWhiteSpace = -1;
      int endWhiteSpace = -1;

      StringBuilder decodedText = new StringBuilder(text.length());

      boolean previousTokenEncoded = false;

      while (offset < endOffset) {
        char ch = text.charAt(offset);

        if (LINEAR_WHITESPACE.indexOf(ch) != -1) { // whitespace found
          startWhiteSpace = offset;
          while (offset < endOffset) {
            ch = text.charAt(offset);
            if (LINEAR_WHITESPACE.indexOf(ch) != -1) { // whitespace found
              offset++;
            } else {
              endWhiteSpace = offset;
              break;
            }
          }
        } else {
          int wordStart = offset;

          while (offset < endOffset) {
            ch = text.charAt(offset);
            if (LINEAR_WHITESPACE.indexOf(ch) == -1) { // not white space
              offset++;
            } else {
              break;
            }
          }
          String word = text.substring(wordStart, offset);
          if (word.startsWith(ENCODED_TOKEN_MARKER)) {
            try {
              String decodedWord = decodeWord(word);

              if (!previousTokenEncoded && startWhiteSpace != -1) {
                decodedText.append(text.substring(startWhiteSpace, endWhiteSpace));
                startWhiteSpace = -1;
              }
              previousTokenEncoded = true;
              decodedText.append(decodedWord);
              continue;

            } catch (ParseException e) {
            }
          }
          if (startWhiteSpace != -1) {
            decodedText.append(text.substring(startWhiteSpace, endWhiteSpace));
            startWhiteSpace = -1;
          }
          previousTokenEncoded = false;
          decodedText.append(word);
        }
      }

      return decodedText.toString();

    } catch (Throwable ExceptionObjectForCaching) {
      ExceptionHandler.ERR = ExceptionObjectForCaching;
      throw ExceptionObjectForCaching;
    }
  }

  public static String javaCharset(String charset) {

    if (charset == null) {
      return null;
    }

    String mappedCharset = MIME2JAVA.get(charset.toLowerCase(Locale.ENGLISH));
    if (mappedCharset == null) {
      return charset;
    }
    return mappedCharset;
  }

  public static String decodeWord(String word) throws ParseException, UnsupportedEncodingException {

    try {

      if (!word.startsWith(ENCODED_TOKEN_MARKER)) {
        throw new ParseException("Invalid RFC 2047 encoded-word: " + word);
      }

      int charsetPos = word.indexOf('?', 2);
      if (charsetPos == -1) {
        throw new ParseException("Missing charset in RFC 2047 encoded-word: " + word);
      }

      String charset = word.substring(2, charsetPos).toLowerCase(Locale.ENGLISH);

      int encodingPos = word.indexOf('?', charsetPos + 1);
      if (encodingPos == -1) {
        throw new ParseException("Missing encoding in RFC 2047 encoded-word: " + word);
      }

      String encoding = word.substring(charsetPos + 1, encodingPos);

      int encodedTextPos = word.indexOf(ENCODED_TOKEN_FINISHER, encodingPos + 1);
      if (encodedTextPos == -1) {
        throw new ParseException("Missing encoded text in RFC 2047 encoded-word: " + word);
      }

      String encodedText = word.substring(encodingPos + 1, encodedTextPos);

      if (encodedText.length() == 0) {
        return "";
      }

      try {
        ByteArrayOutputStream out = new ByteArrayOutputStream(encodedText.length());

        byte[] encodedData = encodedText.getBytes(US_ASCII_CHARSET);

        if (encoding.equals(BASE64_ENCODING_MARKER)) {
          Base64Decoder.decode(encodedData, out);
        } else if (encoding.equals(QUOTEDPRINTABLE_ENCODING_MARKER)) { // maybe quoted printable.
          QuotedPrintableDecoder.decode(encodedData, out);
        } else {
          throw new UnsupportedEncodingException("Unknown RFC 2047 encoding: " + encoding);
        }
        byte[] decodedData = out.toByteArray();
        return new String(decodedData, javaCharset(charset));
      } catch (IOException e) {
        throw new UnsupportedEncodingException("Invalid RFC 2047 encoding");
      }

    } catch (Throwable ExceptionObjectForCaching) {
      ExceptionHandler.ERR = ExceptionObjectForCaching;
      throw ExceptionObjectForCaching;
    }
  }

  public MimeUtility() {}

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
