import re
import json
from typing import Optional


def extract_cangjie_code(generation: str, class_name: str = None) -> Optional[str]:
    """
    Extract Cangjie code from markdown code blocks.

    Args:
        generation: LLM response containing markdown code blocks
        class_name: Optional class name to wrap the method in

    Returns:
        Extracted code or None if not found
    """
    # Replace cangjie code block markers
    generation = generation.replace("```cangjie", "```")
    generation = generation.replace("```cj", "```")
    generation = generation.replace("```java", "```")

    # Extract code block content
    pattern = r"(?:```\s*)+(.+?)(?:\s*```)+"
    match = re.search(pattern, generation, re.DOTALL)

    if match:
        extracted = match.group(1).strip()

        # If extracted code doesn't contain class definition but we have a class_name,
        # wrap the method in a class
        if class_name and 'class ' not in extracted:
            # Check if it's a method (contains 'func')
            if 'func ' in extracted:
                # Wrap method in class
                wrapped = f"class {class_name} {{\n{extracted}\n}}"
                return wrapped

        return extracted

    # Try alternative pattern if no code block found
    # Look for anything that looks like Cangjie code (has func, class, let, etc.)
    lines = generation.split('\n')
    code_lines = []
    in_code = False

    for line in lines:
        # Check if line looks like it contains code (starts with whitespace or has common keywords)
        if any(keyword in line for keyword in ['func ', 'class ', 'let ', 'var ', 'pub ', 'priv ', 'import ', 'package ']):
            in_code = True
            code_lines.append(line)
        elif in_code and (line.strip() == '' or line.strip().startswith('//') or line.strip().startswith('#')):
            # Allow empty lines and comments in code
            code_lines.append(line)
        elif in_code and not line.startswith(' ') and not line.startswith('\t'):
            # Stop if we hit a non-indented line that's not a comment
            if line.strip():
                break
            code_lines.append(line)

    if code_lines:
        extracted = '\n'.join(code_lines).strip()

        # If extracted code doesn't contain class definition but we have a class_name,
        # wrap the method in a class
        if class_name and 'class ' not in extracted:
            if 'func ' in extracted:
                wrapped = f"class {class_name} {{\n{extracted}\n}}"
                return wrapped

        return extracted

    return None


def add_dummy_main(code: str) -> str:
    """
    Add a dummy main function if not present (required by Cangjie compiler).
    Must be placed at the beginning of the file (before class definitions).
    Cangjie uses 'main()' not 'func main()'.
    """
    # Check if main function already exists (with any parameters)
    # Match patterns like: main(), main(args: ...), main(args: Array<String>)
    import re
    if re.search(r'\bmain\s*\(', code):
        return code

    # Add a dummy main function at the beginning (Cangjie uses main() without func)
    code = """main() {
    return 0
}

""" + code
    return code


def cangjie_syntax_validation(generation: str, fragment: dict, args) -> tuple:
    """
    Validate Cangjie syntax by extracting code from markdown and checking basic structure.

    Args:
        generation: LLM response
        fragment: Fragment information
        args: Command line arguments

    Returns:
        tuple: (success: bool, extracted_code: str or None, feedback: str)
    """
    # Get class name from fragment
    class_name = fragment.get('class_name', None)

    # Extract Cangjie code from markdown, passing class name for wrapping
    extracted_code = extract_cangjie_code(generation, class_name)

    if extracted_code is None:
        return False, None, "the model did not generate any code"

    # Add dummy main function if not present (required by Cangjie compiler)
    extracted_code = add_dummy_main(extracted_code)

    # Basic Cangjie syntax checks
    code_lines = extracted_code.split('\n')

    # Remove empty lines and comments for analysis
    meaningful_lines = [line for line in code_lines if line.strip() and not line.strip().startswith('//')]

    if not meaningful_lines:
        return False, None, "the model did not generate any code"

    # Check that the code has at least some structure
    # Look for common Cangjie keywords
    # Note: 'main(' without 'func' is also valid (main function in Cangjie)
    has_function = any('func ' in line or 'main(' in line for line in code_lines)
    has_class = any('class ' in line for line in code_lines)
    has_var = any('var ' in line for line in code_lines)
    has_let = any('let ' in line for line in code_lines)

    if not (has_function or has_class or has_var or has_let):
        return False, None, "the generated code does not appear to be valid Cangjie code"

    # If validation passes, return the extracted code
    return True, extracted_code.split('\n'), None


# Legacy function name for compatibility
def syntactic_validation(generation, fragment, args, signature):
    """
    Legacy function for compatibility with existing code.
    For Cangjie, we use simple extraction without AST parsing.
    """
    success, code, feedback = cangjie_syntax_validation(generation, fragment, args)

    if not success:
        return False, None, feedback

    # Return in the format expected by the caller
    return True, code, None
