from fastapi import FastAPI
from db import get_conn
from matcher import match_job
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://ai-job-matcher-phi.vercel.app"
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
)


@app.get("/")
def root():
    return {"status": "AI Job Matcher is running!"}


@app.get("/health")
def health():
    return {"ok": True}



@app.post("/match")
def match(user_cv: str):
    try:
        jobs = [
            {
                "title": "Python Backend Developer",
                "company": "OpenAI Labs",
                "location": "Remote",
                "description": "Python FastAPI PostgreSQL Docker APIs"
            }
        ]

        results = []

        for job in jobs:
            ai = match_job(user_cv, job)

            results.append({
                "title": job["title"],
                "company": job["company"],
                "location": job["location"],
                "score": ai["score"],
                "reason": ai["reason"],
                "strengths": ai["strengths"],
                "missing_skills": ai["missing_skills"]
            })

        return {"matches": results}

    except Exception as e:
        return {"error": str(e)}
    
    
@app.get("/job")
def get_job():
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("SELECT id, title, company, location, description FROM job")

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return {
        "jobs": [
            {
                "id": r[0],
                "title": r[1],
                "company": r[2],
                "location": r[3],
                "description": r[4]
            } for r in rows
        ]
    }

