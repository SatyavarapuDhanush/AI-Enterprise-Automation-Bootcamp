import shutil
from pathlib import Path
from datetime import datetime

def move_file(item: Path, source_path: Path, extension_map: dict):
    file_suffix = item.suffix.lower()
    destination_name = extension_map.get(file_suffix, "unknown")
    destination_path = source_path / destination_name
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        destination_path.mkdir(parents=True, exist_ok=True)
        target_path = destination_path / item.name
        shutil.move(str(item), str(target_path))
        status = "Success"
    except Exception:
        status = "Failed"
        
    return {
        "file": item.name,
        "extension": item.suffix,
        "destination": destination_name,
        "status": status,
        "timestamp": timestamp
    }