
from flask import render_template, request, redirect, url_for
from app.services.resume_parser import parse_resume
from app.services.ats_scoring import calculate_ats_score
from app import app

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        resume_file = request.files["resume"]
        job_description = request.form["job_description"]
        resume_text = parse_resume(resume_file)
        ats_score = calculate_ats_score(resume_text, job_description)
        return render_template("results.html", ats_score=ats_score)
    return render_template("index.html")
