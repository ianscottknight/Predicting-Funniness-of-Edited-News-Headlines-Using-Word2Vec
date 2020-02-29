
import os
import dotenv
from pathlib import Path

dotenv.load_dotenv()

# TODO: assign environmental variables
#VAR = os.getenv("VAR_NAME")

def get_root_dir():
    """Returns project root directory based on hierarchical depth of util.py"""
    return Path(__file__).parent.parent

ROOT_DIR = get_root_dir()
DATA_DIR = os.path.join(ROOT_DIR, "data")
SRC_DIR = os.path.join(ROOT_DIR, "src")
NOTEBOOKS_DIR = os.path.join(ROOT_DIR, "notebooks")

def load_txt_file_as_list(filepath):
    with open(filepath, "r") as f:
        lst = [line.strip() for line in f.readlines()]
    return lst
