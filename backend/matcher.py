from openai import OpenAI
import os
import json

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def match_job(cv, job):
    prompt = f"""
You are an expert technical recruiter.

Score this job match from 0 to 100 using:

-Skills match (40%)
- Experience relevance (25%)
- Industry/domain relevance (15%)
- Seniority alignment (10%)


CV:
{cv}

JOB TITLE:
{job["title"]}

COMPANY:
{job["company"]}

DESCRIPTION:
{job["description"]}

Return ONLY valid JSON:
{{
    "score": number,
    "reason": "short explanation",
    "strengths": ["list"],
    "missing_skills": ["list"]
}}
"""
    
    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        temperature = 0.2,
        response_format={"type": "json_object"},
        messages = [{"role": "user", "content": prompt}]
        
    )

    return json.loads(
        response.choices[0].message.content
    )

