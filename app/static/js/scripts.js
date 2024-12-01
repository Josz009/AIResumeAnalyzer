
document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    form.addEventListener("submit", async function (event) {
        event.preventDefault(); // Prevent default form submission

        const fileInput = document.querySelector("#resume");
        const jobDescription = document.querySelector("#jobDescription").value;

        // Validate file format
        if (!fileInput.value.endsWith(".pdf") && !fileInput.value.endsWith(".docx")) {
            alert("Please upload a valid .pdf or .docx file.");
            return;
        }

        // Prepare form data
        const formData = new FormData();
        formData.append("resume", fileInput.files[0]);
        formData.append("jobDescription", jobDescription);

        try {
            // Send data to the backend
            const response = await fetch("https://airesumeanalyzerbackend.onrender.com/process", {
                method: "POST",
                body: formData,
            });

            if (response.ok) {
                const result = await response.json();
                alert(`Analysis Complete! ATS Score: ${result.atsScore}`);
            } else {
                alert("Error: Unable to process the file.");
            }
        } catch (error) {
            console.error("Error:", error);
            alert("Error: Could not connect to the server.");
        }
    });
});
