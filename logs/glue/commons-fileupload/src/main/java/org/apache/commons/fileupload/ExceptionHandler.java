package org.apache.commons.fileupload;

import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.lang.ArrayIndexOutOfBoundsException;
import java.lang.ClassCastException;
import java.lang.NumberFormatException;
import java.lang.SecurityException;
import java.nio.charset.UnsupportedCharsetException;
import java.util.NoSuchElementException;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

/**
 * Provides a method to handle exceptions from Polyglot.
 *
 * <p>e: the PolyglotException object to handle thrower: the class and method that threw the
 * exception (as "Class.method")
 */
public final class ExceptionHandler {
  public static Throwable ERR = null;

  public static Throwable handle(PolyglotException e, String thrower) {
    if (e.isHostException()) {
      return e.asHostException();
    }

    String exceptionType;
    String exceptionMessage;

    if (e.getMessage().contains(": ")) {
      exceptionType = e.getMessage().split(":", 2)[0].trim();
      exceptionMessage = e.getMessage().split(": ", 2)[1].trim();
    } else {
      exceptionType = e.getMessage().trim();
      exceptionMessage = "".trim();
    }
    Value exceptionObj = e.getGuestObject();

    if (exceptionObj.hasMember("javaObj")) {
      return exceptionObj.getMember("javaObj").as(Throwable.class);
    }

    if (exceptionType.equals("OSError") && thrower.equals("QuotedPrintableDecoder.decode")) {
      return new IOException();
    }
    if (exceptionType.equals("ValueError")) {
      return new IllegalArgumentException();
    }
    if (exceptionType.equals("RuntimeError")) {
      return new RuntimeException();
    }
    if (exceptionType.equals("NotImplementedError")) {
      return new UnsupportedOperationException();
    }
    if (exceptionType.equals("NotImplementedError")) {
      return new CloneNotSupportedException();
    }
    if (exceptionType.equals("RuntimeError")) {
      return new IllegalStateException();
    }
    if (exceptionType.equals("RuntimeError")) {
      return new NullPointerException();
    }
    if (exceptionType.equals("OSError")) {
      return new IOException();
    }
    if (exceptionType.equals("ValueError")) {
      return new UnsupportedEncodingException();
    }
    if (exceptionType.equals("RuntimeError")) {
      return new NoSuchElementException();
    }
    if (exceptionType.equals("ValueError")) {
      return new NumberFormatException();
    }
    if (exceptionType.equals("TypeError")) {
      return new ClassCastException();
    }
    if (exceptionType.equals("IndexError")) {
      return new ArrayIndexOutOfBoundsException();
    }
    if (exceptionType.equals("ValueError")) {
      return new UnsupportedCharsetException("unsupported charset");
    }
    if (exceptionType.equals("PermissionError")) {
      return new SecurityException();
    }

    System.out.println("[ExceptionHandler] Unhandled exception type: " + exceptionType);
    System.out.println("The exception had the following message: " + exceptionMessage);
    return new RuntimeException(exceptionMessage);
  }
}
