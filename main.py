from CancerML import logger
from CancerML.Pipeline.stage_01_data_ingestion import  DataIngestionPipeLine
from CancerML.Pipeline.stage_02_data_validation import DataValidationPipeline
from CancerML.Pipeline.stage_03_data_preprocessing import DataPreProcessingPipeline
from CancerML.Pipeline.stage_04_data_modeling import DataModelingPipeline
from CancerML.Pipeline.stage_05_data_dript import DataDriftPipeline

Stage_Name ='Data Ingestion'

try :
    logger.info(f">>>>>>>>>> Stage : {Stage_Name} Started <<<<<<<<<<")
    obj=DataIngestionPipeLine()
    obj.main()
    logger.info(f">>>>>>>>>> Stage : {Stage_Name} Completed Successfully <<<<<<<<<<")
except Exception as e:
    logger.info(e)
    raise e


Stage_Name ="Data Validation"


try :
    logger.info(f">>>>>>>>>> Stage : {Stage_Name} Started <<<<<<<<<<")
    obj=DataValidationPipeline()
    obj.main()
    logger.info(f">>>>>>>>>> Stage : {Stage_Name} Completed Successfully <<<<<<<<<<")
except Exception as e:
    logger.info(e)
    raise e

Stage_Name=" Data PreProcessing"

try :
    logger.info(f">>>>>>>>>> Stage : {Stage_Name} Started <<<<<<<<<<")
    obj=DataPreProcessingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>> Stage : {Stage_Name} Completed Successfully <<<<<<<<<<")
except Exception as e:
    logger.info(e)
    raise e


Stage_Name='Data Modeling'
try :
    
    logger.info(f">>>>>>>>>> Stage : {Stage_Name} Started <<<<<<<<<<")
    obj=DataModelingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>> Stage : {Stage_Name} Completed Successfully <<<<<<<<<<")
except Exception as e:
    logger.info(e)
    raise e

Stage_Name='Data Drift'
try :
    
    logger.info(f">>>>>>>>>> Stage : {Stage_Name} Started <<<<<<<<<<")
    obj=DataDriftPipeline()
    obj.main()
    logger.info(f">>>>>>>>>> Stage : {Stage_Name} Completed Successfully <<<<<<<<<<")
except Exception as e:
    logger.info(e)
    raise e