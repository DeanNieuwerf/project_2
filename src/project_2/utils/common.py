import os
from box.exceptions import BoxValueError
import yaml
from project_2.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """ reads yaml file and returns
    
    Args:
        path_to_yaml (str): path like input
        
    Raises:
        ValueError: If yaml file is empty
        e: empty file
    
    Returns:
        ConfigBox: ConfigBox type
    """
    
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded succesfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Create list of directories
    
    Args:
        path_to_directories(list): list of path of directories
        ignore_log (bool, optional): Ignore if multiple dirs are to be created. Default to False.
    """
    
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at : {path}")
            


@ensure_annotations
def get_size(path: Path) -> str:
    """Get size in kb
    
    Args:
        path (Path): path of the file ARG MAX
        
    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.get_size(path)/1024)
    return f"~ {size_in_kb} KB"