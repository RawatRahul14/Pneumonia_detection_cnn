from cnn_classification import logger
from cnn_classification.pipeline.data_ingestion import DataIngestionPipeline

STAGE_NAME = "Data Ingestion"
try:
    logger.info(f">>>>>>>> stage: {STAGE_NAME} started <<<<<<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>> stage: {STAGE_NAME} completed <<<<<<<<")
    logger.info("-"*50)
except Exception as e:
    logger.exception(e)
    raise e