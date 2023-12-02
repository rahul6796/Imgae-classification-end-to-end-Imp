import os.path
from pathlib import Path

from src.imageClassifier.constant import CONFIG_FILE_PATH, PARAM_FILE_PATH
from src.imageClassifier.utils.common import read_yaml, create_directories
from src.imageClassifier.entity.config_entity import DataIngestionConfig
from src.imageClassifier.entity.config_entity import PrepareBaseModelConfig, PrepareCallbacksConfig


class ConfigurationManager:

    def __init__(self,
                 config_file_path=CONFIG_FILE_PATH,
                 params_file_path=PARAM_FILE_PATH):

        self.config = read_yaml(config_file_path)
        self.param = read_yaml(params_file_path)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config

    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config.prepare_base_model
        create_directories([config.root_dir])
        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir=config.root_dir,
            base_model_path=config.base_model_path,
            updated_base_model_path=config.updated_base_model_path,
            params_image_size=self.param.IMAGE_SIZE,
            params_learning_rate=self.param.LEARNING_RATE,
            params_include_top=self.param.INCLUDE_TOP,
            params_weights=self.param.WEIGHTS,
            params_classes=self.param.CLASSES
        )
        return prepare_base_model_config

    def get_prepare_callbacks_config(self) -> PrepareCallbacksConfig:
        config = self.config.prepare_callbacks
        model_ckpt_dir = os.path.dirname(config.checkpoint_model_filepath)
        create_directories([Path(model_ckpt_dir),
                            Path(config.tensorboard_root_log_dir)])

        prepare_callback_config = PrepareCallbacksConfig(
            root_dir=Path(config.root_dir),
            tensorboard_root_log_dir=Path(config.tensorboard_root_log_dir),
            checkpoint_model_filepath=Path(config.checkpoint_model_filepath)
        )
        return prepare_callback_config









