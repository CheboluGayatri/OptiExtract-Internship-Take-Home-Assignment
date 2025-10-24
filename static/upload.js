const uploadForm = document.getElementById("uploadForm");
const fileInput = document.getElementById("fileInput");

uploadForm.addEventListener("submit", async (e) => {
    e.preventDefault();

    const file = fileInput.files[0];
    if (!file) {
        alert("Please select a file");
        return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
        const response = await fetch("/upload-document", {
            method: "POST",
            body: formData,
        });

        if (!response.ok) {
            const text = await response.text();
            console.error("Server error:", text);
            alert("Upload failed");
            return;
        }

        const data = await response.json();
        console.log("Uploaded:", data);
        alert(`File uploaded: ${data.file.original_filename}`);
        fileInput.value = "";
    } catch (err) {
        console.error("Upload error:", err);
        alert("Error uploading file");
    }
});
