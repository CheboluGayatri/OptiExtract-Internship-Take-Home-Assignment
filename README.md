OptiExtract File Uploader
A FastAPI-based web app to upload, store, and manage files securely with metadata tracking.

🚀 Features

Upload multiple file types: PDF, DOCX, MP4, EXE, etc.

Unique system filenames to prevent collisions using UUID.

Metadata storage in SQLite (files.db) for original name, system name, type, and upload timestamp.

Clean, responsive frontend with HTML, CSS, and JS.

Handles large files efficiently using Git LFS for version control.

📁 Project Structure
.
├── main.py           # FastAPI app entry point
├── database.py       # SQLite DB connection
├── models.py         # SQLAlchemy models
├── schemas.py        # Pydantic schemas
├── requirements.txt  # Dependencies
├── static/           # Frontend HTML, CSS, JS
├── uploaded_files/   # Saved user files
├── .venv/            # Python virtual environment

⚙️ Local Setup

Clone repo:

git clone https://github.com/CheboluGayatri/OptiExtract-Internship-Take-Home-Assignment.git
cd OptiExtract-Internship-Take-Home-Assignment


Create virtual environment:

python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\Activate.ps1 # Windows PowerShell


Install dependencies:

pip install -r requirements.txt


Run the app:

uvicorn main:app --reload


Access frontend:

http://127.0.0.1:8000

💡 How It Works

Files are saved physically in uploaded_files/.

Metadata is inserted into SQLite after successful file save to ensure synchronization.

Unique filenames (UUID) prevent collisions even if users upload files with the same name.

🎨 Design & Adaptability

Minimal, functional frontend with basic CSS for clean UI.

JS handles asynchronous uploads for smooth UX.

AI tools were used for boilerplate generation and styling suggestions.

Code is well-commented for maintainability and future enhancements.

🛠 Challenges & Solutions

Large files (>50MB) → Used Git LFS.

Filename collisions → Used UUID system names.

DB/File sync → Ensured transactional save: file first, DB second.

📌 Dependencies

fastapi

uvicorn

SQLAlchemy

python-multipart

pydantic

aiofiles

✨ Conclusion

OptiExtract is a robust, scalable file upload system with unique filenames, database metadata tracking, a clean frontend, and Git LFS support for large files. Perfect for demonstrating backend, frontend, and database integration in a professional project.
