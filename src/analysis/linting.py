import subprocess

class Linting:
    @staticmethod
    def run_pylint(file_path: str):
        result = subprocess.run(["pylint", file_path], capture_output=True, text=True)
        return result.stdout

    @staticmethod
    def run_flake8(file_path: str):
        result = subprocess.run(["flake8", file_path], capture_output=True, text=True)
        return result.stdout

    @staticmethod
    def run_bandit(file_path: str):
        result = subprocess.run(["bandit", "-r", file_path], capture_output=True, text=True)
        return result.stdout

# Example 
if __name__ == "__main__":
    file_to_check = "../parsers/ast_parser.py"
    print("Pylint Report:\n", Linting.run_pylint(file_to_check))
    print("Flake8 Report:\n", Linting.run_flake8(file_to_check))
    print("Bandit Security Report:\n", Linting.run_bandit(file_to_check))
