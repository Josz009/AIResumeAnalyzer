document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const feedbackDiv = document.getElementById("feedback"); // Add a feedback element in your HTML

    form.addEventListener("submit", async function (event) {
        event.preventDefault(); // Prevent default form submission

        const fileInput = document.querySelector("#resume");
        const jobDescription = document.querySelector("#job_description").value.trim();
        const allowedExtensions = ["pdf", "docx"];
        const backendUrl = "/process"; // Relative path


        // Clear previous feedback
        feedbackDiv.innerHTML = "";
        feedbackDiv.className = "";

        // Validate file
        const file = fileInput.files[0];
        if (!file) {
            displayFeedback("Please upload a resume file.", "error");
            return;
        }

        const fileExtension = file.name.split(".").pop().toLowerCase();
        if (!allowedExtensions.includes(fileExtension)) {
            displayFeedback("Unsupported file format. Please upload a PDF or DOCX file.", "error");
            return;
        }

        // Validate job description
        if (!jobDescription) {
            displayFeedback("Please enter a job description.", "error");
            return;
        }

        // Show loading indicator
        displayFeedback("Processing your resume, please wait...", "info");

        // Prepare form data
        const formData = new FormData();
        formData.append("resume", file);
        formData.append("jobDescription", jobDescription);

        try {
            // Send data to the backend
            const response = await fetch(backendUrl, {
                method: "POST",
                body: formData,
            });

            if (response.ok) {
                const result = await response.json();
                displayFeedback(`Analysis Complete! ATS Score: ${result.atsScore}`, "success");
            } else {
                const errorText = await response.text();
                console.error("Response Error:", errorText);
                displayFeedback("Error: Unable to process the file. Check the backend for details.", "error");
            }
        } catch (error) {
            console.error("Fetch Error:", error);
            displayFeedback("Error: Could not connect to the server.", "error");
        }
    });

    function displayFeedback(message, type) {
        feedbackDiv.textContent = message;
        feedbackDiv.className = `feedback ${type}`;
    }
});

