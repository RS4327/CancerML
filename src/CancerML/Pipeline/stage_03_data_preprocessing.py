from CancerML.Config.ConfigurationManager import ConfigurationManager
from CancerML.Entity.Config_Entity import DataPreProcessingConfig
from CancerML.Components.Data_PreProcessing import DataPreProcessing
from CancerML import logger

Stage_Name=" Data PreProcessing"

class DataPreProcessingPipeline:
    def __init__(self):
        pass

    def main(self): 
        try :
            config=ConfigurationManager()
            data_preproces=config.Get_DataPreProcesing_Config()
            data_preprocessing=DataPreProcessing(config=data_preproces)
            check_files=data_preprocessing.Check_files()
            df=data_preprocessing.DataFrame()
        
        except Exception as e:
            raise e
    


if __name__=="__main__":
    try :
        logger.info(f">>>>>>>>>> Stage : {Stage_Name} Started <<<<<<<<<<")
        obj=DataPreProcessingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>> Stage : {Stage_Name} Completed Successfully <<<<<<<<<<")
    except Exception as e:
        logger.info(e)
        raise e