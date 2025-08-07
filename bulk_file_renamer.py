
import os
import csv
import datetime
from pathlib import Path

# --- CONFIGURATION ---
FOLDER_PATH = "SampleFiles"  # Replace with your folder path
PREVIEW_MODE = True          # Set to False to apply changes

# Custom renaming options
ADD_PREFIX = "IMG_"
ADD_SUFFIX = "_edited"
REPLACE_FROM = "_copy"
REPLACE_TO = ""
ADD_DATE = True
FILENAME_CASE = "lower"  # Options: "lower", "upper", None

# Log output
LOG_FILE = "rename_log.csv"

# --- SCRIPT START ---
folder = Path(FOLDER_PATH)
renamed_files = []

for file in folder.iterdir():
    if file.is_file():
        old_name = file.name
        name, ext = os.path.splitext(old_name)

        # Apply replacement
        name = name.replace(REPLACE_FROM, REPLACE_TO)

        # Add prefix/suffix
        name = f"{ADD_PREFIX}{name}{ADD_SUFFIX}"

        # Add date
        if ADD_DATE:
            date_str = datetime.datetime.fromtimestamp(file.stat().st_ctime).strftime('%Y-%m-%d')
            name = f"{date_str}_{name}"

        # Apply case
        if FILENAME_CASE == "lower":
            name = name.lower()
        elif FILENAME_CASE == "upper":
            name = name.upper()

        new_name = f"{name}{ext}"
        new_path = file.with_name(new_name)

        # Log
        renamed_files.append((old_name, new_name))

        # Preview or execute
        if not PREVIEW_MODE:
            file.rename(new_path)

# Save log
with open(LOG_FILE, "w", newline="", encoding="utf-8") as log_file:
    writer = csv.writer(log_file)
    writer.writerow(["Old Filename", "New Filename"])
    writer.writerows(renamed_files)

print("Done. Check 'rename_log.csv' for the renaming preview or results.")
