import subprocess
import shutil

class SecurityChecker:
    """
    Performs security checks on code using Bandit and Safety tools.
    """

    @staticmethod
    def check_tool(tool_name: str):
        if not shutil.which(tool_name):
            raise RuntimeError(f"Error: {tool_name} is not installed. Install it using `pip install {tool_name}`.")

    @staticmethod
    def run_bandit(file_path: str):
        SecurityChecker.check_tool("bandit")
        result = subprocess.run(["bandit", "-r", file_path], capture_output=True, text=True)
        return result.stdout

    @staticmethod
    def run_safety():
        SecurityChecker.check_tool("safety")
        result = subprocess.run(["safety", "check"], capture_output=True, text=True)
        return result.stdout

# Example
if __name__ == "__main__":
    file_to_scan = "../parsers/ast_parser.py"
    print("Bandit Security Check:\n", SecurityChecker.run_bandit(file_to_scan))
    print("Dependency Vulnerability Check (Safety):\n", SecurityChecker.run_safety())
