from openai import OpenAI
import os
import json

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def match_job(cv, job):
    prompt = f"""
Compare CV to job offer.

CV: 
{cv}

JOB:
Title: {job['title']}
Company: {job['company']}
Description: {job['description']}

Return ONLY valid JSON:
{{
    "score": number,,
    "reason": "short explanation"
}}
"""
    response = client.chat.completions.create(
        model="gpt-40-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    content = response.choices[0].message.content
    return json.loads(content)

