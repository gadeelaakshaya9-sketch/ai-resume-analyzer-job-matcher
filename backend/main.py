from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import os
import shutil

from resume_parser import extract_text_from_pdf
from skill_extractor import extract_skills
from matcher import calculate_semantic_match

def calculate_ats_score(resume_text, job_description):
    """
    Calculate a basic ATS keyword score.
    """

    resume_words = set(resume_text.lower().split())
    job_words = set(job_description.lower().split())

    if not job_words:
        return 0

    matched_words = resume_words.intersection(job_words)

    score = (len(matched_words) / len(job_words)) * 100

    return round(score, 2)
app = FastAPI(
    title="AI Resume Analyzer & Job Matcher",
    description="Analyze resumes and match them with job descriptions using AI.",
    version="2.0"
)


# Allow frontend to connect with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Upload folder
UPLOAD_FOLDER = "../uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# Home API
@app.get("/")
def home():
    return {
        "message": "AI Resume Analyzer API is running!"
    }


# Resume analysis API
@app.post("/analyze")
async def analyze_resume(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):

    # Create file path
    file_path = os.path.join(
        UPLOAD_FOLDER,
        resume.filename
    )

    # Save uploaded resume
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(
            resume.file,
            buffer
        )

    # Extract text from resume
    resume_text = extract_text_from_pdf(
        file_path
    )

    # Extract skills from resume
    resume_skills = extract_skills(
        resume_text
    )

    # Extract required skills from job description
    job_skills = extract_skills(
        job_description
    )

    # Calculate AI semantic similarity
    semantic_score = calculate_semantic_match(
        resume_text,
        job_description
    )
    ats_score = calculate_ats_score(
    resume_text,
    job_description
    )
    # Calculate exact skill matching
    resume_skills_lower = {
        skill.lower()
        for skill in resume_skills
    }

    job_skills_lower = {
        skill.lower()
        for skill in job_skills
    }

    matched_skills = sorted(
        resume_skills_lower.intersection(
            job_skills_lower
        )
    )

    missing_skills = sorted(
        job_skills_lower - resume_skills_lower
    )

    # Calculate skill match percentage
    if len(job_skills_lower) == 0:
        skill_score = 0
    else:
        skill_score = (
            len(matched_skills)
            / len(job_skills_lower)
        ) * 100

    skill_score = round(
        skill_score,
        2
    )

    # Final AI score
    final_score = round(
        (semantic_score * 0.6)
        +
        (skill_score * 0.4),
        2
    )

    # Return result
    return {
        "resume_filename": resume.filename,

        "resume_skills": resume_skills,

        "job_required_skills": job_skills,

        "semantic_score": semantic_score,

        "ats_score": ats_score,

        "skill_score": skill_score,

        "match_score": final_score,

        "matched_skills": matched_skills,

        "missing_skills": missing_skills
    }