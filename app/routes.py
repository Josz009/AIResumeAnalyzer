from flask import render_template, request, redirect, url_for, jsonify
from app.services.resume_parser import parse_resume
from app.services.ats_scoring import calculate_ats_score
from app import app, mongo

# Existing "/" route
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        resume_file = request.files["resume"]
        job_description = request.form["job_description"]
        
        # Process resume and calculate ATS score
        resume_text = parse_resume(resume_file)
        ats_score = calculate_ats_score(resume_text, job_description)
        
        # Save results to MongoDB
        mongo.db.results.insert_one({
            "resume_text": resume_text,
            "job_description": job_description,
            "ats_score": ats_score
        })

        return render_template("result.html", ats_score=ats_score)
    return render_template("index.html")

# New "/process" API endpoint
@app.route("/process", methods=["POST"])
def process_file():
    if "resume" not in request.files or "job_description" not in request.form:
        return jsonify({"error": "Invalid input"}), 400

    # Access uploaded file and job description
    resume_file = request.files["resume"]
    job_description = request.form["job_description"]

    # Process the file and calculate ATS score
    resume_text = parse_resume(resume_file)
    ats_score = calculate_ats_score(resume_text, job_description)

    # Save results to MongoDB
    mongo.db.results.insert_one({
        "resume_text": resume_text,
        "job_description": job_description,
        "ats_score": ats_score
    })

    # Return JSON response
    return jsonify({"atsScore": ats_score})
