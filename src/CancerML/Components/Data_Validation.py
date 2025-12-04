from pathlib import Path
from CancerML.Constants import *
from CancerML.Utils.common import *
from CancerML.Entity.Config_Entity import DataValidationConfig


class DataValidation:
    def __init__(self,config:DataValidationConfig):
        self.config=config

    
    def Check_files(self)->bool:
        
        validation_status=None
        file='cancer_dataset.csv'
        if file not in self.config.ALL_REQUIRED_FILES:
              validation_status=False
              with open(self.config.STATUS_FILE,'w') as f:
                    f.write(f"Validation Status :{validation_status}")
        else:
            validation_status=True
            with open(self.config.STATUS_FILE,'w') as f:
                  f.write(f"Validation Status : {validation_status}")
        return validation_status