import kagglehub
import shutil
from pathlib import Path
import os
from cnn_classification import logger

class DataIngestion:
    def __init__(self,
                 url: str = "paultimothymooney/chest-xray-pneumonia",
                 file_path: Path = Path("Data/raw_data")):
        self.url = url
        self.file_path = file_path

    def load_data(self):
        logger.info("Data Downloading...")
        self.path = kagglehub.dataset_download(self.url)
        logger.info("Data Downloaded...")

    def relocate_data(self):
        logger.info("ReLocating the dataset...")
        os.makedirs(self.file_path, exist_ok = True)
        shutil.move(src = self.path,
                    dst = self.file_path)
        logger.info("ReLoaction Done...")