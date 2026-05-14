from db import get_conn

def save_jobs():
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO job (id, title, company, location, description)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (title, company) DO NOTHING
    """, (
        job["title"],
        job["company"],
        job["location"],
        job.get("description", "")

    ))
    conn.commit()
    cursor.close()
    conn.close()