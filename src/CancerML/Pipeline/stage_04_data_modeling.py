from CancerML.Config.ConfigurationManager import ConfigurationManager
from CancerML.Components.Data_modeling import DataModeling
from CancerML import logger
from CancerML.Entity.Config_Entity import DataModelingConfig

Stage_Name='Data Modeling'

class DataModelingPipeline:
        def __init__(self):
             pass    
        

        def main(self):

            try:
                config=ConfigurationManager()
                data_model=config.get_data_modeling_config()
                DataModel=DataModeling(config=data_model)
                Model=DataModel.Train_Model()
                
                
            except Exception as e:
                raise e


if __name__=="__main__":
    try :
        logger.info(f">>>>>>>>>> Stage : {Stage_Name} Started <<<<<<<<<<")
        obj=DataModelingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>> Stage : {Stage_Name} Completed Successfully <<<<<<<<<<")
    except Exception as e:
        logger.info(e)
        raise e
    



