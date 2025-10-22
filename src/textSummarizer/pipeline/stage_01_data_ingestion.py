from textSummarizer.components.data_ingestion import DataIngestion
from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.logging import logger


class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()

            data_ingestion = DataIngestion(config=data_ingestion_config)

            # ✅ Step 1: download data and store returned path
            zip_file_path = data_ingestion.download_data()

            # ✅ Step 2: extract using that path
            data_ingestion.extract_zip(zip_file_path)

            logger.info("✅ Data ingestion stage completed successfully!")

        except Exception as e:
            logger.exception(e)
            raise e
