"""
This file is responsible for accessing variables in the .env and making them available globally 
"""

from dotenv import load_dotenv
import os

load_dotenv()

INSTANCE = os.getenv("INSTANCE")
TOKEN = os.getenv("CANVAS_API_TOKEN")
