
from src.imageClassifier.config.configuration import ConfigurationManager
from src.imageClassifier.components.prepare_callbacks import PrepareCallbacks


class PrepareCallbacksPipeline:

    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_callbacks_config = config.get_prepare_callbacks_config()
        prepare_callbacks = PrepareCallbacks(config=prepare_callbacks_config)
        prepare_callbacks.get_tb_ckpt_callbacks()





