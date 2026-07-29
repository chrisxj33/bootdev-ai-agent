from functions.validate import resolve_path
from config import MAX_CHARS

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        header = f'Result for {file_path}\n'
        target_file, error = resolve_path(working_directory, file_path)

        if error:
            return header + error

        with open(target_file, "r") as f:
            file_content_string = f.read(MAX_CHARS)

            if f.read(1):
                file_content_string += f'[...File "{target_file}" truncated at {MAX_CHARS} characters]'

        return header + file_content_string

    except Exception as e:
        return f'Error: {e}'