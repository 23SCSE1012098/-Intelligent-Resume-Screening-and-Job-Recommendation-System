import streamlit as st
import PyPDF2
import re

# Page Setup
st.set_page_config(page_title="Intelligent Resume Screening", layout="wide")

st.title("Intelligent Resume Screening System")
st.write("Upload a candidate's resume (PDF/TXT) to screen skills, predict job category, and see matches.")

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
    
    # Extract text based on file type
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
        
        # Display Text Preview
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("📄 Extracted Resume Text")
            st.text_area("Original Text", resume_text, height=220)
        with col2:
            st.subheader("🧹 Processed Text")
            st.text_area("Cleaned Text", cleaned_text, height=220)
            
        st.markdown("---")
        st.subheader("📊 Resume Screening & Recommendation Results")
        
        # Skill Database & Categories
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

        # Determine Best Matched Category
        best_category = max(matched_scores, key=matched_scores.get)
        max_matches = matched_scores[best_category]

        if max_matches == 0:
            predicted_role = "General / Other Domain"
        else:
            predicted_role = best_category

        # Results UI Layout
        res_col1, res_col2 = res_cols = st.columns(2)
        
        with res_col1:
            st.info(f"🎯 **Predicted Category:** {predicted_role}")
            if max_matches > 0:
                st.write(f"**Matched Keywords Count:** {max_matches}")
            else:
                st.write("No specific domain-matched keywords found.")

        with res_col2:
            st.success("🛠️ **Detected Key Skills:**")
            if all_detected_skills:
                st.write(", ".join(sorted(all_detected_skills)))
            else:
                st.write("No specific technical keywords detected.")

    else:
        st.error("Uploaded file me se text extract nahi ho paya. Kripya doosri file try karein.")
