import os 
from pathlib import Path
import logging 

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s')


project_name="CancerML"

list_files=[

    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/Components/__init__.py",
    f"src/{project_name}/Config/__init__.py",
    f"src/{project_name}/Constraints/__init__.py",
    f"src/{project_name}/Entity/__init__.py",
    f"src/{project_name}/Utils/__init__.py",
    "Config/Config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirments.txt",
    "setup.py",
    "Research/trails.ipynb",
    "Templates/index.html",
    "app.py"

]



for filepath in list_files:
    filepath=Path(filepath)
    print(f" File path {filepath}")
    filedir,filename =os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating the Directory :{filedir} for the file name :{filename} ")
    if (not  os.path.exists(filepath) or os.path.getsize==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating the Empty File : {filepath}")
    else:
        logging.info(f"{filename} is already exists")

