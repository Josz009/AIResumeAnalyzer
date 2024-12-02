document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    form.addEventListener("submit", async function (event) {
        event.preventDefault(); // Prevent default form submission

        const fileInput = document.querySelector("#resume");
        const jobDescription = document.querySelector("#job_description").value;

        // Validate file format
        if (!fileInput.value.endsWith(".pdf") && !fileInput.value.endsWith(".docx")) {
            alert("Please upload a valid .pdf or .docx file.");
            return;
        }

        const backendUrl = "https://airesumeanalyzer.onrender.com/process"; // Corrected endpoint

        // Prepare form data
        const formData = new FormData();
        formData.append("resume", fileInput.files[0]);
        formData.append("jobDescription", jobDescription);

        // Debugging: Log form data
        console.log("Form Data:", {
            resume: fileInput.files[0],
            jobDescription: jobDescription,
        });

        try {
            // Send data to the backend
            const response = await fetch(backendUrl, {
                method: "POST",
                body: formData,
            });

            if (response.ok) {
                const result = await response.json();
                alert(`Analysis Complete! ATS Score: ${result.atsScore}`);
            } else {
                const errorText = await response.text();
                console.error("Response Error:", errorText);
                alert("Error: Unable to process the file. Check the backend for details.");
            }
        } catch (error) {
            console.error("Fetch Error:", error);
            alert("Error: Could not connect to the server.");
        }
    });
});
