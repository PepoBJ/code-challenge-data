import os
from dotenv import load_dotenv

load_dotenv()

HOST=os.getenv('HOST')
DEBUG = bool(os.getenv('DEBUG'))
CONNECTION_STRING = os.getenv('CONNECTION_STRING_AZURE_SQL')
PORT = int(os.getenv('PORT', '5000'))
