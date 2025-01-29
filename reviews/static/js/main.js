function confirmDelete(url) {
    if (confirm("Are you sure you want to delete this?")) {
        window.location.href = url;
    }
}

document.addEventListener("DOMContentLoaded", function() {
    const toggleButton = document.getElementById("toggle-review-form");
    const formContainer = document.getElementById("review-form-container");

    if (toggleButton && formContainer) {
        toggleButton.addEventListener("click", function() {
            formContainer.style.display = (formContainer.style.display === "none") ? "block" : "none";
        });
    }
});
