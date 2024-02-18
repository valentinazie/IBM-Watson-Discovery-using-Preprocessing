import json
from typing import List, Dict

def save_json(data: Dict, file_path: str) -> None:
    """
    Save data to a JSON file.

    Parameters:
    data (dict): Data to be saved.
    file_path (str): Path to the file where data should be saved.
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent='\t')