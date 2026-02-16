package org.apache.commons.fileupload;

import java.util.Iterator;
import org.apache.commons.fileupload.ContextInitializer;
import org.apache.commons.fileupload.ExceptionHandler;
import org.apache.commons.fileupload.IntegrationUtils;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public interface FileItemHeaders {
  Iterator<String> getHeaderNames();

  Iterator<String> getHeaders(String name);

  String getHeader(String name);
}
