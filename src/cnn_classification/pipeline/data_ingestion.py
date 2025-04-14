from cnn_classification.components.download_data import DataIngestion
from cnn_classification import logger

STAGE_NAME = "Data Ingestion"

class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        dataingestion = DataIngestion()
        dataingestion.load_data()
        dataingestion.relocate_data()

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>> stage: {STAGE_NAME} started <<<<<<<<")
        data_ingestion = DataIngestionPipeline()
        data_ingestion.main()
        logger.info(f">>>>>>>> stage: {STAGE_NAME} completed <<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e