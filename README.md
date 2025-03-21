# COINS PDF Extractor - Backend

This is the frontend for the COINS PDF Extractor, built for the Princeton University-based FLAME project.

## 🛠 Built With

- **Flask**
- **gmft**
- **ocrmypdf**
- **pywebview** 

## Features

- PDF ingestion
- Table extraction using gmft
- OCR preprocessing via ocrmypdf
- Preview image generation of tables
- Exporting selected tables to CSV

### How to use

To run locally:
```
pip install -r requirements.txt
python index.py
```

To export as an app:
```
pyinstaller --windowed --name "COINS PDF Extractor" --add-data "static:static" index.py
```