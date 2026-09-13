# AI Resume Analyzer & Job Matcher

An AI-powered web application that analyzes a resume and compares it with a job description.

## Features

- Upload PDF resumes
- Extract resume text automatically
- Detect technical skills
- Calculate ATS score
- Calculate AI semantic similarity
- Calculate skill match score
- Identify matched skills
- Identify missing skills
- FastAPI backend
- Interactive web frontend

## Technologies Used

- Python
- FastAPI
- Sentence Transformers
- Scikit-learn
- PyMuPDF
- HTML
- CSS
- JavaScript

## How It Works

1. User uploads a PDF resume.
2. The application extracts the resume text.
3. Technical skills are identified.
4. The job description is analyzed.
5. AI semantic similarity is calculated.
6. ATS and skill scores are calculated.
7. Matched and missing skills are displayed.

## Project Structure

```text
AI Resume Analyzer & Job Matcher
├── backend
│   ├── main.py
│   ├── matcher.py
│   ├── resume_parser.py
│   └── skill_extractor.py
├── data
│   └── skills.json
├── frontend
│   └── index.html
├── uploads
├── requirements.txt
└── README.md