


from src.imageClassifier.config.configuration import ConfigurationManager
from src.imageClassifier.components.evaluation import Evaluation

class EvaluationPipeline:

    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(config=val_config)
        evaluation.evaluation()
        evaluation.save_score()
