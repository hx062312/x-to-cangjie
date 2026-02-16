from __future__ import annotations
import re
from abc import ABC
import io
import os


class Closeable(ABC):

    def isClosed(self) -> bool:
        raise NotImplementedError("Subclasses must implement this method")

    def close(self) -> None:
        raise NotImplementedError("Subclasses must implement this method")
