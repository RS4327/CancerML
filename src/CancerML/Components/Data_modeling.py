from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score,mean_squared_error
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
import joblib
from CancerML import logger
from pathlib import Path
from CancerML.Entity.Config_Entity import DataModelingConfig
import pandas as pd
import numpy as np


class DataModeling:
    def __init__(self,config=DataModelingConfig):
        self.config=config
    def Train_Model(self):
        file =Path(self.config.data_load_path)
        if file.name in self.config.all_required_files:
            validation_status=True
            with open(self.config.status_file,'w') as f:
                f.write(f"Validation Status : {validation_status}")
            
            logger.info(f" \n -------- Encoding the Categorical Features -------- ")
            df=pd.read_csv(file)
            df['train']=df['train'].astype(int)
            print(df.head(1))
            logger.info(f"\n ---------- Spliting the Data set into Train and Test ----------  \n")

            x=df.drop(columns='lpsa')
            y=df['lpsa']
            logger.info(f"--------- Scalling Data set ---------")
            scaler=StandardScaler()
            X=scaler.fit_transform(x)
            x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=.2,random_state=11)
            

            model=LinearRegression()
            model.fit(x_train,y_train)
            pred=model.predict(x_test)

            logger.info(f" Old Model R2-Score :{r2_score(y_test,pred)}")
            logger.info(f" Old Model MSE      :{mean_squared_error(y_test,pred)}")

            logger.info(f" ---------Ridge Regression -------")
            rmodel=Ridge(alpha=0.01)
            rmodel.fit(x_train,y_train)
            rpred=rmodel.predict(x_test)
            logger.info(f" Ridge Old Model R2-Score :{r2_score(y_test,rpred)}")
            logger.info(f" Ridge Old Model MSE      :{mean_squared_error(y_test,rpred)}")


            logger.info(f"---------- Lasso Regression -----------")
            lmodel=Lasso(alpha=0.01)
            lmodel.fit(x_train,y_train)
            lpred=lmodel.predict(x_test)
            logger.info(f" Lasso Old Model R2-Score :{r2_score(y_test,lpred)}")
            logger.info(f" Lasso Old Model MSE      :{mean_squared_error(y_test,lpred)}")

            logger.info(f" ----- MODEL DEPLOYMENT (SAVE MODEL) ---- ")
            full_path=Path(self.config.local_data_path)
            save_dir = full_path.parent
            model_path = save_dir / "old_prostate_model.pkl"
            scaler_path = save_dir / "old_scaler.pkl"
            joblib.dump(model, model_path)
            joblib.dump(scaler, scaler_path)
            

            print("MODEL DEPLOYED SUCCESSFULLY")

        else:
            logger.info(f"There is no csv file exist in source path")
    
