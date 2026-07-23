import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        header = f'Result for {directory}\n'
        if directory == ".":
            header = f'Result for current directory\n'

        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

        if not os.path.isdir(target_dir):
            return header + f'  Error: "{target_dir}" is not a directory'

        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        if not valid_target_dir:
            return header + f'  Error: Cannot list "{directory}" as it is outside the permitted working directory'

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


if __name__ == "__main__":
    get_files_info(working_directory="functions", directory="hello")