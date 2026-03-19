// Package Declaration
package calculator

// Imports Begin
import std.collection.*
import std.io.*
// Imports End

class Main {
	// Class Fields Begin
	// Class Fields End

	// Class Methods Begin
	internal static func printUsage(): Unit {
				println("Simple Calculator - Command Line Tool")
		println("")
		println("Usage:")
		println("    calc <operation> <num1> <num2>")
		println("")
		println("Operations:")
		println("    add, +     Addition")
		println("    sub, -     Subtraction")
		println("    mul, *     Multiplication")
		println("    div, /     Division")
		println("")
		println("Examples:")
		println("    calc add 10 5")
		println("    calc + 10 5")
		println("    calc sub 20 8")
		println("    calc mul 6 7")
		println("    calc div 100 4")
		println("")
		println("Note: Input values must be between 0 and 999")
	}
	internal static func printResult(result: Int64): Unit {
		throw Exception('TODO')
	}
	internal static func parseInt(s: String): Int64 {
		throw Exception('TODO')
	}
	// Class Methods End

}

main(args: Array<String>): Int64 {
	throw Exception('TODO')
}

