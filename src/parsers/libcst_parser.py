import libcst as cst
from typing import List, Tuple

class LoopVisitor(cst.CSTVisitor):
    def __init__(self):
        self.loops = []

    def visit_For(self, node: cst.For):
        """Records 'for' loop presence in the code."""
        self.loops.append("for loop")

    def visit_While(self, node: cst.While):
        """Records 'while' loop presence in the code."""
        self.loops.append("while loop")

class ClassVisitor(cst.CSTVisitor):
    def __init__(self):
        self.classes = []
        self.current_class = None 
        self.class_methods = {}

    def visit_ClassDef(self, node: cst.ClassDef):
        """Tracks class names while parsing."""
        class_name = node.name.value
        self.current_class = class_name
        self.class_methods[class_name] = []

    def leave_ClassDef(self, node: cst.ClassDef):
        """Records class name and associated methods."""
        self.classes.append((self.current_class, self.class_methods[self.current_class]))
        self.current_class = None 

    def visit_FunctionDef(self, node: cst.FunctionDef):
        """Tracks methods within classes."""
        if self.current_class:
            self.class_methods[self.current_class].append(node.name.value)

class CSTParser:
    def __init__(self, code: str):
        """Parses code into a CST for further analysis."""
        self.tree = cst.parse_module(code)

    def extract_loops(self) -> List[str]:
        """Extracts loop types (for, while) from the code."""
        visitor = LoopVisitor()
        self.tree.visit(visitor)
        return visitor.loops

    def extract_classes(self) -> List[Tuple[str, List[str]]]:
        """Extracts class names and their methods from the code."""
        visitor = ClassVisitor()
        self.tree.visit(visitor)
        return visitor.classes

    def get_syntax_tree(self) -> str:
        """Returns the string representation of the code's syntax tree."""
        return self.tree.code

# Example
if __name__ == "__main__":
    sample_code = """\
class Example:
    def method1(self):
        for i in range(10):
            print(i)

    def method2(self):
        while True:
            break
"""
    parser = CSTParser(sample_code)
    print("Loops Found:", parser.extract_loops())  
    print("Classes and Methods:", parser.extract_classes())  
    print("Syntax Tree:\n", parser.get_syntax_tree())
