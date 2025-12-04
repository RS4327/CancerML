from pathlib import Path
import os
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    root_dir:Path
    source_url:Path
    local_data_file:Path

@dataclass
class DataValidationConfig:
    root_dir:Path
    data_load_path:Path
    local_data_path:Path
    STATUS_FILE:Path
    ALL_REQUIRED_FILES:list

@dataclass
class DataPreProcessingConfig:
    root_dir:Path
    data_load_path:Path
    local_data_path:Path
    status_file:Path
    all_required_files:list

