import json
import os


def read_JSON_data(file_path: str) -> list:
    if os.path.exists(file_path):

        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)


    else:
        data = []
        print(f"файл {file_path} не существует")
    return data
