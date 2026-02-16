package org.apache.commons.fileupload;

import org.apache.commons.fileupload.ContextInitializer;
import org.apache.commons.fileupload.ExceptionHandler;
import org.apache.commons.fileupload.IntegrationUtils;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public interface FileItemHeadersSupport {
  void setHeaders(FileItemHeaders headers);

  FileItemHeaders getHeaders();
}
