from functions.validate import resolve_path
import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        header = f'Result for {file_path}\n'

        target, error = resolve_path(working_directory, file_path)

        if error:
            return header + error

        if os.path.isdir(target):
            return f'Error: Cannot write to "{target}" as it is a directory'

        os.makedirs(os.path.dirname(target), exist_ok=True)

        with open(target, "w") as f:
            f.write(content)

        return header + f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f'Error: {e}'