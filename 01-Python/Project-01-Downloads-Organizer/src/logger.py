from pathlib import Path

def log_start(source_path:Path):
    print(f"Path exists: {source_path}")

def log_error(message: str):
    print(message)

def log_file_found(item: Path):
    print(f"File: {item.name} and {item.suffix}")

def log_move(item:Path, destination_path: Path):
    print(f"Moved {item.name} to {destination_path}")
    