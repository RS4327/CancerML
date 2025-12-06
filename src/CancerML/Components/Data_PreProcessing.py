import numpy as np
import pandas as pd
import os 
from CancerML.Entity.Config_Entity import DataPreProcessingConfig
from pathlib import Path
from CancerML import logger
import seaborn as sns
import matplotlib.pyplot as plt


class DataPreProcessing:
    def __init__(self,
                 config=DataPreProcessingConfig):
        self.config=config
    def Check_files(self):
        file=Path(self.config.data_load_path)
        if file.name in self.config.all_required_files:
            validataion_staus=True
            with open(self.config.status_file,'w') as f:
                f.write(f" Validation Status : {validataion_staus}")
        else:
            logger.info(f"File doesnot exist in the source path")
        return validataion_staus
    def DataFrame(self):
        file=Path(self.config.data_load_path)
        if file.name in self.config.all_required_files:
            df=pd.read_csv(file)
            logger.info(f"\n Data Frame Information  \n {df.info()}")
            logger.info(f"\n  \n" )
            logger.info(f"\n ---------------- Step 1 : Checking Missing Values ---------------- \n" )
            missing_found=False
            for features in df.columns:
                if df[features].isnull().sum()>0:
                    logger.info(f" \n Features Name : {features} \n Missing Values Count :{df[features].isnull().sum()}")
                    missing_found=True
            if  not missing_found: 
                logger.info(f" There is no missing values in our data set")
            logger.info(f"\n  \n" )
            logger.info(f"\n ---------------- Step 2 : Checking the Dupliate Values ---------------- \n" )
            if df.duplicated().sum()==0:
                logger.info(f"There is no Duplicated recoreds in our data set")
            else:
                logger.info(f"Found the few duplciated records in our dataset")
                duplicate_rows = df[df.duplicated()]
                logger.info(f"\n {duplicate_rows} \n")
                logger.info(f"--- Removing the Duplicate Records ----- ")
                df=df.drop_duplicates()
            logger.info(f"\n  \n" )
            logger.info(f"\n ---------------- Step 3 : Exploratory Data Analysis---------------- \n" )
            logger.info("**** Histogram **** ")
            df.hist(figsize=(7,7))
            plt.show()

            logger.info("-------------- Describe the Histogram -----------------")
            logger.info("\n --------- icavol(Log Cancer Volume) ---------\n 1.Almost normal Distribution \n 2.Good Bell shaped curve \n 3.No Action Needed ")
            logger.info("\n --------- lweight(Log Prostate Weight) ---------\n 1.Normal Distribution \n 2.Already Gaussian-like \n 3.No Action Needed ")
            logger.info("\n --------- age(Patient Age ) ---------\n 1.Slight skew \n 2.Acceptable \n 3.No action needed ")
            logger.info("\n --------- lbph(Log Benign Prostatic Hyperplasia) ---------\n 1.Highly right-skewed \n 2.Long tail, heavy skew \n 3.Yes Action Needed ")
            logger.info("\n --------- svi(Seminal Vesicle Invasion (binary)) ---------\n 1.Binary (0/1) \n 2.Categorical \n 3.No action needed ")
            logger.info("\n --------- lcp(Log Capsular Penetration ) ---------\n 1.Strong right-skew \n 2.Very concentrated at low values \n 3.Yes Action Needed ")
            logger.info("\n --------- gleason(Gleason Score	Clinical  ) ---------\n 1.Discrete small range \n 2.Treat as categorical \n 3.No action needed ")
            logger.info("\n --------- pgg45(% of Gleason patterns 4 or 5 ) ---------\n 1.Extremely right-skewed \n 2.Heavy outliers \n 3.Yes Action Needed ")
            logger.info("\n --------- lpsa(Log Prostate-specific Antigen (PSA)) ---------\n 1.Mild skew (0/1) \n 2.Small skew ok \n 3.Optional action needed ")
            
            logger.info(f" \n------- Linear Regression, you must fix skewness for these features -------- \n ✅ lbph \n ✅ lcp \n ✅ pgg45")
            
            logger.info(f"\n Identifying the which columns having the invalid values")
            cols = ['lbph', 'lcp', 'pgg45']
            for c in cols:
                print(c, df[c].min(), df[c].isnull().sum())
            
            logger.info(f"\n Fix negative and missing values" )  

            for c in ['lbph', 'lcp', 'pgg45']:
                df[c] = df[c].clip(lower=0)
            
            logger.info("\n Filling the NAN values ")
            for c in ['lbph', 'lcp', 'pgg45']:
                df[c] = df[c].fillna(df[c].median())

            df['lbph'] = np.log1p(df['lbph'])
            df['lcp'] = np.log1p(df['lcp'])
            df['pgg45'] = np.log1p(df['pgg45'])

            df.hist(figsize=(7, 7))
            plt.show()

            logger.info(f"\n --------------  HeatMap ----------------------")
            sns.heatmap(df.corr(),annot=True,cmap='coolwarm')

            logger.info(f"---- Saving the preprocessind data into csv ")
            df.to_csv(self.config.local_data_path, index=False)
            

        else:
            logger.info(f"Data set does not exist in the source path : please check")
        return df
            



