package org.apache.commons.fileupload.util;

import java.io.IOException;
import org.apache.commons.fileupload.ContextInitializer;
import org.apache.commons.fileupload.ExceptionHandler;
import org.apache.commons.fileupload.IntegrationUtils;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public interface Closeable {
  boolean isClosed() throws IOException;

  void close() throws IOException;
}
