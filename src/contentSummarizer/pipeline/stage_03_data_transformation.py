from contentSummarizer.config.configuration import  ConfigurationManager
from contentSummarizer.components.data_transformation import DataTransformation
from contentSummarizer.logging import logger
from contentSummarizer.components.data_validation import DataValidation

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config_manager = ConfigurationManager()
        data_transformation = DataTransformation(config_manager.get_data_transformation())
        data_transformation.convert()