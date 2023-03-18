import os


def find_executables_in_path(path_str: str | None = None) -> list[str]:
    path_env = path_str or os.environ.get("PATH", "")
    assert path_env is not None
    path_dirs = path_env.split(os.pathsep)
    unique_path_dirs = {os.path.realpath(path_dir) for path_dir in path_dirs}
    executables = []

    for path_dir in unique_path_dirs:
        if os.path.isdir(path_dir):
            for entry in os.listdir(path_dir):
                entry_path = os.path.join(path_dir, entry)
                if os.path.isfile(entry_path) and os.access(entry_path, os.X_OK):
                    executables.append(entry_path)

    return executables
