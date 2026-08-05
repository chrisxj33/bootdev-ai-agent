from functions.validate import resolve_path
from config import MAX_CHARS

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": f"Gets file contents of a specified files path relative to the working directory, truncating contents if greater than {MAX_CHARS}",
        "parameters": {
            "type": "object",
            "required": ["file_path"],
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path to read contents from, relative to the working directory. This arg is required.",
                },
            },
        },
    },
}

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