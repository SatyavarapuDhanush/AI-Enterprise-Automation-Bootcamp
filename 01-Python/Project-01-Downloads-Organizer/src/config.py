import json
import csv
from pathlib import Path

def configure(current_path : Path):
    config_path = current_path / "config.json"
    csv_path = current_path / "support.csv"

    with open(config_path,'r',encoding='utf-8') as f:
        config=json.load(f)

    source_path = current_path / config['source_folder']

    extension_map = {}
    with open(csv_path,'r',encoding='utf-8') as read_file:
        reader=csv.DictReader(read_file)
        for row in reader: 
            extension_map[row['FILE_EXTENSION'].lower()] = row['DESTINATION_FOLDER']
    
    return source_path, extension_map