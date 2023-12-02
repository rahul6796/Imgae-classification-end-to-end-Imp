import os
import urllib.request as request
import zipfile

from src.imageClassifier import logger
from src.imageClassifier.utils.common import get_size
from src.imageClassifier.config.configuration import DataIngestionConfig
from pathlib import Path


class DataIngestion:

    def __init__(self,
                 config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        try:
            if not os.path.exists(self.config.local_data_file):
                filename, header = request.urlretrieve(
                    url=self.config.source_URL,
                    filename=self.config.local_data_file
                )
                logger.info(f"{filename} download! with following info: \n{header}")
            else:
                logger.info(f"file already exit of size : {get_size(Path(self.config.local_data_file))}")

        except Exception as ex:
            logger.error(f"failed to download file :: {ex}")

    def extract_zip_file(self):
        try:
            unzip_dir = self.config.unzip_dir
            os.makedirs(unzip_dir, exist_ok=True)
            with zipfile.ZipFile(self.config.local_data_file, 'r') as f:
                f.extractall(unzip_dir)
        except Exception as ex:
            logger.error(f"failed to extract zip file :: {ex}")

