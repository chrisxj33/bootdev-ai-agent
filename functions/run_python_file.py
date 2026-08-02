from functions.validate import resolve_path
import subprocess
import os

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        header = f'Result for {file_path}\n'

        target_file, error = resolve_path(working_directory, file_path)

        if error:
            return header + error

        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_file]
        if args:
            command += args

        completed_process = subprocess.run(args=command, cwd=working_directory, capture_output=True, text=True, timeout=30.0)

        message = ''
        if completed_process.returncode != 0:
            message += f"Process exited with code {completed_process.returncode}"
        if not completed_process.stderr and not completed_process.stdout:
            message += f"No output produced"
        if completed_process.stdout:
            message += f"STDOUT: {completed_process.stdout}"
        if completed_process.stderr:
            message += f"STDERR: {completed_process.stderr}"

        return message
    
    except Exception as e:
        return f'Error: {e}'


