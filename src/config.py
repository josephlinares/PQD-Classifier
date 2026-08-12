import yaml
from pathlib import Path

import utils

def get_config_path(config_path=None, filename=None):
    """Return config.yaml path object"""
    if config_path:
        return Path(config_path) / filename
    
    # If no path is received, returns /path/to/script/config.yaml
    return Path(__file__).parent / filename

def load_config(filename='config.yaml') -> dict:
    print("Reading yaml config")
    path = get_config_path(utils.SRC_DIR, filename)

    if not path.exists():
        raise FileNotFoundError(f"Config file not found at {path}")
    
    with open(path, "r") as stream:
        try:
            return yaml.safe_load(stream) or {}
        except yaml.YAMLError as exc:
            raise ValueError(f"Config file cannot be parsed: {exc}")


def log_config(config, config_path):
    """Export data to a YAML file"""
    config_path = config_path / 'config.yaml'

    with open(config_path, 'w') as file:
        yaml.dump(config, file, default_flow_style=False, sort_keys=False)

    print("Successfully exported yaml config")