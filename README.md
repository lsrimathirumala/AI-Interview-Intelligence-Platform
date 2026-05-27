# AI Interview Intelligence Platform

An AI-powered platform that analyzes mock interview responses using speech-to-text, NLP evaluation, semantic analysis, and progress analytics.

---

## Features

- Audio/video interview upload
- Persistent interview metadata storage
- Speech-to-text transcription pipeline
- NLP-based answer evaluation
- Semantic similarity analysis
- Progress tracking dashboard
- Async processing pipeline
- Interview feedback reports

---

## Tech Stack

### Frontend
- React
- Tailwind CSS

### Backend
- FastAPI
- Python

### Database
- SQLite (development)
- PostgreSQL / Supabase (planned production migration)

### AI/NLP
- Whisper
- Sentence Transformers
- FAISS

### Async Processing
- Celery
- Redis

### DevOps
- Docker
- GitHub Actions

---

## Current Progress

### Phase 1 — Backend MVP

#### Completed
- [x] FastAPI backend setup
- [x] Health check endpoint
- [x] File upload API
- [x] Persistent database integration
- [x] Local file storage pipeline
- [x] SQLite development database setup
- [x] SQLAlchemy ORM integration

#### In Progress
- [ ] Whisper transcription pipeline
- [ ] Interview retrieval APIs
- [ ] NLP evaluation engine
- [ ] Async job processing
- [ ] Frontend dashboard

---

## Current Architecture

```text
Client → FastAPI Backend → SQLite Database
                        → Local File Storage
```

Planned production architecture:

```text
Frontend → FastAPI Backend → PostgreSQL/Supabase
                          → Cloud Object Storage
                          → Async Workers
```

---

## Project Goal

The platform helps users improve interview performance through AI-generated feedback, transcript analysis, semantic evaluation, and personalized progress tracking.

---

## Engineering Goals

- Build production-style backend architecture
- Implement scalable async processing
- Explore semantic evaluation pipelines
- Design measurable AI feedback systems
- Practice full-stack system design concepts

---

## Future Improvements

- Real-time interview analysis
- Emotion/confidence detection
- Personalized interview recommendations
- AI-generated improvement suggestions
- Cloud deployment
- Authentication and user management
- RAG-based interview evaluation
- Advanced analytics dashboard
