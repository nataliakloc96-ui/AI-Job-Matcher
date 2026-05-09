from fastapi import FastAPI
from db import get_conn
from matcher import match_job

app = FastAPI()

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
                "location": r[3],
                "description": r[4]
            } for r in rows
        ]
    }

@app.post("/match")
def match(user_cv: str):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("SELECT title, company, description FROM job")
    jobs = cursor.fetchall()

    results = []

    for j in job:
        jo = {
            "title": j[0],
            "company": j[1],
            "description": j[2]
        }
        result = match_job(user_cv, jo)
        results.append(result)

    return {"matches": results}