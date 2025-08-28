import os,sys
from box.exceptions import BoxValueError
import yaml
from src.textSummarizer.logging import logging
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations # What is ensure_annotations
def read_yaml(path_to_yaml:Path)->ConfigBox: # what is ConfigBox
    try:
        with open(path_to_yaml)as yaml_file:
            content=yaml.safe_load(yaml_file)
            logging.info(f"Yaml file:{path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories:list,verbose=True):
    """
    create list of directories
    Args:
        path_to_directories(list): list of path of directories
        ignore_log(bool, optional):ignore if multiple dirs to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logging.info(f"Created Directory at: {path}")