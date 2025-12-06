from CancerML.Config.ConfigurationManager import ConfigurationManager
from CancerML.Entity.Config_Entity import DataValidationConfig
from CancerML.Components.Data_Validation import DataValidation
from CancerML import logger

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
    

if __name__=="__main__":
    try :
        logger.info(f">>>>>>>>>> Stage : {Stage_Name} Started <<<<<<<<<<")
        obj=DataValidationPipeline()
        obj.main()
        logger.info(f">>>>>>>>>> Stage : {Stage_Name} Completed Successfully <<<<<<<<<<")
    except Exception as e:
        logger.info(e)
        raise e