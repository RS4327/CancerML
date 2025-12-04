from CancerML.Config.ConfigurationManager import ConfigurationManager
from CancerML.Entity.Config_Entity import DataValidationConfig
from CancerML.Components.Data_Validation import DataValidation

Stage_Name="Data Validation"

class DataValidationPipeline:
    def __init__(Self):
        pass
    def main(self):
        try:
            config=ConfigurationManager()
            DataValidationConfig=config.get_datavalidation_config()
            datavaliation=DataValidation(config=DataValidationConfig)
            validation=datavaliation.Check_files()
        except Exception as e:
            raise e