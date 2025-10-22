from textSummarizer.components.data_ingestion import DataIngestion
from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.logging import logger


class DataIngestionPipeline:
    def __init__(self):
        self.config_manager = ConfigurationManager()
        self.data_ingestion_config = self.config_manager.get_data_ingestion_config()
        # define self.data_ingestion here
        self.data_ingestion = DataIngestion(config=self.data_ingestion_config)
    def main(self):
        
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()

            data_ingestion = DataIngestion(config=data_ingestion_config)

            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
            
        