# OCR System Using Neural Networks (Django + Tesseract)

A simple Django web app that extracts text from an uploaded image using Tesseract OCR. The UI lets you upload an image, runs OCR server‑side, and displays both the image preview and extracted text.

## Features
- Image upload via a web form
- OCR extraction with `pytesseract`
- Preview of the uploaded image
- Display of the extracted text on the same page

## Tech Stack
- Python, Django
- Tesseract OCR + `pytesseract`
- Pillow, NumPy
- SQLite (default Django DB)

## Project Structure
- `OCR/` — Django project root
- `OCR/core/` — App with views, URLs, templates, and static assets
- `OCR/core/templates/core/index.html` — Main UI
- `OCR/core/static/style.css` — Styles

## Prerequisites
- Python 3.9+
- Tesseract OCR installed locally

### Install Tesseract OCR
- macOS (Homebrew): `brew install tesseract`
- Ubuntu/Debian: `sudo apt-get install tesseract-ocr`
- Windows: Install from the official installer, then ensure the path to `tesseract.exe` is correct

## Setup
1. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
2. Install Python dependencies:
   ```bash
   pip install django pytesseract pillow numpy
   ```
3. If Tesseract is not on your PATH, update the command path in `OCR/core/views.py`:
   ```python
   pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
   ```
   On macOS/Linux, you can usually omit this line if `tesseract` is in your PATH.

## Run
```bash
cd OCR
python manage.py migrate
python manage.py runserver
```
Open `http://127.0.0.1:8000/` in your browser and upload an image to extract text.

## Notes
- This project uses a simple synchronous OCR call in the request/response cycle. Large images may take longer to process.
- The database is SQLite by default (`OCR/db.sqlite3`).

## Troubleshooting
- If you see a `TesseractNotFoundError`, confirm Tesseract is installed and the path in `OCR/core/views.py` is correct.
- If uploads fail, ensure the form is sending `multipart/form-data` (already configured in the template).

