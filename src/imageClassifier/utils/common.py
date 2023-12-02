import os
from typing import Any

from box.exceptions import BoxValueError
import yaml
from src.imageClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import  ConfigBox
from pathlib import Path
import base64


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """

    :param path_to_yaml:
    :return:
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info("successfully read yaml file!")
            return ConfigBox(content)
    except Exception as ex:
        logger.error(f"failed to read yaml file :: {ex}")


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    try:
        for path in path_to_directories:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f"created directories as :: {path}")
    except Exception as ex:
        logger.error(f"failed to create directories :: {ex}")


@ensure_annotations
def save_json(path: Path, data : dict):
    """

    :param path:
    :param data:
    :return:
    """
    try:
        with open(path, 'w') as f:
            json.dump(data, f)

        logger.info("successfully save json")
    except Exception as ex:
        logger.error(f"failed to save json :: {ex}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """

    :param path:
    :return:
    """
    try:
        with open(path, "r") as f:
            content = json.load(f)
        logger.error("successfully load json data")
        return ConfigBox(content)
    except Exception as ex:
        logger.error(f"failed to load json data :: {ex}")


@ensure_annotations
def save_bin(data: Any, path: Path):
    """

    :param data:
    :param path:
    :return:
    """
    try:
        joblib.dump(value=data, filename=path)
        logger.info("successfully save data as binary")
    except Exception as ex:
        logger.error(f"failed to save data as binary :: {ex}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """

    :param path:
    :return:
    """
    try:
        data = joblib.load(filename=path)
        logger.info("successfully binary file data loaded !")
        return data
    except Exception as ex:
        logger.error(f"failed to load binary file data :: {ex}")


@ensure_annotations
def get_size(path: Path) -> str:
    """

    :param path:
    :return:
    """
    try:
        size_in_kb = round(os.path.getsize(filename=path)/1024)
        return f"~{size_in_kb} kb"
    except Exception as ex:
        logger.error(f"failed to get_size :: {ex}")


def decodeImage(imgstring, filename):
    imgdata = base64.b64decode(imgstring)
    with open(filename, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())








