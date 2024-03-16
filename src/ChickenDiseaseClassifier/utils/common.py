import os
from ensure import ensure_annotations
from box import ConfigBox
from box.exceptions import BoxValueError
from pathlib import Path
import json
import joblib
from typing import Any
import yaml
from ChickenDiseaseClassifier import logger

from typing import Any
import base64


@ensure_annotations
def read_yaml(path_to_yaml:Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def save_json(path:Path,data:dict):
    """save son data
    
    Keyword arguments:
    Args:
     path(Path): path to json file
     data(dict): data to be saved in json file 
    """
    with open(path,"w") as f:
        json.dump(data,f,indent=4)

    logger.info(f'json file saved at: {path}')

@ensure_annotations
def get_size(path:Path) -> str:
    ''' get size in kB

    Args:
        path(Path): path of the file

    Returns:
        str: size in KB
    '''
    size_in_kb = round(os.path.getsize(path)/1024)
    return f'~{size_in_kb} KB'

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

def decodeImage(imgstring,filename):
    imgdata =  base64.b64decode(imgstring)
    with open(filename,'wb') as f:
        f.write(imgdata)
        f.close()


    
