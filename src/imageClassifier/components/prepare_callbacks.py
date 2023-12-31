import os.path

import tensorflow as tf
from src.imageClassifier.config.configuration import PrepareCallbacksConfig
import time
from src.imageClassifier import logger


class PrepareCallbacks:

    def __init__(self,
                 config: PrepareCallbacksConfig):
        self.config = config

    @property
    def _create_tb_callbacks(self):
        try:
            timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")
            tb_running_log_dir = os.path.join(
                self.config.tensorboard_root_log_dir,
                f"tb_logs_at_{timestamp}"
            )
            return tf.keras.callbacks.TensorBoard(log_dir=tb_running_log_dir)
        except Exception as ex:
            logger.error(f"failed to _create_tb_callbacks :: {ex}")

    @property
    def _create_ckpt_callbacks(self):
        return tf.keras.callbacks.ModelCheckpoint(
            filepath=self.config.checkpoint_model_filepath,
            save_best_only=True
        )

    def get_tb_ckpt_callbacks(self):
        try:
            return [
                self._create_tb_callbacks,
                self._create_ckpt_callbacks
            ]
        except Exception as ex:
            logger.error(f"failed to get tb ckpt callbacks :: {ex}")
