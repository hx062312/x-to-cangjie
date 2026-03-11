package com.example.helloworld;

import java.util.Scanner;

public class HelloWorld {

    public static void hello() {
        System.out.println("Hello, World!");
    }

    public static void hello(String name) {
        System.out.println("Hello, " + name + "!");
    }

    public static void main(String[] args) {
        // 调用无参版本
        hello();

        // 调用带参版本
        Scanner scanner = new Scanner(System.in);
        System.out.print("Please enter your name: ");
        String name = scanner.nextLine();
        hello(name);
        scanner.close();
    }
}
