import os
import urllib.request
import zipfile
from textSummarizer.logging import logger


class DataIngestion:
    def __init__(self, config):
        self.config = config

    def download_data(self):
        logger.info("Starting data download...")

        # ✅ Ensure directory exists before download
        os.makedirs(os.path.dirname(self.config.local_data_file), exist_ok=True)

        logger.info(f"Downloading data from {self.config.source_URL} to {self.config.local_data_file}...")
        urllib.request.urlretrieve(self.config.source_URL, self.config.local_data_file)
        logger.info("Data download complete.")
        return self.config.local_data_file

    def extract_zip(self, zip_file_path):
        logger.info(f"Extracting data from {zip_file_path} to {self.config.unzip_dir}...")
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(self.config.unzip_dir)
        logger.info("Extraction completed.")