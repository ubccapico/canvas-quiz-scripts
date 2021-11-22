"""
This file is responsible for defining/initializing global variables.
"""

from dotenv import load_dotenv
import os

load_dotenv()

INSTANCE = os.getenv("INSTANCE")
TOKEN = os.getenv("CANVAS_API_TOKEN")