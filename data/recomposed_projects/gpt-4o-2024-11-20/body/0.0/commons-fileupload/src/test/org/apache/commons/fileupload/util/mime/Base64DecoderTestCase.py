from __future__ import annotations
import re
from io import BytesIO
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.fileupload.util.mime.Base64Decoder import *


class Base64DecoderTestCase(unittest.TestCase):

    __US_ASCII_CHARSET: str = "US-ASCII"

    def testnonASCIIcharacter_test0_decomposed(self) -> None:
        self.__assertEncoded("f", "Zg=À=")
        self.__assertEncoded("f", "Zg=\u0100=")

    def testbadLength_test0_decomposed(self) -> None:
        self.__assertOSError("truncated", "Zm8==")

    def testbadPaddingLeading2_test0_decomposed(self) -> None:
        self.__assertOSError(
            "incorrect padding, first two bytes cannot be padding", "===="
        )

    def testbadPaddingLeading1_test0_decomposed(self) -> None:
        self.__assertOSError(
            "incorrect padding, first two bytes cannot be padding", "=A=="
        )

    def testbadPadding_test0_decomposed(self) -> None:
        self.__assertOSError("incorrect padding, 4th byte", "Zg=a")

    def testdecodeTrailing3_test0_decomposed(self) -> None:
        self.__assertOSError("truncated", "Zm9vYmFy123")

    def testdecodeTrailing2_test0_decomposed(self) -> None:
        self.__assertOSError("truncated", "Zm9vYmFy12")

    def testdecodeTrailing1_test0_decomposed(self) -> None:
        self.__assertOSError("truncated", "Zm9vYmFy1")

    def testdecodeTrailingJunk_test0_decomposed(self) -> None:
        self.__assertEncoded("foobar", "Zm9vYmFy!!!")

    def testtruncatedString_test0_decomposed(self) -> None:
        x = b"n"  # Equivalent to new byte[] {'n'} in Java
        with self.assertRaises(
            io.UnsupportedOperation
        ):  # OSError in Java maps to IOError/UnsupportedOperation in Python
            Base64Decoder.decode(x, io.BytesIO())

    def testnonBase64Bytes_test0_decomposed(self) -> None:
        self.__assertEncoded("Hello World", "S?G!V%sbG 8g\rV\t\n29ybGQ*=")

    def testdecodeWithInnerPad_test0_decomposed(self) -> None:
        self.__assertEncoded(
            "Hello WorldHello World", "SGVsbG8gV29ybGQ=SGVsbG8gV29ybGQ="
        )

    def testrfc4648Section10Decode_test0_decomposed(self) -> None:
        self.__assertEncoded("", "")
        self.__assertEncoded("f", "Zg==")
        self.__assertEncoded("fo", "Zm8=")
        self.__assertEncoded("foo", "Zm9v")
        self.__assertEncoded("foob", "Zm9vYg==")
        self.__assertEncoded("fooba", "Zm9vYmE=")
        self.__assertEncoded("foobar", "Zm9vYmFy")

    @staticmethod
    def __assertOSError(messageText: str, encoded: str) -> None:
        out = io.BytesIO()  # Equivalent to ByteArrayOutputStream in Java
        encodedData = encoded.encode(
            Base64DecoderTestCase.__US_ASCII_CHARSET
        )  # Convert string to bytes using US-ASCII

        try:
            Base64Decoder.decode(encodedData, out)  # Attempt to decode
            pytest.fail("Expected OSError")  # Fail if no exception is raised
        except IOError as e:  # Catch the IOError (equivalent to OSError in Java)
            em = str(e)  # Get the exception message
            assert (
                messageText in em
            ), f"Expected to find '{messageText}' in '{em}'"  # Assert the message contains the expected text

    @staticmethod
    def __assertEncoded(clearText: str, encoded: str) -> None:
        expected = clearText.encode("US-ASCII")

        out = io.BytesIO()
        encodedData = encoded.encode("US-ASCII")
        Base64Decoder.decode(encodedData, out)
        out.seek(0)  # Ensure the pointer is at the beginning of the stream
        actual = out.read(len(expected))  # Read only the expected number of bytes

        assert expected == actual, f"Expected {expected}, but got {actual}"
