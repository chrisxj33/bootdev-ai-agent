import os
from functions.validate import resolve_path

schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        header = f'Result for {directory}\n'
        if directory == ".":
            header = f'Result for current directory\n'

        target_dir, error = resolve_path(working_directory, directory)
        if error:
            return header + error

        info = ''
        for name in os.listdir(target_dir):
            abs_path = os.path.join(target_dir, name)
            isdir = False

            if os.path.isdir(abs_path):
                isdir = True

            file_size = os.path.getsize(abs_path)

            info += f'  - {name}: file_size={file_size} bytes, is_dir={isdir}\n'

        return header + info

    except Exception as e:
        return f'Error: {e}'