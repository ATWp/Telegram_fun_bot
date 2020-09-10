import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
DATA_PHRASES_PATH = os.getenv("DATA_PHRASES_PATH")
DATA_FOLDER = os.getenv("DATA_FOLDER")
FOLDER_PICTURES = os.getenv("FOLDER_PICTURES")
CHANNEL_PUBLIC_ID = os.getenv("CHANNEL_PUBLIC_ID")
RESOURCE_FONT = os.getenv("RESOURCE_FONT")