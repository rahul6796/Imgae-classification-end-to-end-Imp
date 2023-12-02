from src.imageClassifier import logger
from src.imageClassifier.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.imageClassifier.pipeline.prepare_base_model_pipeline import PrepareBaseModelPipeline
from src.imageClassifier.pipeline.prepare_callbacks_pipeline import PrepareCallbacksPipeline
#
# stage_name = "data_ingestion"
#
# try:
#     logger.info(f"start data ingestion :: {stage_name}")
#     data_ingestion = DataIngestionPipeline()
#     data_ingestion.main()
# except Exception as ex:
#     logger.error(f"failed to run data_ingestion :: {ex}")

# stage_name = "prepare_base_model"
#
# try:
#     logger.info(f"start : {stage_name}")
#     prepare_base_model = PrepareBaseModelPipeline()
#     prepare_base_model.main()
#
# except Exception as ex:
#     logger.error(f"failed to prepare base model :: {ex}")

stage_name = "prepare_callbacks"

try:
    logger.info(f"start : {stage_name}")
    prepare_callbacks = PrepareCallbacksPipeline()
    prepare_callbacks.main()
except Exception as ex:
    logger.error(f"failed to prepare base model :: {ex}")
