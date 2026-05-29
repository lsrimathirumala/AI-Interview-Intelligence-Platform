from fastapi import FastAPI, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal, Base, engine
from models import Interview
import models
import os
import shutil
import imageio_ffmpeg

ffmpeg_path = imageio_ffmpeg.get_ffmpeg_exe()
ffmpeg_dir = os.path.dirname(ffmpeg_path)

os.environ["PATH"] = ffmpeg_dir + os.pathsep + os.environ["PATH"]

import whisper


Base.metadata.create_all(bind=engine)

app = FastAPI()
whisper_model = whisper.load_model("base")

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/ffmpeg-check")
def ffmpeg_check():
    return {
        "ffmpeg_path": ffmpeg_path,
        "ffmpeg_exists": os.path.exists(ffmpeg_path),
        "ffmpeg_dir": ffmpeg_dir
    }

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
                "uploaded_at": str(interview.uploaded_at),
                "transcript": interview.transcript,
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
        "uploaded_at": str(interview.uploaded_at),
        "transcript": interview.transcript,
    }

@app.post("/interviews/{interview_id}/transcribe")
def transcribe_interview(interview_id: int, db: Session = Depends(get_db)):
    interview = db.query(Interview).filter(Interview.id == interview_id).first()

    if interview is None:
        raise HTTPException(status_code=404, detail="Interview not found")

    if not os.path.exists(interview.file_path):
        raise HTTPException(status_code=404, detail="Audio file not found")

    result = whisper_model.transcribe(interview.file_path)

    interview.transcript = result["text"]
    db.commit()
    db.refresh(interview)

    return {
        "message": "Transcription completed successfully",
        "interview_id": interview.id,
        "filename": interview.filename,
        "transcript": interview.transcript
    }
