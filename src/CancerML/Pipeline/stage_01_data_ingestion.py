from CancerML.Entity.Config_Entity import DataIngestionConfig
from CancerML.Config.ConfigurationManager import ConfigurationManager
from CancerML.Components.Data_Ingestion import DataIngestion
from CancerML import logger

Stage_Name ="Data Ingestion"



class DataIngestionPipeLine:
    def __init__(self):
        pass
    def main(self):

        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.Download_File()
            
        except Exception as e:
            raise e


if __name__=="__main__":
    try :
        logger.info(f">>>>>>>>>> Stage : {Stage_Name} Started <<<<<<<<<<")
        obj=DataIngestionPipeLine()
        obj.main()
        logger.info(f">>>>>>>>>> Stage : {Stage_Name} Completed Successfully <<<<<<<<<<")
    except Exception as e:
        logger.info(e)
        raise e
        

