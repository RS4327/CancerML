from CancerML.Config.ConfigurationManager import ConfigurationManager
from CancerML.Components.Data_Drift import DataDrift
from CancerML import logger
from CancerML.Entity.Config_Entity import DataDriftConfig

Stage_Name='Data Drift'

class DataDriftPipeline:
        def __init__(self):
             pass    
        

        def main(self):

            try:
                config=ConfigurationManager()
                data_drift=config.get_data_drift()
                validation=DataDrift(config=data_drift)
                validation=validation.data_validation()
            except Exception as e:
                raise e


if __name__=="__main__":
    try :
        logger.info(f">>>>>>>>>> Stage : {Stage_Name} Started <<<<<<<<<<")
        obj=DataDriftPipeline()
        obj.main()
        logger.info(f">>>>>>>>>> Stage : {Stage_Name} Completed Successfully <<<<<<<<<<")
    except Exception as e:
        logger.info(e)
        raise e
    



