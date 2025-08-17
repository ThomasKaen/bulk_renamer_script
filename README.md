# 🧾 Bulk File Renamer (Script Version)

A simple yet powerful Python script to batch rename files in a folder using fully customizable rules.

Whether you want to organize photos, clean up messy filenames, or apply consistent naming across large batches of files — this tool gets it done.

---

## ⚙️ Features

- ✅ Add **prefix** and **suffix** to filenames
- 📆 Optionally prepend the file's **creation date**
- 🔁 Perform **find & replace** in filenames
- 🔡 Convert filenames to **lowercase** or **UPPERCASE**
- 🔍 Run in **Preview Mode** to see changes before applying
- 📝 Saves a **CSV log file** with old vs. new filenames

---

## 🛠️ How to Use

1. Edit the script and set your desired options in the **Configuration** section:
   
   FOLDER_PATH = "SampleFiles"      # Folder containing files to rename
   PREVIEW_MODE = True              # False = actually rename, True = dry-run
   ADD_PREFIX = "IMG_"
   ADD_SUFFIX = "_edited"
   REPLACE_FROM = "_copy"
   REPLACE_TO = ""
   ADD_DATE = True
   FILENAME_CASE = "lower"          # Options: "lower", "upper", or None
   

2. Place your target files in the specified folder.

3. Run the script:
   python bulk_renamer.py

4. Check the terminal output and `rename_log.csv` for preview or confirmation.

---

## 📁 Example

**Before:**
holiday_photo_copy.JPG
document_copy.txt

**After:**

2025-08-07_img_holiday_photo_edited.jpg
2025-08-07_img_document_edited.txt


---

## 🧠 Preview Mode

To safely test changes before renaming files, set:

PREVIEW_MODE = True

No files will be renamed — only `rename_log.csv` will be created to show what *would* happen.

---

## 💡 Why Use This?

This script is ideal for:
- Organizing thousands of files in seconds
- Prepping folders for uploads, archives, or print
- Cleaning up naming issues from exports or downloads

---

📜 **License**: All Rights Reserved © 2025 ThomasKaen  
This project is for personal/portfolio use only.  
For commercial use or custom solutions, please contact me via [Fiverr](https://www.fiverr.com/thomas_kaen).
---

**Need a visual interface (GUI) instead of a script?**
Check out the [Bulk File Renamer GUI Version](https://github.com/yourusername/bulk_renamer_gui) (coming soon!)
