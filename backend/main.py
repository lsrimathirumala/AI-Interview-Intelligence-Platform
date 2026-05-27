from fastapi import FastAPI, UploadFile, File
import os
import shutil

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
def home():
    return {"message": "AI Interview Intelligence Platform Backend Running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/upload")
def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "message": "File uploaded successfully",
        "filename": file.filename,
        "content_type": file.content_type,
        "saved_path": file_path
    }