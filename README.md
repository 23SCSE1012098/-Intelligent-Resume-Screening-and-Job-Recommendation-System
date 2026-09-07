
# 🤖 Intelligent Resume Screening and Job Recommendation System

An intelligent machine learning and NLP-based system that analyzes resumes, extracts relevant skills, compares them with job descriptions, calculates job-match scores, and recommends suitable job roles.

## 📌 Project Overview

The **Intelligent Resume Screening and Job Recommendation System** is designed to automate the initial resume screening process.

The system uses **Natural Language Processing (NLP)** and **Machine Learning** techniques to understand resume content and job requirements.

It helps users and recruiters by:

- Extracting important information from resumes
- Identifying technical and professional skills
- Comparing resumes with job descriptions
- Calculating resume-job similarity scores
- Identifying missing or required skills
- Recommending suitable job roles
- Ranking jobs according to resume relevance

---

## 🎯 Objectives

The main objectives of this project are:

1. Automate the resume screening process.
2. Reduce the time required for manual resume evaluation.
3. Match candidates with relevant job descriptions.
4. Identify skills present and missing in a resume.
5. Recommend suitable job roles based on candidate profiles.
6. Provide an understandable job-match score.

---

## 🚀 Key Features

### 📄 Resume Analysis

The system analyzes uploaded or provided resume content and extracts relevant information such as:

- Technical skills
- Programming languages
- Frameworks
- Databases
- Tools
- Education
- Experience
- Projects

### 🔍 Job Description Analysis

The system processes job descriptions and identifies:

- Required skills
- Technologies
- Qualifications
- Job-related keywords
- Role requirements

### 📊 Resume-Job Matching

The system compares the resume with a job description and calculates a similarity score.

Example:

```text
Resume-Job Similarity Score: 0.78

Match Percentage: 78%

Status: Good Match
````

### 🧠 Skill Gap Analysis

The system identifies skills that are required by the job but are missing from the resume.

Example:

```text
Matched Skills:
✓ Java
✓ SQL
✓ Git
✓ Data Structures

Missing Skills:
✗ Spring Boot
✗ REST API
```

### 💼 Job Recommendation

Based on the candidate's skills and resume content, the system recommends relevant job roles.

Example:

```text
Recommended Roles:

1. Software Developer
2. Backend Developer
3. Java Developer
4. Full Stack Developer
5. Web Developer
```

---

## 🏗️ System Architecture

```text
                Resume
                   │
                   ▼
          Resume Text Extraction
                   │
                   ▼
             Text Cleaning
                   │
                   ▼
          NLP / Feature Extraction
                   │
                   ▼
            Skill Extraction
                   │
                   │
                   ▼
          ┌──────────────────┐
          │                  │
          │ Job Description  │
          │                  │
          └────────┬─────────┘
                   │
                   ▼
           Text Processing
                   │
                   ▼
          Similarity Calculation
                   │
                   ▼
          Resume-Job Match Score
                   │
          ┌────────┴─────────┐
          ▼                  ▼
    Skill Gap Analysis   Job Recommendation
          │                  │
          └────────┬─────────┘
                   ▼
             Final Results
```

---

## 🛠️ Technologies Used

| Technology        | Purpose                                     |
| ----------------- | ------------------------------------------- |
| Python            | Core development                            |
| Machine Learning  | Job recommendation and classification       |
| NLP               | Resume and job-description processing       |
| Pandas            | Data processing                             |
| NumPy             | Numerical operations                        |
| Scikit-learn      | Machine learning and similarity calculation |
| TF-IDF            | Text feature extraction                     |
| Cosine Similarity | Resume-job similarity                       |
| Streamlit         | User interface                              |
| Git               | Version control                             |
| GitHub            | Project hosting                             |

---

## 🧠 Machine Learning / NLP Approach

### 1. Text Preprocessing

Resume and job-description text is cleaned before processing.

Typical preprocessing includes:

* Lowercase conversion
* Removing unnecessary characters
* Tokenization
* Stop-word removal
* Text normalization

### 2. TF-IDF Vectorization

The system converts resume and job-description text into numerical vectors using **TF-IDF (Term Frequency-Inverse Document Frequency)**.

```text
Resume Text
     ↓
TF-IDF Vectorization
     ↓
Numerical Representation
```

### 3. Cosine Similarity

Cosine similarity is used to measure how closely the resume matches the job description.

```text
Resume Vector
       +
Job Description Vector
       ↓
Cosine Similarity
       ↓
Similarity Score
```

A higher similarity score indicates stronger textual alignment between the resume and job description.

---

## 📈 Example Output

```text
----------------------------------------
        RESUME SCREENING RESULT
----------------------------------------

Job Role:
Software Developer

Similarity Score:
0.78

Match Percentage:
78%

----------------------------------------
Matched Skills
----------------------------------------

✓ Java
✓ Data Structures
✓ SQL
✓ Git
✓ JavaScript
✓ React

----------------------------------------
Missing Skills
----------------------------------------

✗ Spring Boot
✗ REST API
✗ Microservices

----------------------------------------
Recommended Roles
----------------------------------------

1. Software Developer
2. Java Developer
3. Backend Developer
```

---

## 📂 Project Structure

```text
Intelligent-Resume-Screening-and-Job-Recommendation-System/
│
├── dataset/
│   └── jobs.csv
│
├── model/
│   └── model.pkl
│
├── notebooks/
│   └── analysis.ipynb
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/Intelligent-Resume-Screening-and-Job-Recommendation-System.git
```

### Navigate to the Project

```bash
cd Intelligent-Resume-Screening-and-Job-Recommendation-System
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

If the project uses Streamlit:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📋 Requirements

Example `requirements.txt`:

```text
pandas
numpy
scikit-learn
nltk
joblib
streamlit
PyPDF2
```

Add or remove libraries according to the actual implementation.

---

## 🌐 Deployment

The application can be deployed using platforms such as:

* Streamlit Community Cloud
* Render
* Railway

For Streamlit deployment:

```text
GitHub Repository
        ↓
Streamlit Community Cloud
        ↓
Live Application
```

---

## 🔮 Future Improvements

The project can be enhanced with:

* Deep learning based resume classification
* BERT/Transformer-based semantic matching
* Advanced skill extraction using Named Entity Recognition
* Resume ranking system
* Personalized career recommendations
* LinkedIn/job portal integration
* Resume improvement suggestions
* Automated ATS score generation
* Explainable AI for recommendations

---

## ⚠️ Disclaimer

This project is intended for educational and demonstration purposes.

The generated similarity scores and job recommendations should not be considered as guaranteed hiring decisions. Final recruitment decisions should involve human evaluation and additional candidate assessment.

---

## 👨‍💻 Author

**Ram Kumar**

B.Tech Computer Science and Engineering
Galgotias University

### Skills

`Java` `Python` `Machine Learning` `NLP` `SQL` `React` `DSA` `Git` `GitHub`

---

## ⭐ Project Highlights

* Resume text analysis
* NLP-based skill extraction
* Job description matching
* TF-IDF based text representation
* Cosine similarity
* Skill gap analysis
* Job role recommendation
* Machine Learning integration
* Streamlit-based interface

```

**Important:** README mein wahi technologies/models rakho jo tumne actually project mein use kiye hain. Agar tum mujhe apne project ka **actual folder structure ya code** de do, main is README ko exactly tumhare implementation ke according bana dunga—fake features/technologies ke bina.
```
