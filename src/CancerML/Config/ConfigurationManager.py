from CancerML.Constants import *
from CancerML.Utils.common import * 
from CancerML.Entity.Config_Entity import DataIngestionConfig
from pathlib import Path


class ConfigurationManager:
    def __init__(
            self,
            config_path=CONFIG_FILE_PATH,
            params_path=PARAMS_FILE_PATH
    ):
        self.config=Read_Yaml(Path("Config/Config.yaml"))
        self.params=Read_Yaml(params_path)

    
    def get_data_ingestion_config(self)->DataIngestionConfig:
        config=self.config.data_ingestion
        data_ingestion_config=DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file
        )
        return data_ingestion_config



