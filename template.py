import logging
import os
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    ".env",
    "requirements.txt",
    "setup.py",
    "app.py",
    "research/trials.ipynb"
]


for filepath in list_of_files:
    filepath = Path(filepath)  # Convert string path to a Path object
    filedir, filename = os.path.split(filepath)  # Separate directory and filename

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  # Create directories if they don't exist
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:  # Create empty file if it does not exist
            pass
        logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")
