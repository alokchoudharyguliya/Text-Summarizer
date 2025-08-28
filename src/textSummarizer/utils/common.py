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
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e