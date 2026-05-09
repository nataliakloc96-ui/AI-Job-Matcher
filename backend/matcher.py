import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def match_job(cv, job):
    prompt = f"""
You are a job matching AI.

CV: 
{cv}

JOB:
Title: {job['title']}
Company: {job['company']}
Description: {job.get('description', '')}

Return JSON:
{{
    "score": 0-100,
    "reason": "short explanation"
}}
"""
    response = openai.Completion.create(
        model="gpt-40-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["choices"][0]["message"]["content"]