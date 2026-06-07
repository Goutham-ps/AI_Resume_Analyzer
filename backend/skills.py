SKILLS = [
    "python",
    "sql",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "fastapi",
    "streamlit",
    "docker",
    "aws",
    "cloud",
    "cloud computing",
    "react",
    "flask",
    "django",
    "node.js",
    "mongodb",
    "tableau",
    "git",
    "github",
    "rest api"
]

def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in SKILLS:

        if skill in text:
            found_skills.append(skill)

    return found_skills