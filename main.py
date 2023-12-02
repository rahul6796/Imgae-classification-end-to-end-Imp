from src.imageClassifier import logger
from src.imageClassifier.pipeline.data_ingestion_pipeline import DataIngestionPipeline

stage_name = "data_ingestion"

try:
    logger.info(f"start data ingestion :: {stage_name}")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
except Exception as ex:
    logger.error(f"failed to run data_ingestion :: {ex}")
