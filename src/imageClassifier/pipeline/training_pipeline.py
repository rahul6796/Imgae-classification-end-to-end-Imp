

from src.imageClassifier.config.configuration import ConfigurationManager
from src.imageClassifier.components.prepare_callbacks import PrepareCallbacks
from src.imageClassifier.components.training import Training


class TrainingPipeline:

    def __init__(self):
        pass

    def main(self):

        # first prepare for callback:
        config = ConfigurationManager()
        prepare_callbacks_config = config.get_prepare_callback_config()
        prepare_callbacks = PrepareCallbacks(config=prepare_callbacks_config)
        callback_list = prepare_callbacks.get_tb_ckpt_callbacks()

        # second for training:
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train(callback_list=callback_list)




