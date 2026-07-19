from pathlib import Path
from src.config import configure
from src.scanner import scanner
from src.mover import move_file
from src.logger import log_start, log_error, log_file_found, log_move
from src.report import generate_summary_report

def main():
    current_path = Path(__file__).parent

    config, extension_map = configure(current_path)
    source_path = current_path / config
    if not current_path.exists():
        log_error(f"Current path does not exist: {current_path}")
        return
    
    log_start(source_path)
    files_to_process= list(scanner(source_path))
    execution_history = []

    for item in files_to_process:
        log_file_found(item)
        result = move_file(item, source_path, extension_map)
        log_move(item, source_path / result['destination'])
        execution_history.append(result)

    generate_summary_report(execution_history)

if __name__ == "__main__":
    main()






# import json
# from pathlib import Path
# import csv
# import shutil

# current_path = Path(__file__).parent
# config_path = current_path / "config.json"
# csv_path = current_path / "support.csv"

# with open(config_path,'r',encoding='utf-8') as f:
#     config=json.load(f)

# source_path = current_path / config['source_folder']

# extension_map = {}
# with open(csv_path,'r',encoding='utf-8') as read_file:
#     reader=csv.DictReader(read_file)
#     for row in reader: 
#         extension_map[row['FILE_EXTENSION'].lower()] = row['DESTINATION_FOLDER']

# if source_path.exists():
#     print(f"Path exists: {source_path}")
#     for item in source_path.iterdir():
#         if item.is_file():
#             print(f"File: {item.name} and {item.suffix}")
#             if item.suffix.lower() in extension_map:
#                 destination_name = extension_map.get(item.suffix.lower(), "unknown")
#                 destination_path = source_path / destination_name
#                 destination_path.mkdir(parents=True, exist_ok=True)
#                 shutil.move(str(item), str(destination_path/item.name))
#             else:
#                 destination_name="unknown"
#                 destination_path =  source_path / destination_name
#                 destination_path.mkdir(parents=True, exist_ok=True)
#                 shutil.move(str(item), str(destination_path/item.name))
# else:
#     print(f"Path does not exist: {source_path}")
