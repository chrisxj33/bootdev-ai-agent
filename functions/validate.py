import os

def resolve_path(working_directory: str, target: str):
    working_dir_abs = os.path.abspath(working_directory)
    target_abs = os.path.normpath(os.path.join(working_dir_abs, target))
    valid_target = os.path.commonpath([working_dir_abs, target_abs]) == working_dir_abs

    if not valid_target:
        return None, f'  Error: "{target}" is outside the permitted working directory'

    return target_abs, None
        

