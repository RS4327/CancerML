from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error 
import joblib

import pandas as pd
import numpy as np
import os
import requests
from io import StringIO
from pathlib import Path
from CancerML.Entity.Config_Entity import DataDriftConfig
from CancerML import logger


class DataDrift:
    def __init__(self,config:DataDriftConfig):
        self.config=config
    def data_validation(self):
        new_file=Path(self.config.new_data_source_url)
        old_file=Path(self.config.old_data_path)
        #logger.info(new_file.name)
        #logger.info(new_file)
        #logger.info(old_file.name)
        #new1_df = pd.read_csv(new_file)
        #logger.info(new1_df)
        csv_file_old_name='data_preprocessing.csv'
        csv_file_new_name='new_cancer_dataset.csv'
        
        if new_file.name ==csv_file_new_name and old_file.name==csv_file_old_name:
            logger.info(' Inside ')
            old_df=pd.read_csv(old_file)
            #logger.info(old_df.info())
            #new_df=pd.read_csv(new_file)
            #new_file = new_file.replace("https:\\", "https://").replace("https:/", "https://")
            new_file = str(new_file)

            # Fix malformed slashes
            new_file = new_file.replace("https:\\", "https://")
            new_file = new_file.replace("https:/", "https://")
            new_file = new_file.replace("\\", "/")
            new_file = new_file.replace("///", "//")
            #print(new_file)
            new_df = pd.read_csv(new_file) 
            logger.info('-- Checking Missing values : ')
            missing_value_count=False
            for features in new_df.columns:
                if new_df[features].isnull().sum()>0:
                    logger.info(f'\n Missing Values Count : {new_df[features].isnull().sum()}')
                    #new_df[] = df_new.fillna(df_new.mean())
                else:
                    missing_value_count=True
            if not missing_value_count:
                logger.info('\n There is no missing values')
            if new_df.duplicated().sum()>0:
                new_df.drop_duplicates()
            else:
                logger.info(f" There is no Duplicate alues")
            logger.info(f"\n --- Compare the # schema mismatch ----")
            #logger.info(new_df.dtypes())

            logger.info("\n Checking for Data Drift")
            drift_report=(new_df.mean()-old_df.mean())
            logger.info(f" Data Drift Report :{drift_report}")

            logger.info(f" LOAD DEPLOYED MODEL & TEST ON NEW DATA")
            old_scaler_pkl=self.config.load_old_scaler_path
            old_model_pkl=self.config.load_old_model_path
            scaler = joblib.load(old_scaler_pkl)
            deployed_model = joblib.load(old_model_pkl)

            X_new = new_df.drop("lpsa", axis=1)
            y_new = new_df["lpsa"]

            X_new_scaled = scaler.transform(X_new)
            pred_new = deployed_model.predict(X_new_scaled)

            print("NEW DATA R2 Score:", r2_score(y_new, pred_new))
            print("NEW DATA RMSE:", mean_squared_error(y_new, pred_new))

            logger.info(f"\n STEP 11 — RETRAIN MODEL USING NEW DATA")
            from sklearn.model_selection import train_test_split

            Xn_train, Xn_test, yn_train, yn_test = train_test_split(X_new_scaled, y_new, test_size=0.2)

            new_model = LinearRegression()
            new_model.fit(Xn_train, yn_train)

            print("UPDATED MODEL R2:", r2_score(yn_test, new_model.predict(Xn_test)))
            logger.info(f"\n Re Deploying the model")
            model_save= Path(self.config.root_dir)
            
            model_save = model_save / "prostate_model_v2.pkl"
            joblib.dump(new_model, model_save )
            print("🔥 NEW UPDATED MODEL DEPLOYED")

        

            
