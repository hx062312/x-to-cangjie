package org.apache.commons.fileupload;

import java.io.IOException;
import java.io.InputStream;
import org.apache.commons.fileupload.ContextInitializer;
import org.apache.commons.fileupload.ExceptionHandler;
import org.apache.commons.fileupload.IntegrationUtils;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public interface RequestContext {
  InputStream getInputStream() throws IOException;

  int getContentLength();

  String getContentType();

  String getCharacterEncoding();
}
