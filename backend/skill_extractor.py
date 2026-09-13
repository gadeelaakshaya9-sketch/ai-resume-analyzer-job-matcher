import json
import os


def load_skills():
    current_file = os.path.dirname(os.path.abspath(__file__))

    skills_file = os.path.join(
        current_file,
        "..",
        "data",
        "skills.json"
    )

    with open(skills_file, "r", encoding="utf-8") as file:
        return json.load(file)


def extract_skills(text):
    skills = load_skills()

    text_lower = text.lower()

    found_skills = []

    for skill in skills:
        if skill.lower() in text_lower:
            found_skills.append(skill)

    return found_skills