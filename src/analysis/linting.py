"""

"""

import subprocess
import shutil

class Linting:
    """
    Runs static analysis using pylint, flake8, and bandit to check code quality and security.
    """

    @staticmethod
    def check_tool(tool_name: str):
        if not shutil.which(tool_name):
            raise RuntimeError(f"Error: {tool_name} is not installed. Install it using `pip install {tool_name}`.")

    @staticmethod
    def run_pylint(file_path: str):
        Linting.check_tool("pylint")
        result = subprocess.run(["pylint", file_path], capture_output=True, text=True)
        return result.stdout

    @staticmethod
    def run_flake8(file_path: str):
        Linting.check_tool("flake8")
        result = subprocess.run(["flake8", file_path], capture_output=True, text=True)
        return result.stdout

    @staticmethod
    def run_bandit(file_path: str):
        Linting.check_tool("bandit")
        result = subprocess.run(["bandit", "-r", file_path], capture_output=True, text=True)
        return result.stdout

# Example
if __name__ == "__main__":
    file_to_check = "../parsers/ast_parser.py"
    print("Pylint Report:\n", Linting.run_pylint(file_to_check))
    print("Flake8 Report:\n", Linting.run_flake8(file_to_check))
    print("Bandit Security Report:\n", Linting.run_bandit(file_to_check))
