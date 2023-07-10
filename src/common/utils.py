import shutil
import yaml
import os
from ensure import ensure_annotations
from pathlib import Path
from box import ConfigBox
from box.exceptions import BoxValueError
from src import logger
import dill
import json
import base64


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
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
def create_directories(path_to_directories: list, verbose=True):
    for path in path_to_directories:
        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f"created directory at: {path}")


@ensure_annotations
def remove_directories(path_to_directories: list, verbose=True):
    for path in path_to_directories:
        if os.path.exists(path):
            shutil.rmtree(path)
            if verbose:
                logger.info(f"removed directory at: {path}")


@ensure_annotations
def save_object(data: object, path: Path):
    with open(path, "w") as f:
        dill.dump(data, f)
    logger.info(f"object saved at: {path}")


@ensure_annotations
def load_object(path: Path) -> object:
    data = dill.load(path)
    logger.info(f"object loaded from: {path}")
    return data


@ensure_annotations
def save_json(path: Path, data: dict):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"json file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    with open(path) as f:
        content = json.load(f)
    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)


def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()