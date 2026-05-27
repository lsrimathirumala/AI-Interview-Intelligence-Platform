from fastapi import FastAPI, UploadFile, File, Depends
from sqlalchemy.orm import Session
import os
import shutil

from database import SessionLocal, Base, engine
from models import Interview
import models

Base.metadata.create_all(bind=engine)

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "AI Interview Intelligence Platform Backend Running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/upload")
def upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    interview = Interview(
        filename=file.filename,
        file_path=file_path,
        content_type=file.content_type
    )

    db.add(interview)
    db.commit()
    db.refresh(interview)

    return {
        "message": "File uploaded successfully",
        "interview_id": interview.id,
        "filename": interview.filename,
        "content_type": interview.content_type,
        "saved_path": interview.file_path,
        "uploaded_at": str(interview.uploaded_at)
    }