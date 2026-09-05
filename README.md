# Resume Analyzer AI

## Overview
Resume Analyzer AI is an AI-powered web application that analyzes resumes using Generative AI and Retrieval-Augmented Generation (RAG). The application extracts text from uploaded PDF resumes, compares the content with HR knowledge data, and generates professional feedback including ATS score, skill analysis, interview questions, and job recommendations.

The project is built using Python, Flask, Google Gemini AI, LangChain, and FAISS.

---

# Features

- Upload PDF resumes
- Extract resume text automatically
- AI-powered resume analysis
- ATS score generation
- Technical skill identification
- Missing skill suggestions
- HR interview questions
- Technical interview questions
- Resume improvement recommendations
- Job role recommendations
- RAG-based HR knowledge integration
- Simple web interface using Flask

---

# Project Structure

```bash
ResumeAnalyzerAI/
│
├── app.py                  # Main Flask application
├── rag_pipeline.py         # RAG pipeline creation
├── resume_parser.py        # PDF text extraction
├── hr_knowledge.txt        # HR knowledge base
├── index.html              # Frontend HTML
├── style.css               # CSS styling
├── requirements.txt        # Required Python packages
├── .env                    # API keys and environment variables
├── uploads/                # Uploaded resume files
└── __pycache__/            # Python cache files
```

---

# Technologies Used

## Backend
- Python
- Flask

## AI & Machine Learning
- Google Gemini API
- LangChain
- LangChain Google Generative AI
- FAISS Vector Database
- Retrieval-Augmented Generation (RAG)

## Frontend
- HTML
- CSS

## PDF Processing
- PyPDF

---

# Installation

## Step 1: Clone the Repository

```bash
git clone <repository_url>
cd ResumeAnalyzerAI
```

---

## Step 2: Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the project root directory.

Example:

```env
GOOGLE_API_KEY=your_google_gemini_api_key
```

---

# Running the Application

```bash
python app.py
```

The application will start on:

```bash
http://127.0.0.1:5000
```

---

# How the System Works

## 1. Resume Upload
The user uploads a PDF resume through the web interface.

## 2. Resume Parsing
The application extracts text from the uploaded PDF using PyPDF.

## 3. RAG Pipeline
The HR knowledge base is loaded and converted into embeddings using LangChain and FAISS.

## 4. AI Analysis
Google Gemini analyzes the resume with the HR knowledge context.

## 5. Result Generation
The system generates:

- Resume Summary
- Skills Analysis
- Missing Skills
- ATS Score
- Interview Questions
- Improvement Suggestions
- Job Recommendations

---

# Example Output

```text
1. Resume Summary
2. Technical Skills
3. Missing Skills
4. ATS Score: 82/100
5. HR Interview Questions
6. Technical Questions
7. Resume Improvements
8. Job Recommendations
9. Final Suggestions
```

---

# Dependencies

The project uses the following libraries:

```text
flask
python-dotenv
google-generativeai
langchain
langchain-community
langchain-google-genai
faiss-cpu
pypdf
```

---

# Future Improvements

- Multiple resume uploads
- Resume ranking system
- Job matching engine
- Resume keyword optimization
- Resume template generation
- Database integration
- User authentication
- Export analysis as PDF
- Dashboard analytics
- AI career guidance chatbot

---

# Advantages

- Automated resume analysis
- Faster HR screening
- AI-generated recommendations
- ATS optimization guidance
- Easy-to-use interface
- Smart HR knowledge integration

---

# Limitations

- Requires internet connection for Gemini API
- Limited to PDF resumes
- AI responses may vary
- No database storage currently
- Basic frontend UI

---

# Author

Developed as an AI-based Resume Analyzer project using Flask, LangChain, Gemini AI, and RAG.

---

# License

This project is for educational and learning purposes.

