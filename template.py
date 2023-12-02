import logging
import os
from pathlib import Path


logging.basicConfig(
    format="[%(asctime)]: %(message)s:",
    level=logging.INFO
)


project_name = "imageClassifier"

list_of_line = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constant/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "research/test.ipynb",
    "test.py",
    "templates/index.html"



]

for filepath in list_of_line:
    # for the path type for window kind of system:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # now first i will create directories:
    if filedir != "":
        # create a directories
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating directory : {filedir} for : {filename}")

    # now I am going to create filename:
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"creating empty file :: {filepath}")

    else:
        logging.info(f"file is already exits !")




