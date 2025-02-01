document.addEventListener("DOMContentLoaded", function () {
    const toggleButton = document.getElementById("toggle-review-form");
    const reviewForm = document.querySelector(".card.shadow-sm.border-info");

    if (toggleButton && reviewForm) {
        // Check if the form was opened before submitting
        const isFormOpen = sessionStorage.getItem("reviewFormOpen");
        if (isFormOpen === "true") {
            reviewForm.style.display = "block"; // Keep form visible
        } else {
            reviewForm.style.display = "none"; // Default: Hide form
        }

        toggleButton.addEventListener("click", function () {
            if (reviewForm.style.display === "none") {
                reviewForm.style.display = "block"; // Show form
                sessionStorage.setItem("reviewFormOpen", "true"); // Store state
            } else {
                reviewForm.style.display = "none"; // Hide form
                sessionStorage.setItem("reviewFormOpen", "false"); // Store state
            }
        });
    }
});
