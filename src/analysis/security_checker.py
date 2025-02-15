import subprocess

class SecurityChecker:
    @staticmethod
    def run_bandit(file_path: str):
        result = subprocess.run(["bandit", "-r", file_path], capture_output=True, text=True)
        return result.stdout

    @staticmethod
    def run_safety():
        result = subprocess.run(["safety", "check"], capture_output=True, text=True)
        return result.stdout

# Example 
if __name__ == "__main__":
    file_to_scan = "../parsers/ast_parser.py"
    print("Bandit Security Check:\n", SecurityChecker.run_bandit(file_to_scan))
    print("Dependency Vulnerability Check (Safety):\n", SecurityChecker.run_safety())
