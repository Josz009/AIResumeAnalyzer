
import json
from textstat import flesch_reading_ease

def calculate_ats_score(resume_text, job_description):
    with open("models/skills.json", "r") as f:
        skills = json.load(f)
    matching_skills = [skill for skill in skills if skill in resume_text]
    missing_skills = [skill for skill in skills if skill not in resume_text]
    keyword_score = len(matching_skills) / len(skills) * 100
    readability_score = flesch_reading_ease(resume_text)
    return {"keyword_score": keyword_score, "readability_score": readability_score,  "matching_skills": matching_skills,
        "missing_skills": missing_skills}
