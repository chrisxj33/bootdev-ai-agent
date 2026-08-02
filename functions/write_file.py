from functions.validate import resolve_path
import os

schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes contents to a file relative to the working directory.",
        "parameters": {
            "type": "object",
            "required": ["file_path", "content"],
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path relative to the working directory to write contents to. This arg is required.",
                "content": {
                    "type": "string",
                    "description": "A string of the contents to write to the file. This arg is required"
                }
                },
            },
        },
    },
}

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