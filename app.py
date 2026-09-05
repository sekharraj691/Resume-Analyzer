from flask import Flask, request, render_template_string
from dotenv import load_dotenv

import os

from resume_parser import extract_text_from_pdf
from rag_pipeline import build_rag

# LOAD ENV VARIABLES
load_dotenv()

# FLASK APP
app = Flask(__name__)

# UPLOAD FOLDER
UPLOAD_FOLDER = "uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# CREATE uploads FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# BUILD RAG
knowledge, llm = build_rag()

# LOAD HTML
with open("index.html", "r", encoding="utf-8") as file:
    html_template = file.read()

# LOAD CSS
with open("style.css", "r", encoding="utf-8") as file:
    css = file.read()


@app.route("/", methods=["GET", "POST"])
def index():

    result = ""

    if request.method == "POST":

        try:

            # GET FILE
            file = request.files["resume"]

            # CHECK FILE
            if file.filename == "":

                result = "Please upload a PDF resume."

            else:

                # FILE PATH
                filepath = os.path.join(
                    app.config["UPLOAD_FOLDER"],
                    file.filename
                )

                # SAVE FILE
                file.save(filepath)

                # EXTRACT RESUME TEXT
                resume_text = extract_text_from_pdf(filepath)

                # PROMPT
                prompt = f"""
You are an Advanced AI Resume Analyzer and HR Assistant.

Use the HR knowledge below while analyzing.

HR KNOWLEDGE:
{knowledge}

RESUME:
{resume_text}

Analyze and provide:

1. Resume Summary
2. Technical Skills
3. Missing Skills
4. ATS Score out of 100
5. HR Interview Questions
6. Technical Questions
7. Resume Improvements
8. Job Recommendations
9. Final Suggestions

Give professional output.
"""

                # AI RESPONSE
                response = llm.invoke(prompt)

                result = response.content

        except Exception as e:

            result = f"Error: {str(e)}"

    # ADD CSS TO HTML
    final_html = html_template.replace(
        "</head>",
        f"<style>{css}</style></head>"
    )

    return render_template_string(
        final_html,
        result=result
    )


if __name__ == "__main__":

    app.run(debug=True)