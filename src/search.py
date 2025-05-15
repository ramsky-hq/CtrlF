import argparse

def search(folder_path:str, search_string: str, exact_match: bool, ignore_case:bool, type:str):
    """
    search the cache and return a list of column names
    """
    print(f"folder_path: {folder_path}")
    print(f"search_string: {search_string}")
    print(f"exact_match: {exact_match}")
    print(f"ignore_case: {ignore_case}")
    print(f"type: {type}")