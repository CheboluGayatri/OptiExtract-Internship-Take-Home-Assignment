from pydantic import BaseModel
from datetime import datetime

class FileRecordBase(BaseModel):
    original_filename: str
    system_filename: str
    file_size_bytes: int
    uploaded_at: datetime

    class Config:
        orm_mode = True

class FileListResponse(BaseModel):
    files: list[FileRecordBase]
