import streamlit as st
import PyPDF2
import re
import pickle

# Page Configuration
st.set_page_config(page_title="Intelligent Resume Screening", layout="wide")

st.title("Intelligent Resume Screening System")
st.write("Welcome! Upload your resume to get started.")

# Text Cleaning Function
def clean_resume(text):
    text = re.sub('http\S+\s*', ' ', text)
    text = re.sub('RT|cc', ' ', text)
    text = re.sub('#\S+', '', text)
    text = re.sub('@\S+', '  ', text)
    text = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"""), ' ', text)
    text = re.sub(r'[^\x00-\x7f]', r' ', text)
    text = re.sub('\s+', ' ', text)
    return text

# File Uploader
uploaded_file = st.file_uploader("Upload your Resume (PDF or TXT)", type=["pdf", "txt"])

if uploaded_file is not None:
    resume_text = ""
    
    # Extract Text from PDF/TXT
    if uploaded_file.type == "application/pdf":
        reader = PyPDF2.PdfReader(uploaded_file)
        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                resume_text += extracted
    elif uploaded_file.type == "text/plain":
        resume_text = str(uploaded_file.read(), "utf-8")
        
    if resume_text.strip():
        st.success("Resume Uploaded & Processed Successfully!")
        
        # Cleaned Text Preview
        cleaned_text = clean_resume(resume_text)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Extracted Resume Preview")
            st.text_area("Original Text", resume_text, height=250)
            
        with col2:
            st.subheader("Cleaned Resume Text")
            st.text_area("Processed Text", cleaned_text, height=250)
            
        # Model Prediction Section
        st.markdown("---")
        st.subheader("Resume Screening Result")
        
        try:
            # Model & Vectorizer Load
            clf = pickle.load(open('model.pkl', 'rb'))
            tfidf = pickle.load(open('tfidf.pkl', 'rb'))
            
            # Prediction
            input_features = tfidf.transform([cleaned_text])
            prediction_id = clf.predict(input_features)[0]
            
            st.info(f"**Predicted Category / Recommendation:** Category ID {prediction_id}")
            
        except FileNotFoundError:
            st.warning("⚠️ `model.pkl` ya `tfidf.pkl` file missing/empty hai. Tab tak resume parsing functioning fully active hai.")
        except Exception as e:
            st.error(f"Prediction Error: {e}")
    else:
        st.error("Uploaded file me se text read nahi ho paya. Kripya doosri file try karein.")
