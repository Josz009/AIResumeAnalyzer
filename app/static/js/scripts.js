
document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    form.addEventListener("submit", function (event) {
        const fileInput = document.querySelector("#resume");
        if (!fileInput.value.endsWith(".pdf") && !fileInput.value.endsWith(".docx")) {
            event.preventDefault();
            alert("Please upload a valid .pdf or .docx file.");
        }
    });
});
