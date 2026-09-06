```python
import os

from flask import Flask, request, render_template_string
from dotenv import load_dotenv

from resume_parser import extract_text_from_pdf
from rag_pipeline import build_rag


# ==========================================
# LOAD ENVIRONMENT VARIABLES
# ==========================================
load_dotenv()


# ==========================================
# FLASK APP
# ==========================================
app = Flask(__name__)


# ==========================================
# UPLOAD FOLDER
# ==========================================
UPLOAD_FOLDER = "uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# ==========================================
# LOAD RAG + AI MODEL
# ==========================================
try:
    knowledge, llm = build_rag()
    rag_error = None

except Exception as e:
    knowledge = ""
    llm = None
    rag_error = str(e)


# ==========================================
# LOAD HTML
# ==========================================
with open("index.html", "r", encoding="utf-8") as file:
    html_template = file.read()


# ==========================================
# LOAD CSS
# ==========================================
with open("style.css", "r", encoding="utf-8") as file:
    css = file.read()


# ==========================================
# HOME ROUTE
# ==========================================
@app.route("/", methods=["GET", "POST"])
def index():

    result = ""

    if request.method == "POST":

        try:

            # Check AI configuration
            if llm is None:
                result = f"AI configuration error: {rag_error}"
                return render_page(result)

            # Check uploaded file
            if "resume" not in request.files:
                result = "Please upload a PDF resume."
                return render_page(result)

            file = request.files["resume"]

            # Check filename
            if file.filename == "":
                result = "Please upload a PDF resume."
                return render_page(result)

            # Only allow PDF
            if not file.filename.lower().endswith(".pdf"):
                result = "Only PDF files are supported."
                return render_page(result)

            # Secure filename
            filename = os.path.basename(file.filename)

            filepath = os.path.join(
                app.config["UPLOAD_FOLDER"],
                filename
            )

            # Save uploaded file
            file.save(filepath)

            # Extract resume text
            resume_text = extract_text_from_pdf(filepath)

            if not resume_text.strip():
                result = "Could not extract text from the PDF."
                return render_page(result)

            # ==========================================
            # AI PROMPT
            # ==========================================
            prompt = f"""
You are an Advanced AI Resume Analyzer and HR Assistant.

Use the HR knowledge below while analyzing the resume.

HR KNOWLEDGE:
{knowledge}

RESUME:
{resume_text}

Analyze the resume and provide:

1. Resume Summary
2. Technical Skills
3. Missing Skills
4. ATS Score out of 100
5. HR Interview Questions
6. Technical Interview Questions
7. Resume Improvements
8. Job Recommendations
9. Final Suggestions

Give professional, clear and structured output.
"""

            # ==========================================
            # AI RESPONSE
            # ==========================================
            response = llm.invoke(prompt)

            result = response.content

        except Exception as e:

            result = f"Error: {str(e)}"

    return render_page(result)


# ==========================================
# RENDER PAGE
# ==========================================
def render_page(result=""):

    final_html = html_template.replace(
        "</head>",
        f"<style>{css}</style></head>"
    )

    return render_template_string(
        final_html,
        result=result
    )


# ==========================================
# LOCAL DEVELOPMENT
# ==========================================
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=False
    )
```
