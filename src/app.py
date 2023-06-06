import sys
import config
from flask import Flask
from database.create_structure import create_tables

def main():
    if len(sys.argv) > 1 and sys.argv[1] == 'db_init':
        create_tables(config.CONNECTION_STRING)

if __name__ == "__main__":
    main()