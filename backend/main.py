from fastapi import FastAPI, UploadFile, File, Depends, HTTPException
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

@app.get("/interviews")
def get_interviews(db: Session = Depends(get_db)):
    interviews = db.query(Interview).order_by(Interview.uploaded_at.desc()).all()

    return {
        "count": len(interviews),
        "interviews": [
            {
                "id": interview.id,
                "filename": interview.filename,
                "file_path": interview.file_path,
                "content_type": interview.content_type,
                "uploaded_at": str(interview.uploaded_at)
            }
            for interview in interviews
        ]
    }

@app.get("/interviews/{interview_id}")
def get_interview(interview_id: int, db: Session = Depends(get_db)):
    interview = db.query(Interview).filter(Interview.id == interview_id).first()

    if interview is None:
        raise HTTPException(status_code=404, detail="Interview not found")

    return {
        "id": interview.id,
        "filename": interview.filename,
        "file_path": interview.file_path,
        "content_type": interview.content_type,
        "uploaded_at": str(interview.uploaded_at)
    }