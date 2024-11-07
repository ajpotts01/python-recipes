import json

def import_recipes(data_path: str) -> list[dict]:
    result: list[dict] = []

    with open(data_path, "r") as f:
        result = json.load(f)

    return result