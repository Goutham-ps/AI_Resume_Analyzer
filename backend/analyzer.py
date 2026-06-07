def calculate_match(resume_text, job_description):

    resume_words = set(resume_text.lower().split())
    jd_words = set(job_description.lower().split())

    matched = resume_words.intersection(jd_words)

    score = round(
        (len(matched) / len(jd_words)) * 100,
        2
    )

    return score, list(matched)