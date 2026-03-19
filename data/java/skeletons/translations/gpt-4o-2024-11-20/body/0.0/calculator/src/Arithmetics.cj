// Package Declaration
package calculator

// Imports Begin
import std.io.*
// Imports End

class Arithmetics {
	// Class Fields Begin
	// Class Fields End

	// Class Methods Begin
	public func div(a: Int64, b: Int64): Int64 {
				if (b == 0) {
		return 0
		}
		return a / b
	}
	public func mul(a: Int64, b: Int64): Int64 {
				return a * b
	}
	public func sub(a: Int64, b: Int64): Int64 {
				return a - b
	}
	public func add(a: Int64, b: Int64): Int64 {
				return a + b
	}
	// Class Methods End

}

