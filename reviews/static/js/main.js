document.addEventListener("DOMContentLoaded", function () {
    const toggleButton = document.getElementById("toggle-review-form");
    const reviewForm = document.getElementById("review-form");

    if (toggleButton && reviewForm) {
        // Restore form visibility based on session storage
        const isFormOpen = sessionStorage.getItem("reviewFormOpen");

        if (isFormOpen === "true") {
            reviewForm.style.display = "block"; // Show form if previously opened
        } else {
            reviewForm.style.display = "none"; // Hide form by default
        }

        // Event listener for button click
        toggleButton.addEventListener("click", function () {
            if (reviewForm.style.display === "none" || reviewForm.style.display === "") {
                reviewForm.style.display = "block"; // Show form
                sessionStorage.setItem("reviewFormOpen", "true");
            } else {
                reviewForm.style.display = "none"; // Hide form
                sessionStorage.setItem("reviewFormOpen", "false");
            }
        });
    }
});
