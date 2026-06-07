import streamlit as st
import requests

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

if "resume_text" not in st.session_state:
    st.session_state.resume_text = ""

st.title("📄 AI Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

# ==========================
# Resume Upload
# ==========================
if uploaded_file:

    if st.button("Extract Resume"):

        files = {
            "file": (
                uploaded_file.name,
                uploaded_file,
                "application/pdf"
            )
        }

        response = requests.post(
            "https://ai-resume-analyzer-api-gmbq.onrender.com/extract-resume",
            files=files
        )

        data = response.json()

        st.session_state.resume_text = data["resume_text"]

        st.success(
            "✅ Resume Uploaded & Processed Successfully"
        )

# ==========================
# Resume Analysis
# ==========================
if st.session_state.resume_text:

    st.info("📄 Resume Ready For Analysis")

    analysis_type = st.radio(
        "Select Analysis Type",
        [
            "Job Description Analysis",
            "Role Based Analysis"
        ]
    )

    if analysis_type == "Job Description Analysis":

        job_description = st.text_area(
            "Paste Job Description",
            height=200,
            placeholder="Paste the job description here..."
        )

    else:

        role = st.selectbox(
            "Select Target Role",
            [
                "Cloud Engineer",
                "Machine Learning Engineer",
                "Full Stack Developer",
                "Data Analyst"
            ]
        )

    if st.button("Analyze Resume"):

        if analysis_type == "Job Description Analysis":

            payload = {
                "resume_text": st.session_state.resume_text,
                "job_description": job_description
            }

            response = requests.post(
                "http://ai-resume-analyzer-api-gmbq.onrender.com/analyze",
                json=payload
            )
            st.write("Status Code:", response.status_code)
            st.write("Response Text:", response.text)

        else:

            payload = {
                "resume_text": st.session_state.resume_text,
                "role": role
            }

            response = requests.post(
                "http://ai-resume-analyzer-api-gmbq.onrender.com/analyze-role",
                json=payload
            )
            st.write("Status Code:", response.status_code)
            st.write("Response Text:", response.text)


        result = response.json()

        score = round(
            result["match_score"],
            2
        )

        # ==========================
        # ATS Score Section
        # ==========================
        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "📊 ATS Match Score",
                f"{score}%"
            )

        with col2:

            if score >= 80:
                st.success(
                    "🏆 Excellent Match"
                )

            elif score >= 60:
                st.warning(
                    "👍 Good Match"
                )

            else:
                st.error(
                    "⚠️ Needs Improvement"
                )

        st.progress(score / 100)

        st.divider()

        # ==========================
        # Skills Section
        # ==========================
        col1, col2 = st.columns(2)

        with col1:

            st.subheader(
                "🟢 Matched Skills"
            )

            if result["matched_skills"]:

                for skill in result["matched_skills"]:

                    st.success(
                        f"✓ {skill.title()}"
                    )

            else:

                st.info(
                    "No matching skills found"
                )

        with col2:

            st.subheader(
                "🔴 Missing Skills"
            )

            if result["missing_skills"]:

                for skill in result["missing_skills"]:

                    st.error(
                        f"✗ {skill.title()}"
                    )

            else:

                st.success(
                    "No missing skills found"
                )

        st.divider()
# ==========================
# Resume Quality
# ==========================
        if (
            analysis_type == "Job Description Analysis"
            and "quality" in result
        ):

            st.subheader(
                "📄 Resume Quality Analysis"
            )

            quality = result["quality"]

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Relevant Skills",
                    quality["relevant_skills"]
                )

            with col2:
                st.metric(
                    "Relevant Projects",
                    quality["relevant_projects"]
                )

            strength_score = (
                quality["relevant_skills"] * 15
                +
                quality["relevant_projects"] * 5
            )

            if strength_score >= 40:
                st.success("🏆 Strong Resume")

            elif strength_score >= 20:
                st.warning("👍 Average Resume")

            else:
                st.error("⚠️ Weak Resume")
