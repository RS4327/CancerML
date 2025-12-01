import os
import sys
import yaml
import json
import joblib
from pathlib import Path
from ensure import ensure_annotations
from box import Box
from box.exceptions import BoxValueError
from CancerML import logger


# Safer path change (optional)
os.chdir(r"C:\Users\RSR\PYTHON\LinearRegression")


class ConfigBox(Box):
    def __getattr__(self, item):
        if item not in self:
            raise AttributeError(f"Key '{item}' not found in ConfigBox.")
        return super().__getattr__(item)


# ------------------- FIXED YAML READER -------------------
@ensure_annotations
def Read_Yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml, "r", encoding="utf-8-sig") as yaml_file:
            content = yaml.safe_load(yaml_file)

        if not isinstance(content, dict):
            raise ValueError(f"YAML must contain a dictionary, got {type(content)}")

        logger.info(f"YAML loaded successfully: {path_to_yaml}")
        return ConfigBox(content)

    except FileNotFoundError:
        raise FileNotFoundError(f"YAML file does not exist → {path_to_yaml}")
    except BoxValueError:
        raise ValueError("YAML content invalid for Box conversion")
    except Exception as e:
        raise e


# ------------------- DIRECTORY CREATION -------------------
@ensure_annotations
def create_directories(paths: list, verbose=True):
    for path in paths:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created: {path}")


# ------------------ FILE SIZE CHECK ------------------
@ensure_annotations
def get_size(path: Path) -> str:
    size_kb = round(os.path.getsize(path) / 1024)
    return f"~{size_kb} KB"
