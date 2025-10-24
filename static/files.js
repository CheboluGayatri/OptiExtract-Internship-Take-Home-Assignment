async function fetchFiles() {
    try {
        const response = await fetch("/files");

        if (!response.ok) {
            const text = await response.text();
            console.error("Server error:", text);
            return;
        }

        const data = await response.json();

        const listContainer = document.getElementById("fileList");
        listContainer.innerHTML = "";

        data.files.forEach(file => {
            const li = document.createElement("li");
            li.innerHTML = `
                ${file.original_filename} 
                (<a href="/download/${file.system_filename}">Download</a>)
            `;
            listContainer.appendChild(li);
        });
    } catch (err) {
        console.error("Error fetching files:", err);
    }
}

// Call it once on page load
fetchFiles();
