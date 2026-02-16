package org.apache.commons.fileupload;

import java.io.IOException;
import org.apache.commons.fileupload.ContextInitializer;
import org.apache.commons.fileupload.ExceptionHandler;
import org.apache.commons.fileupload.IntegrationUtils;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public interface FileItemIterator {
  FileItemStream next() throws FileUploadException, IOException;

  boolean hasNext() throws FileUploadException, IOException;
}
