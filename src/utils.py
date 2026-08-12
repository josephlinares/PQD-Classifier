import os
from pathlib import Path
from datetime import datetime

UTILS_DIR = Path(__file__).resolve().parent

PROJECT_ROOT = UTILS_DIR.parent

DATA_DIR = PROJECT_ROOT / "data"
SRC_DIR = PROJECT_ROOT / "src"
MODELS_DIR = PROJECT_ROOT / "models"
#OUTPUT_DIR = DATA_DIR / "output"

def timestamp_dir():
    now = datetime.now().strftime('%m_%d-%H_%M')
    experiment_name = f'run_{now}'

    path = MODELS_DIR / experiment_name
    os.makedirs(path, exist_ok=True)

    return path

def print_dictionary(dictionary: dict = {}):
    for key, value in dictionary.items():
        print(f'{key}: {value}')