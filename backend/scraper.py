from bs4 import BeautifulSoup
import requests
from db import get_conn
from notifications import send_telegram

def scrape_jobs():
    url = "https://remoteok.com/remote-dev-jobs"

    headers = {"User-Agent": "Mozilla/5.0 "}

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")

    jobs = []

    for row in soup.select("tr.job"):
        title = row.get("data-position")
        company = row.get("data-company")
        location = row.get("data-location")

        if title:
            jobs.append((title, company, location))

    return jobs

def save_jobs(jobs):
    conn = get_conn()
    cursor = conn.cursor()

    for job in jobs:
        cursor.execute("""
            INSERT INTO job (title, company, location)
            VALUES (%s, %s, %s)
            ON CONFLICT (title, company) DO NOTHING
        """, job)

        if cursor.rowcount > 0:
            send_telegram(f"NEW JOB:\n{job[0]}\n{job[1]}\n({job[2]})")
    
    conn.commit()
    cursor.close()
    conn.close()
    