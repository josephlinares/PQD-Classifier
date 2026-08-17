import os
import sys
from pathlib import Path
from datetime import datetime

UTILS_DIR = Path(__file__).resolve().parent

PROJECT_ROOT = UTILS_DIR.parent

DATA_DIR = PROJECT_ROOT / "data"
SRC_DIR = PROJECT_ROOT / "src"
MODELS_DIR = PROJECT_ROOT / "models"
CONFIG_DIR = PROJECT_ROOT / "configs"

def get_first_arg() -> str:
    return sys.argv[1]

def get_config_path(filename: str=None):
    '''Returns path of experiment configuration

    Parameters:
    filename (str): configuration filename
    '''
    return CONFIG_DIR / filename

def set_timestamp_dir():
    '''Creates a directory named run_MM_DD-HH_MM
    under models/ for experiment logging
    '''
    now = datetime.now().strftime('%m_%d-%H_%M')
    experiment_name = f'run_{now}'

    path = MODELS_DIR / experiment_name
    os.makedirs(path, exist_ok=True)

    return path

def print_dictionary(dictionary: dict = {}):
    for key, value in dictionary.items():
        print(f'{key}: {value}')

def create_markdown(results : list, path : Path):
    '''Writes a MarkDown file for experimentation results

    Parameters:
    results (list): Macro F1 and Classification in MD format
    path (Path): Experimentation path where this will be stored
    '''
    with open(path / "README.md", "w", encoding="utf-8") as file:
        print("# Experimentation results\n", file=file)
        print(results[0], '\n', file=file)
        print(results[1], '\n', file=file)
        print('![Confusion Matrix](<confusion matrix.png>)\n', file=file)
        print('# Annotations\n', file=file)

def get_file_size(file_path):
    size = os.path.getsize(file_path)
    return size
    
def convert_bytes(size, unit=None):
    if unit == "KB":
        return print('File size: ' + str(round(size / 1024, 3)) + ' Kilobytes')
    elif unit == "MB":
        return print('File size: ' + str(round(size / (1024 * 1024), 3)) + ' Megabytes')
    else:
        return print('File size: ' + str(size) + ' bytes')