import ast
from typing import List

class ASTParser:
    def __init__(self, code: str):
        """Parses the given code into an AST."""
        self.tree = ast.parse(code)

    def get_functions(self) -> List[str]:
        """Extracts all function names from the AST."""
        return [node.name for node in ast.walk(self.tree) if isinstance(node, ast.FunctionDef)]

    def get_variables(self) -> List[str]:
        """Extracts all variable names from assignments in the AST."""
        return [node.targets[0].id for node in ast.walk(self.tree) if isinstance(node, ast.Assign)]

    def check_for_bad_practices(self) -> List[str]:
        """Checks for security risks like eval() or exec()."""
        issues = []
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                if node.func.id in {"exec", "eval"}:
                    issues.append(f"⚠️ Avoid using {node.func.id}() for security reasons!")
        return issues

# Example
if __name__ == "__main__":
    sample_code = """def hello():
    x = 5
    eval("print('Hello')")"""
    parser = ASTParser(sample_code)
    print("Functions:", parser.get_functions())
    print("Variables:", parser.get_variables())
    print("Issues:", parser.check_for_bad_practices())
