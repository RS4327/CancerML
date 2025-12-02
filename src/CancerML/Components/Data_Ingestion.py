import os 
from pathlib import Path
from urllib.request import Request
from CancerML.Utils.common import *
from CancerML import logger
import requests
from CancerML.Config.ConfigurationManager import DataIngestionConfig

os.chdir(r"C:\Users\RSR\PYTHON\LinearRegression")

class DataIngestion:
    def __init__(self,config=DataIngestionConfig):
        self.config=config
    
    def Download_File(self):

        #Step 1 Get the file paths 
        url=self.config.source_url
        download_path=self.config.local_data_file
        extract_file=self.config.root_dir
        #Step 2 Creating the Directories

        #os.mkdir(os.path.dirname(download_path),exist_ok=True)
        os.makedirs(os.path.dirname(download_path), exist_ok=True)
        os.makedirs(extract_file, exist_ok=True)

        # response=requests.get(url)
        # with open(download_path,'wb') as file:
        #     file.write(requests.content)\
        
        #Dowe Load the file
        response=requests.get(url)
        with open(download_path,'wb') as file:
            file.write(response.content)
          
        logger.info(f"✅ CSV Test file downloaded to: {download_path}") 

