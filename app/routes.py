from flask import render_template, request, jsonify
from app.services.resume_parser import parse_resume
from app.services.ats_scoring import calculate_ats_score
from app import app, mongo

# Main "/" route
@app.route("/", methods=["GET", "POST"])
def index():
    try:
        if request.method == "POST":
            # Access form data
            resume_file = request.files.get("resume")
            job_description = request.form.get("job_description")

            # Validate input
            if not resume_file or not job_description:
                print(f"Validation failed: resume_file={resume_file}, job_description={job_description}")
                return render_template("index.html", error="Please provide both a resume file and a job description."), 400

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
    except Exception as e:
        print(f"Error during processing in index route: {e}")
        return render_template("error.html", message="An unexpected error occurred. Please try again later."), 500


# "/process" API endpoint
@app.route("/process", methods=["POST"])
def process_file():
    try:
        # Log incoming request for debugging
        print("Request form data:", request.form)
        print("Request files:", request.files)

        # Validate input
        if "resume" not in request.files or not request.files["resume"].filename:
            print("Validation failed: Missing or invalid resume file.")
            return jsonify({"error": "Missing or invalid resume file."}), 400

        if "job_description" not in request.form or not request.form["job_description"].strip():
            print("Validation failed: Missing or invalid job description.")
            return jsonify({"error": "Missing or invalid job description."}), 400

        # Access uploaded file and job description
        resume_file = request.files["resume"]
        job_description = request.form["job_description"]

        # Log received data
        print(f"Received resume file: {resume_file.filename}")
        print(f"Received job description: {job_description}")

        # Process the file and calculate ATS score
        resume_text = parse_resume(resume_file)
        ats_score = calculate_ats_score(resume_text, job_description)

        # Log processing results
        print(f"Processed resume text: {resume_text[:100]}")  # Log only first 100 chars
        print(f"Calculated ATS score: {ats_score}")

        # Save results to MongoDB
        mongo.db.results.insert_one({
            "resume_text": resume_text,
            "job_description": job_description,
            "ats_score": ats_score
        })

        # Return JSON response
        return jsonify({"atsScore": ats_score})
    except Exception as e:
        print(f"Error during processing in /process route: {e}")
        return jsonify({"error": "Internal server error"}), 500

