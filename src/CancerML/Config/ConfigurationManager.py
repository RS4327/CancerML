from CancerML.Constants import *
from CancerML.Utils.common import * 
from CancerML.Entity.Config_Entity import DataIngestionConfig
from CancerML.Entity.Config_Entity import DataValidationConfig
from CancerML.Entity.Config_Entity import DataPreProcessingConfig
from pathlib import Path


class ConfigurationManager:
    def __init__(
            self,
            config_path=CONFIG_FILE_PATH,
            params_path=PARAMS_FILE_PATH
    ):
        self.config=Read_Yaml(Path("Config/Config.yaml"))
        self.params=Read_Yaml(params_path)
        create_directories([self.config.artifacts_root])

    
    def get_data_ingestion_config(self)->DataIngestionConfig:
        config=self.config.data_ingestion
        data_ingestion_config=DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file
        )
        return data_ingestion_config

    def get_datavalidation_config(self)->DataValidationConfig:
        config=self.config.data_validation

        create_directories([config.root_dir])
        data_validation_config=DataValidationConfig(
            root_dir=config.root_dir,
            data_load_path=config.data_load_path,
            local_data_path=config.local_data_path,
            STATUS_FILE=config.STATUS_FILE,
            ALL_REQUIRED_FILES=config.ALL_REQUIRED_FILES 
        )
        return data_validation_config
    def Get_DataPreProcesing_Config(self)->DataPreProcessingConfig:
        config=self.config.data_preprocessing

        create_directories([config.root_dir])
        Data_PreProcessing_Config=DataPreProcessingConfig(
            root_dir=config.root_dir,
            data_load_path=config.data_load_path,
            local_data_path=config.local_data_path,
            status_file=config.status_file,
            all_required_files=config.all_required_files

        )
        return Data_PreProcessing_Config



