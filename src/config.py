import yaml
from pathlib import Path

from utils import get_config_path, get_first_arg

def load_config(filename : str=None) -> dict:
    '''Loads experiment configuration file
    
    Parameters:
    filename (str): Name of the config file
    
    Returns:
    dict: Configuration dictionary
    
    '''
    print("Reading config yaml")
    if not filename:
        filename = get_first_arg()
    path = get_config_path(filename)

    if not path.exists():
        raise FileNotFoundError(f"Config file not found at {path}")
    
    with open(path, "r") as stream:
        try:
            return yaml.safe_load(stream) or {}
        except yaml.YAMLError as exc:
            raise ValueError(f"Config file cannot be parsed: {exc}")


def log_config(config, config_path: Path):
    '''Export data to a YAML file
    
    Parameters:
    config (dict): Config dictionary to log
    config_path (Path): Path to folder
    '''
    config_path = config_path / 'config.yaml'

    with open(config_path, 'w') as file:
        yaml.dump(config, file, default_flow_style=False, sort_keys=False)

    print("Successfully exported yaml config")