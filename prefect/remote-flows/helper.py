import os
from datetime import datetime as dt
from functools import lru_cache
from pathlib import Path


def time_stamp():
    return dt.now().strftime("%Y%m%d_%H%M")


def print_cwd():
    cwd = os.getcwd()
    print(cwd)
    return cwd


def create_some_files(dir_path: Path):
    with open(dir_path / "temp_file.txt", "+a") as f:
        out = f"Updating log at {time_stamp()}\n"
        print(out)
        f.write(out)
