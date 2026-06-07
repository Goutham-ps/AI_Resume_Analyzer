def analyze_resume_quality(
    resume_text,
    job_description
):

    resume = resume_text.lower()
    jd = job_description.lower()

    skills = [
        "python",
        "sql",
        "machine learning",
        "deep learning",
        "artificial intelligence",
        "fastapi",
        "streamlit",
        "docker",
        "aws",
        "git",
        "github"
    ]

    jd_skills = []

    for skill in skills:
        if skill in jd:
            jd_skills.append(skill)

    relevant_skills = []

    for skill in jd_skills:
        if skill in resume:
            relevant_skills.append(skill)

    project_keywords = [
        "project",
        "developed",
        "built",
        "implemented",
        "created"
    ]

    project_count = len(relevant_skills)

    suggestions = []

    missing_skills = list(
        set(jd_skills) - set(relevant_skills)
    )

    for skill in missing_skills:
        suggestions.append(
            f"Add projects demonstrating {skill.title()}"
        )

    return {
        "relevant_projects": project_count,
        "relevant_skills": len(relevant_skills),
        "suggestions": suggestions
    }