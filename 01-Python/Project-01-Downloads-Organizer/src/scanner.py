
def scanner(source_path):
    if source_path.exists():
        for item in source_path.iterdir():
            if item.is_file():
                yield item
    else:
        print(f"Path does not exist: {source_path}")