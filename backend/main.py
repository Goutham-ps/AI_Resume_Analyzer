from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel

from resume_parser import extract_text_from_pdf
from semantic_analyzer import semantic_match
from skills import extract_skills
from quality_analyzer import analyze_resume_quality

from role_skills import ROLE_SKILLS

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "AI Resume Analyzer API Running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


class ResumeRequest(BaseModel):
    resume_text: str
    job_description: str

class RoleRequest(BaseModel):
    resume_text: str
    role: str
@app.post("/analyze")
def analyze_resume(data: ResumeRequest):

    # ATS Semantic Score
    score = semantic_match(
        data.resume_text,
        data.job_description
    )

    # Skills Extraction
    resume_skills = extract_skills(
        data.resume_text
    )

    jd_skills = extract_skills(
        data.job_description
    )

    matched_skills = list(
        set(resume_skills).intersection(
            set(jd_skills)
        )
    )

    missing_skills = list(
        set(jd_skills) - set(resume_skills)
    )

    # Resume Quality Analysis
    quality = analyze_resume_quality(
        data.resume_text,
        data.job_description
    )

    return {
        "match_score": round(score, 2),
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "quality": quality
    }

@app.post("/analyze-role")
def analyze_role(data: RoleRequest):

    resume_text = data.resume_text.lower()

    required_skills = ROLE_SKILLS.get(
        data.role,
        []
    )

    matched_skills = []

    for skill in required_skills:

        if skill.lower() in resume_text:
            matched_skills.append(skill)

    missing_skills = list(
        set(required_skills)
        -
        set(matched_skills)
    )

    score = round(
        (
            len(matched_skills)
            /
            len(required_skills)
        ) * 100,
        2
    )

    return {
    "role": data.role,
    "match_score": score,
    "matched_skills": matched_skills,
    "missing_skills": missing_skills,
    "quality": {
        "relevant_skills": len(matched_skills),
        "relevant_projects": len(matched_skills),
        "suggestions": []
    }
}
@app.post("/extract-resume")
async def extract_resume(
    file: UploadFile = File(...)
):

    text = extract_text_from_pdf(
        file.file
    )

    return {
        "resume_text": text
    }