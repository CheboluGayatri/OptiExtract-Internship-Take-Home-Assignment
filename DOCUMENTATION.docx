1. Project Overview & Rationale

Project Name: OptiExtract File Uploader

The OptiExtract File Uploader is a web application designed to allow users to upload various types of files (documents, PDFs, videos, etc.), store them securely on the server, and maintain metadata about each file in a database. The project demonstrates backend handling with FastAPI, frontend interfacing with HTML, CSS, and JS, and database management with SQLite via SQLAlchemy.Folder Structure & Design Choices
Folder/File	Purpose
main.py	Entry point of the FastAPI application. Handles routing, file uploads, and API endpoints.
database.py	Manages the SQLite database connection and session handling.
models.py	Contains SQLAlchemy models representing the file metadata table.
schemas.py	Defines Pydantic schemas to validate request and response data.
requirements.txt	Lists all required Python dependencies for local setup.
static/	Holds static frontend files (CSS, JS, HTML templates).
uploaded_files/	Directory to store uploaded files on the server.
.venv/	Virtual environment for Python dependencies (not committed in production).Rationale:

Clear separation of backend (FastAPI, database models) and frontend (static folder) ensures maintainability.

Using uploaded_files/ for physical files and a database for metadata ensures synchronization and prevents data loss.

SQLAlchemy and Pydantic were chosen for reliability and automatic validation of data.2. Local Setup Guide (The "How-To")

Follow these steps to run the project locally:

Step 1: Clone the Repository
git clone https://github.com/CheboluGayatri/OptiExtract-Internship-Take-Home-Assignment.git
cd OptiExtract-Internship-Take-Home-Assignment
Step 2: Create a Virtual Environment
python -m venv .venv
Activate the environment:
Windows PowerShell
.venv\Scripts\Activate.ps1
Windows CMD
.venv\Scripts\activate.bat
Linux/macOS
source .venv/bin/activate
Step 3: Install Dependencies
pip install -r requirements.txt
Dependencies included:

fastapi – Backend web framework

uvicorn – ASGI server for running FastAPI

SQLAlchemy – ORM for database management

python-multipart – Handle file uploads

pydantic – Data validation

aiofiles – Async file operations
Step 4: Create & Initialize the Database

The database is automatically created if it does not exist when running the app. The SQLite file files.db will store metadata including:

Original filename

Unique system filename

Upload timestamp

File type
Step 5: Run the Application
uvicorn main:app --reload
Open your browser and navigate to:
http://127.0.0.1:8000
Step 6: Frontend Interaction
upload.html – Interface for uploading files.

files.html – View uploaded files and metadata.

Basic CSS (styles.css) ensures a clean, user-friendly layout.

JS files handle file submission asynchronously for better UX.

3. Key Implementation Details
3.1 Unique System Filenames

Each uploaded file is assigned a unique system filename using uuid.uuid4() to prevent collisions and overwrite issues. This ensures that multiple files with the same original name can coexist in the uploaded_files/ directory.
import uuid
system_filename = f"{uuid.uuid4().hex}.{file_extension}"
3.2 File & Database Synchronization

To maintain consistency:

File is saved physically to the uploaded_files/ folder.

Metadata is inserted into the SQLite database after successful file save.

This order prevents database entries pointing to non-existent files and avoids orphaned files.
file_location = f"uploaded_files/{system_filename}"
await file.save(file_location)
new_file = FileModel(original_name=filename, system_name=system_filename)
db.add(new_file)
db.commit()
Challenges & Solutions
Challenge: Handling large files (>50 MB) when pushing to GitHub.
Solution: Used Git Large File Storage (Git LFS) to track .mp4 and .exe files.

Challenge: Synchronization between filesystem and database.
Solution: Implemented a transactional approach—only commit metadata if file save succeeds.

Challenge: Preventing filename collisions.
Solution: Used UUID-based system filenames for uniqueness.
4. Adaptation & Aesthetics 
Frontend Design

Minimalist and functional design ensures easy navigation.

CSS provides consistent styling for buttons, input fields, and file lists.

Responsive layout allows basic mobile compatibility.

Code Commenting

Python files contain inline comments explaining:

API endpoints

Database operations

File handling logic

JS files have comments describing asynchronous file upload flow.

Use of AI Tools

FastAPI boilerplate code and initial CSS design were refined with the help of AI suggestions to speed up setup.

Comments and documentation were enhanced using AI for clarity.

5. Conclusion

This project demonstrates a fully functional file upload system using FastAPI, SQLite, and static frontend files. Key features include:

Unique system filenames for safe file storage

Synchronized database metadata

Handling of large files using Git LFS

Clean and functional frontend with basic CSS styling

Well-commented code for maintainability

The design ensures scalability and adaptability for future enhancements like authentication, AI-based file processing, or cloud storage integration.
