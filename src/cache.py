import os
import shutil
import duckdb
from datetime import datetime

def initialize_cache_database():
    """
    Creates an in-memory DuckDB instance and initializes the required tables for caching
    """
    # Create in-memory DuckDB instance
    con = duckdb.connect(database=':memory:')
    
    # Create Columns table
    con.execute("""
        CREATE TABLE IF NOT EXISTS Columns (
            column_id INTEGER PRIMARY KEY AUTOINCREMENT,
            schemaname TEXT,
            tablename TEXT,
            columnname TEXT,
            columndatatype TEXT CHECK (columndatatype IN ('text', 'integer', 'decimal')),
            max_character_length INTEGER
        )
    """)
    
    # Create CacheFailures table
    con.execute("""
        CREATE TABLE IF NOT EXISTS CacheFailures (
            column_id INTEGER,
            error_details TEXT,
            datetime TIMESTAMP,
            FOREIGN KEY (column_id) REFERENCES Columns(column_id)
        )
    """)
    
    # Create CacheDetails table
    con.execute("""
        CREATE TABLE IF NOT EXISTS CacheDetails (
            cache_name TEXT,
            machine_name TEXT,
            start_time TIMESTAMP,
            end_time TIMESTAMP,
            server_name TEXT,
            database_name TEXT,
            user_id TEXT
        )
    """)
    
    return con


def cache(name: str, folder_path: str, server_name: str, database: str, userid:str, password:str):
    """
    Will generate a cache of given database in the provided directory 
    """
    if not os.path.isdir(folder_path):
        raise ValueError(f"The folder_path '{folder_path}' is not a valid directory.")
    cache_dir = os.path.join(folder_path, name)
    if os.path.exists(cache_dir):
        shutil.rmtree(cache_dir)
    os.makedirs(cache_dir)
    