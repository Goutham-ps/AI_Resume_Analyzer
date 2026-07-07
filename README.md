# 📄 AI Resume Analyzer

> An AI-powered Resume Analyzer that evaluates resumes, extracts skills, performs ATS-style analysis, and provides personalized recommendations using a Streamlit frontend and FastAPI backend.

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red?logo=streamlit)
![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?logo=fastapi)
![Google Gemini](https://img.shields.io/badge/AI-Google%20Gemini-blueviolet)
![Render](https://img.shields.io/badge/Backend-Render-success?logo=render)

</p>

---

# 🚀 Live Demo

### 🌐 Streamlit Application

https://resume-analyzing.streamlit.app/

### ⚙️ FastAPI Backend

https://ai-resume-analyzer-api-gmbq.onrender.com/

### 📘 API Documentation

https://ai-resume-analyzer-api-gmbq.onrender.com/docs

---

# 📌 Project Overview

AI Resume Analyzer is a full-stack AI application designed to help job seekers evaluate and improve their resumes.

The application allows users to upload a PDF resume and analyze it in two different ways:

- 📋 Compare against a Job Description (ATS-style analysis)
- 💼 Compare against predefined job roles

The frontend is built using **Streamlit**, while the backend is powered by **FastAPI**. The backend handles resume parsing, skill extraction, semantic matching, and resume quality analysis before sending structured results back to the frontend.

---

# ✨ Features

- 📄 Upload Resume (PDF)
- 🤖 AI-powered Resume Analysis
- 📊 ATS Match Score
- 💼 Resume Skill Extraction
- ✅ Matched Skills Detection
- ❌ Missing Skills Identification
- 📈 Resume Quality Analysis
- 🎯 Role-Based Skill Matching
- ⚡ FastAPI REST API
- 🌐 Interactive Streamlit Interface

---

# 🏗️ System Architecture

```text
             User
               │
               ▼
      Streamlit Frontend
               │
      HTTP API Requests
               │
               ▼
      FastAPI Backend (Render)
               │
      Resume Processing Engine
               │
 ┌─────────────┼────────────────┐
 │             │                │
 ▼             ▼                ▼
Resume      Skill           Resume
Parser     Extraction       Quality
 │
 ▼
Analysis Results
 │
 ▼
Streamlit Dashboard
```

---

# 🛠 Tech Stack

| Category | Technology |
|-----------|------------|
| Language | Python |
| Frontend | Streamlit |
| Backend | FastAPI |
| AI/NLP | Semantic Analysis |
| PDF Processing | PyMuPDF |
| Data Processing | Pandas, NumPy |
| API | REST API |
| Deployment | Streamlit Community Cloud |
| Backend Hosting | Render |

---

# 📂 Project Structure

```text
AI_Resume_Analyzer/

│

├── app.py                     # Streamlit Frontend

├── main.py                    # FastAPI Backend

├── resume_parser.py

├── semantic_analyzer.py

├── quality_analyzer.py

├── skills.py

├── role_skills.py

├── requirements.txt

└── README.md
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/Goutham-ps/AI_Resume_Analyzer.git

cd AI_Resume_Analyzer
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Run FastAPI Backend

```bash
uvicorn main:app --reload
```

Backend will start at

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

## 4. Run Streamlit Frontend

```bash
streamlit run app.py
```

---

# 📡 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | API Status |
| GET | `/health` | Health Check |
| POST | `/extract-resume` | Extract Resume Text |
| POST | `/analyze` | Job Description Analysis |
| POST | `/analyze-role` | Role-Based Analysis |
| GET | `/docs` | Swagger API Documentation |

---

# 📊 Analysis Includes

✅ ATS Match Score

✅ Matched Skills

✅ Missing Skills

✅ Resume Quality Analysis

✅ Relevant Skills Count

✅ Relevant Projects Count

✅ Role-Based Skill Matching

---

# 💡 Use Cases

- 👨‍🎓 Students
- 💼 Freshers
- 👨‍💻 Software Engineers
- 📊 Data Analysts
- ☁️ Cloud Engineers
- 🤖 Machine Learning Engineers
- 🧑‍💼 Recruiters
- 🎯 Career Coaches

---

# 🚀 Future Improvements

- 🤖 Google Gemini Integration for AI Feedback
- 📄 Resume Ranking System
- 💬 AI Career Suggestions
- 📝 Cover Letter Generator
- 🎤 Interview Question Generator
- 🌍 Multi-language Resume Analysis
- 📥 Downloadable PDF Report
- 📈 Resume History Dashboard

---

# 👨‍💻 Author

**Goutham P S**

GitHub:
https://github.com/Goutham-ps

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

It helps others discover the project and supports future development.
