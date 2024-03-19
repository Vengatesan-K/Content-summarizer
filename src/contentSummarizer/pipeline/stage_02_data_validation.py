from contentSummarizer.config.configuration import  ConfigurationManager
from contentSummarizer.components.data_ingestion import DataIngestion
from contentSummarizer.logging import logger
from contentSummarizer.components.data_validation import DataValidation

class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_validation = DataValidation(config.get_data_validation_config())
        data_validation.validate_all_files_exist()