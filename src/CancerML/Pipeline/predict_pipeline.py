import pandas as pd
import numpy as np
import os 
from CancerML import logger
from CancerML.Utils.common import load_object
import sys 


class ModelPreidctPipeline:
    def __init__(self):
        self.model_path="artifacts/data_modeling/final_model.pkl"
        self.preprocessor_path="artifacts/data_modeling/preprocessor.pkl"


    def predict(self, features):
        try:
            model = load_object(self.model_path)
            preprocessor = load_object(self.preprocessor_path)
            print("Preprocessor Type:", type(preprocessor))  # DEBUG
            #data_scaled = preprocessor.transform(features)
            ##data_scaled = preprocessor.transform(features.values)
            data_scaled = preprocessor.transform(features.to_numpy())
            preds = model.predict(data_scaled)
            return preds

        except Exception as e:
            raise e

    
# class custom_data:
#     def __init__(
            
#             self,
#             lcavol : float, 
#             lweight: float,
#             age: float,	   
#             lbph: float,	
#             svi : float,	   
#             lcp : float,	   
#             gleason : float,
#             pgg45 : float,	
#             train : bool
#     ):
        
#         self.lcavol  = float(lcavol)
#         self.lweight = float(lweight)
#         self.age     = float(age)
#         self.lbph    = float(lbph)
#         self.svi     = float(svi)
#         self.lcp     = float(lcp)
#         self.gleason = float(gleason)
#         self.pgg45   = float(pgg45)
#         self.train   = int(train)
#     def get_data_as_frame_data(self):
#         try:
#             custom_data_input_dict={
#                 'lcavol':[self.lcavol],
#                 'lweight':[self.lweight],
#                 'age':[self.age],
#                 'lbph':[self.lbph],
#                 'svi':[self.svi],
#                 'lcp':[self.lcp],
#                 'gleason':[self.gleason],
#                 'pgg45':[self.pgg45],
#                 'train':[self.train] 

#             }
            
#             return pd.DataFrame(custom_data_input_dict)
#         except Exception as e:
#             raise e


class custom_data:
    def __init__(self, lcavol, lweight, age, lbph, svi, lcp, gleason, pgg45, train, lpsa=None):
        self.lcavol  = float(lcavol)
        self.lweight = float(lweight)
        self.age     = float(age)
        self.lbph    = float(lbph)
        self.svi     = float(svi)
        self.lcp     = float(lcp)
        self.gleason = float(gleason)
        self.pgg45   = float(pgg45)
        self.train   = int(train)
        self.lpsa    = float(lpsa) if lpsa is not None else None

    def get_data_as_frame_data(self):
        data_dict = {
            'lcavol':[self.lcavol],
            'lweight':[self.lweight],
            'age':[self.age],
            'lbph':[self.lbph],
            'svi':[self.svi],
            'lcp':[self.lcp],
            'gleason':[self.gleason],
            'pgg45':[self.pgg45],
            'train':[self.train]
        }
        if self.lpsa is not None:
            data_dict['lpsa'] = [self.lpsa]
        return pd.DataFrame(data_dict)


