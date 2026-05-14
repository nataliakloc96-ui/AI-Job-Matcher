from fastapi import FastAPI
from db import get_conn
from matcher import match_job



app = FastAPI()


@app.get("/")
def root():
    return {"status": "AI Job Matcher is running!"}


@app.get("/health")
def health():
    return {"ok": True}



@app.post("/match")
def match(user_cv: str):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
                   SELECT title, company, description 
                   FROM job
        """)
    jobs = cursor.fetchall()

    results = []

    for j in jobs:
        jo = {
            "title": j[0],
            "company": j[1],
            "location": j[2],
            "description": j[3]
        }

        ai = match_job(user_cv, jo)
    
        results.append({
            "title": jo["title"],
            "company": jo["company"],
            "location": jo["location"],
            "score": ai["score"],
            "reason": ai["reason"],
            "strengths": ai["strengths"],
            "missing_skills": ai["missing_skills"]
        })
    
    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return {
        "matches": results[:10]
    }
    
    
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

