import argparse

def cache(name: str, folder_path: str, server_name: str, database: str, userid:str, password:str):
    """
    Will generate a cache of given database in the provided directory 
    """
    print(f"name: {name}")
    print(f"folder_path: {folder_path}")
    print(f"server_name: {server_name}")
    print(f"database: {database}")
    print(f"userid: {userid}")
    print(f"password: {password}")