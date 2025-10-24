from fastapi import FastAPI, UploadFile, File, HTTPException, Depends
from fastapi.responses import JSONResponse, FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import os, uuid, datetime

from database import Base, engine, get_db
import models

# Create DB tables if they don't exist
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Opti File Uploader")

# Directories
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(ROOT_DIR, "static")
UPLOAD_DIR = os.path.join(ROOT_DIR, "uploaded_files")
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Serve static frontend
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload-document")
async def upload_document(file: UploadFile = File(...), db: Session = Depends(get_db)):
    if not file.filename:
        raise HTTPException(status_code=400, detail="No filename provided")

    orig_name = file.filename
    _, ext = os.path.splitext(orig_name)
    unique_name = f"{uuid.uuid4().hex}{ext}"
    dest_path = os.path.join(UPLOAD_DIR, unique_name)

    try:
        content = await file.read()
        with open(dest_path, "wb") as out_file:
            out_file.write(content)
        size = len(content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save file: {e}")

    record = models.FileRecord(
        original_filename=orig_name,
        system_filename=unique_name,
        file_size_bytes=size,
        uploaded_at=datetime.datetime.utcnow(),
    )
    db.add(record)
    db.commit()
    db.refresh(record)

    return JSONResponse({
        "message": "File uploaded successfully",
        "file": {
            "original_filename": record.original_filename,
            "system_filename": record.system_filename,
            "file_size_bytes": record.file_size_bytes,
            "uploaded_at": record.uploaded_at.isoformat(),
        },
    })

@app.get("/files")
def list_files(db: Session = Depends(get_db)):
    records = db.query(models.FileRecord).order_by(models.FileRecord.id.desc()).all()
    files = [
        {
            "original_filename": r.original_filename,
            "system_filename": r.system_filename,
            "file_size_bytes": r.file_size_bytes,
            "uploaded_at": r.uploaded_at.isoformat(),
        }
        for r in records
    ]
    return {"files": files}

@app.get("/", response_class=HTMLResponse)
def root():
    index_path = os.path.join(STATIC_DIR, "upload.html")
    if not os.path.exists(index_path):
        return HTMLResponse("<h1>Upload page not found</h1>", status_code=404)
    with open(index_path, "r", encoding="utf-8") as fh:
        return fh.read()

@app.get("/download/{system_filename}")
def download(system_filename: str):
    path = os.path.join(UPLOAD_DIR, system_filename)
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(path, filename=system_filename)
