import subprocess
import shutil

class ComplexityAnalyzer:
    """
    Uses Radon to analyze the complexity of a Python file.
    """

    @staticmethod
    def check_tool(tool_name: str):
        if not shutil.which(tool_name):
            raise RuntimeError(f"Error: {tool_name} is not installed. Install it using `pip install {tool_name}`.")

    @staticmethod
    def analyze_complexity(file_path: str):
        ComplexityAnalyzer.check_tool("radon")
        result = subprocess.run(["radon", "cc", file_path, "-a"], capture_output=True, text=True)
        return result.stdout

    @staticmethod
    def analyze_maintainability_index(file_path: str):
        ComplexityAnalyzer.check_tool("radon")
        result = subprocess.run(["radon", "mi", file_path], capture_output=True, text=True)
        return result.stdout

# Example 
if __name__ == "__main__":
    file_to_check = "../parsers/ast_parser.py"
    print("Code Complexity Report:\n", ComplexityAnalyzer.analyze_complexity(file_to_check))
    print("Maintainability Index:\n", ComplexityAnalyzer.analyze_maintainability_index(file_to_check))
