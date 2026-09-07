import streamlit as st
import PyPDF2
import re

# Page Setup
st.set_page_config(page_title="Intelligent Resume Screening", layout="wide")

st.title("Intelligent Resume Screening & Career Recommendation System")
st.write("Upload a candidate's resume (PDF/TXT) to analyze skills, match job categories, and view detailed recommendations.")

# Resume Text Cleaning Function
def clean_resume(text):
    text = re.sub(r'http\S+\s*', ' ', text)
    text = re.sub(r'RT|cc', ' ', text)
    text = re.sub(r'#\S+', '', text)
    text = re.sub(r'@\S+', '  ', text)
    text = re.sub(r'[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"""), ' ', text)
    text = re.sub(r'[^\x00-\x7f]', r' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

# File Uploader
uploaded_file = st.file_uploader("Upload Resume (PDF or TXT)", type=["pdf", "txt"])

if uploaded_file is not None:
    resume_text = ""
    
    try:
        if uploaded_file.type == "application/pdf":
            reader = PyPDF2.PdfReader(uploaded_file)
            for page in reader.pages:
                extracted = page.extract_text()
                if extracted:
                    resume_text += extracted + " "
        elif uploaded_file.type == "text/plain":
            resume_text = str(uploaded_file.read(), "utf-8")
    except Exception as e:
        st.error(f"Error reading file: {e}")

    if resume_text.strip():
        st.success("✅ Resume Uploaded & Processed Successfully!")
        cleaned_text = clean_resume(resume_text)
        
        # 1. Text Preview Collapsible (Clean UI)
        with st.expander("📄 Click to View Extracted & Processed Text Preview"):
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Original Raw Text")
                st.text_area("Original", resume_text, height=200)
            with col2:
                st.subheader("Cleaned Processed Text")
                st.text_area("Cleaned", cleaned_text, height=200)
            
        st.markdown("---")
        st.subheader("📊 Candidate Screening Analysis & Metrics")
        
        # Skill Database & Target Skillsets
        keywords_map = {
            "Software Engineer / Developer": [
                "java", "python", "c++", "data structures", "algorithms", 
                "sql", "git", "oops", "system design", "rest api"
            ],
            "Data Scientist / ML Engineer": [
                "python", "machine learning", "pandas", "numpy", "scikit-learn", 
                "deep learning", "sql", "tensorflow", "data analysis", "nlp"
            ],
            "Web Developer": [
                "html", "css", "javascript", "react", "node", "django", 
                "flask", "bootstrap", "typescript", "mongodb"
            ],
            "Mechanical / Workshop Engineer": [
                "turning", "facing", "threading", "lathe", "drilling", 
                "grinding", "autocad", "solidworks", "maintenance", "workshop"
            ],
            "Human Resources (HR)": [
                "recruitment", "hiring", "sourcing", "payroll", 
                "employee engagement", "management", "communication"
            ]
        }

        text_lower = cleaned_text.lower()
        matched_scores = {}
        all_detected_skills = set()

        for category, skills in keywords_map.items():
            matches = [skill for skill in skills if skill in text_lower]
            matched_scores[category] = len(matches)
            if matches:
                all_detected_skills.update(matches)

        # Best Category Determination
        best_category = max(matched_scores, key=matched_scores.get)
        max_matches = matched_scores[best_category]
        predicted_role = best_category if max_matches > 0 else "General / Other Domain"

        # Match Score Calculation (0 - 100%)
        match_score = min(100, max_matches * 15)

        # 2. Key Dashboards / Metrics
        m1, m2, m3, m4 = st.columns(4)
        m1.metric(label="Predicted Role", value=predicted_role.split('/')[0])
        m2.metric(label="Fit Score", value=f"{match_score}%")
        m3.metric(label="Skills Detected", value=len(all_detected_skills))
        m4.metric(label="ATS Readability", value="High" if len(cleaned_text) > 100 else "Low")

        st.markdown("---")
        
        # 3. Detected Skills & Skill Gap Analysis
        res_col1, res_col2 = st.columns(2)
        
        with res_col1:
            st.success("🛠️ **Detected Key Skills in Resume**")
            if all_detected_skills:
                for skill in sorted(all_detected_skills):
                    st.write(f"- {skill.title()}")
            else:
                st.write("No major domain-specific technical keywords detected.")

        with res_col2:
            st.warning("⚠️ **Skill Gap Analysis (Recommended Skills to Add)**")
            if max_matches > 0:
                category_skills = set(keywords_map[best_category])
                missing_skills = category_skills - all_detected_skills
                
                if missing_skills:
                    st.write(f"To improve match score for **{best_category}**, consider adding:")
                    for missing in sorted(missing_skills):
                        st.write(f"- {missing.title()}")
                else:
                    st.write("Great match! Candidate possesses all key skills for this domain.")
            else:
                st.write("Upload a more detailed resume to generate gap analysis.")

        st.markdown("---")
        
        # 4. Career & Course Recommendations
        st.subheader("💡 Recommended Next Steps & Courses")
        
        rec1, rec2 = st.columns(2)
        with rec1:
            st.info("📚 **Suggested Certifications / Topics**")
            if "Software" in predicted_role or "Web" in predicted_role:
                st.markdown("* Data Structures & Algorithms Refresher\n* System Design & API Integration\n* Version Control (Git/GitHub)")
            elif "Data Scientist" in predicted_role:
                st.markdown("* Machine Learning Specialization\n* Advanced SQL & Database Querying\n* Model Deployment (Streamlit/Docker)")
            elif "Mechanical" in predicted_role:
                st.markdown("* Advanced Lathe Operations & Threading\n* Computer-Aided Design (AutoCAD/SolidWorks)\n* Workshop Maintenance & Safety Protocols")
            else:
                st.markdown("* Communication & Leadership Skills\n* Project Management Fundamentals")

        with rec2:
            # Download Summary Report Button
            st.success("📥 **Download Screening Summary**")
            summary_text = f"""
--- RESUME SCREENING REPORT ---
Predicted Category: {predicted_role}
Fit Score: {match_score}%
Detected Skills: {', '.join(all_detected_skills)}
            """
            st.download_button(
                label="Download Analysis Report (.txt)",
                data=summary_text,
                file_name="Resume_Screening_Report.txt",
                mime="text/plain"
            )

    else:
        st.error("Uploaded file me se text extract nahi ho paya. Kripya doosri file try karein.")
