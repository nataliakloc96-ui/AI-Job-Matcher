# AI Job Matcher

AI-powered job matching platform that compares candidate resumes against job descriptions and returns intelligent fit scores with strengths and missing skills analysis.

## Live Demo

Frontend (Vercel):  
ai-job-matcher-phi.vercel.app

Backend API (Render):  
https://ai-job-matcher-xax3.onrender.com

---

## Features

### Resume Matching
Compare resume content against job descriptions and receive:

- Match score (%)
- Key strengths
- Missing skills
- Fit recommendations

### AI Scoring Engine
Uses semantic-style text similarity scoring to rank candidate-job compatibility.

### Resume Analysis Dashboard
Displays ranked matches with structured scoring output.

### Cloud Deployment
Production deployment:

- Frontend hosted on Vercel
- Backend hosted on Render

---

## Tech Stack

### Backend
- Python
- FastAPI
- JSON processing
- REST API

### Frontend
- HTML
- JavaScript
- Fetch API

### Deployment
- Vercel
- Render

---

## Architecture

Frontend  
↓  
FastAPI Backend  
↓  
Matching Engine  
↓  
Score Analysis Output

---

## API Endpoints

### Match Resume
`POST /match`

Request:

```json
{
  "user_cv": "resume text"
}
```

Response:

```json
{
  "matches": [
    {
      "title": "Python Backend Developer",
      "score": 95,
      "strengths": ["python", "fastapi"],
      "missing_skills": []
    }
  ]
}
```

---

## Installation

Clone repository:

```bash
git clone https://github.com/nataliakloc96-ui/AI-Job-Matcher.git
cd AI-Job-Matcher
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run backend:

```bash
uvicorn main:app --reload
```

Open frontend:

```bash
index.html
```

---

## Example Use Case

1. Paste resume
2. Click **Match**
3. System analyzes fit
4. Receive ranked job matches
5. Review strengths and missing skills

---

## Screenshots

Add screenshots here:

- Landing page
- Resume input form
- Match results
- Score analysis output

---

## Business Value

Helps candidates quickly assess resume-job compatibility and identify missing qualifications before applying.

---

## Future Improvements

- Authentication
- User history tracking
- PDF exports
- Database persistence
- Stripe monetization
- Live job scraping
- Advanced semantic embeddings

---

## Author

Natalia Kurek

AI / Backend Engineering Portfolio Project