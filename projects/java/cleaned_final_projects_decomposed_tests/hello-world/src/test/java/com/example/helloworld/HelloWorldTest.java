package com.example.helloworld;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.io.TempDir;
import org.junit.jupiter.api.BeforeEach;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.util.Scanner;

import static org.junit.jupiter.api.Assertions.*;

public class HelloWorldTest {

    private final ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
    private final PrintStream originalOut = System.out;

    @BeforeEach
    void setUp() {
        System.setOut(new PrintStream(outputStream));
    }

    @Test
    void testHelloWithoutName() {
        HelloWorld.hello();
        String output = outputStream.toString().trim();
        assertEquals("Hello, World!", output);
    }

    @Test
    void testHelloWithName() {
        outputStream.reset();
        HelloWorld.hello("Alice");
        String output = outputStream.toString().trim();
        assertEquals("Hello, Alice!", output);
    }

    @Test
    void testHelloWithEmptyName() {
        outputStream.reset();
        HelloWorld.hello("");
        String output = outputStream.toString().trim();
        assertEquals("Hello, !", output);
    }

    @Test
    void testHelloWithSpecialCharacters() {
        outputStream.reset();
        HelloWorld.hello("张三");
        String output = outputStream.toString().trim();
        assertEquals("Hello, 张三!", output);
    }
}
