// Package Declaration
package calculator

// Imports Begin
import std.io.*
// Imports End

class Validator {
	// Class Fields Begin
	// Class Fields End

	// Class Methods Begin
	public static func isValid(value: Int64): Bool {
				return value >= 0 && value < 1000
	}
	// Class Methods End

}

