import json
from pathlib import Path
import csv
import shutil

current_path = Path(__file__).parent
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

if source_path.exists():
    print(f"Path exists: {source_path}")
    for item in source_path.iterdir():
        if item.is_file():
            print(f"File: {item.name} and {item.suffix}")
            if item.suffix.lower() in extension_map:
                destination_name = extension_map.get(item.suffix.lower(), "unknown")
                destination_path = source_path / destination_name
                destination_path.mkdir(parents=True, exist_ok=True)
                shutil.move(str(item), str(destination_path/item.name))
            else:
                destination_name="unknown"
                destination_path =  source_path / destination_name
                destination_path.mkdir(parents=True, exist_ok=True)
                shutil.move(str(item), str(destination_path/item.name))
else:
    print(f"Path does not exist: {source_path}")
