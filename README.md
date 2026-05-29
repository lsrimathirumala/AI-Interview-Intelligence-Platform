# AI Interview Intelligence Platform

An AI-powered interview evaluation platform that processes mock interview recordings, generates transcripts using Whisper, and provides structured feedback through NLP-based evaluation pipelines.

---

## Overview

The AI Interview Intelligence Platform helps users improve their interview performance by analyzing recorded responses, generating transcripts, evaluating answer quality, and tracking progress over time.

The long-term vision is to build a production-ready interview coaching system capable of:

* Interview transcription
* Semantic answer evaluation
* Feedback generation
* Progress tracking
* Personalized learning recommendations
* Analytics dashboards

---

## Features

### Current Features

* Audio interview upload
* Persistent interview metadata storage
* Interview retrieval APIs
* Individual interview lookup
* Whisper-based speech-to-text transcription
* Transcript persistence in database
* Local file storage
* SQLite-backed development environment

### Planned Features

* Interview evaluation engine
* Keyword coverage analysis
* Semantic similarity scoring
* Filler word detection
* AI-generated feedback
* Progress analytics dashboard
* Authentication and user management
* Async processing pipeline
* Cloud deployment

---

## Tech Stack

### Frontend (Planned)

* React
* Tailwind CSS

### Backend

* FastAPI
* Python

### Database

* SQLite (Development)
* PostgreSQL / Supabase (Production)

### AI / NLP

* OpenAI Whisper
* Sentence Transformers (Planned)
* FAISS (Planned)

### Async Processing (Planned)

* Celery
* Redis

### DevOps (Planned)

* Docker
* GitHub Actions

---

## Current Architecture

```text
Client
  │
  ▼
FastAPI Backend
  │
  ├── Upload Audio
  ├── Retrieve Interviews
  ├── Retrieve Interview by ID
  └── Transcribe Interview
          │
          ▼
      Whisper
          │
          ▼
      Transcript
          │
          ▼
SQLite Database

Audio Files
      │
      ▼
Local Storage (uploads/)
```

---

## Available API Endpoints

### Health Check

```http
GET /health
```

Returns service status.

---

### Upload Interview

```http
POST /upload
```

Uploads an audio file and stores metadata in the database.

#### Response

```json
{
  "message": "File uploaded successfully",
  "interview_id": 1,
  "filename": "sample-speech-1m.mp3"
}
```

---

### Get All Interviews

```http
GET /interviews
```

Returns all uploaded interviews.

---

### Get Interview By ID

```http
GET /interviews/{id}
```

Returns a single interview record.

---

### Transcribe Interview

```http
POST /interviews/{id}/transcribe
```

Generates a transcript using Whisper and stores it in the database.

---

## Current Progress

### Phase 1 — Backend MVP

#### Completed

* [x] FastAPI backend setup
* [x] Health check endpoint
* [x] File upload API
* [x] Persistent database integration
* [x] SQLite development database setup
* [x] SQLAlchemy ORM integration
* [x] Interview retrieval API (`GET /interviews`)
* [x] Individual interview lookup API (`GET /interviews/{id}`)
* [x] Whisper transcription pipeline
* [x] Transcript persistence in database
* [x] Local file storage pipeline

#### In Progress

* [ ] Interview evaluation engine
* [ ] Transcript analysis and scoring
* [ ] Evaluation result persistence
* [ ] Async job processing
* [ ] Frontend dashboard
* [ ] Authentication and user management

---

## Learning Goals

This project is being built to gain hands-on experience in:

* Backend engineering
* API design
* Database design
* AI inference pipelines
* NLP systems
* Full-stack development
* Scalable system architecture
* Production deployment practices

---

## Future Roadmap

### Phase 2

* Evaluation engine v1
* Keyword coverage scoring
* Missing concept detection
* Filler word detection

### Phase 3

* Semantic similarity scoring
* Embedding generation
* FAISS vector search
* Structured feedback generation

### Phase 4

* User authentication
* Interview history dashboard
* Analytics and insights

### Phase 5

* Async processing with Celery
* Redis task queue
* Dockerized deployment
* Cloud infrastructure

---

## Project Status

🚧 Actively under development

Current milestone:
**End-to-end audio upload → transcription → database persistence pipeline completed.**
