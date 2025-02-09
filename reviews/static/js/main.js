document.addEventListener("DOMContentLoaded", function () {
    const toggleButton = document.getElementById("toggle-review-form");
    const reviewForm = document.getElementById("review-form");

    if (toggleButton && reviewForm) {
        // Restore form visibility based on session storage
        const isFormOpen = sessionStorage.getItem("reviewFormOpen");

        if (isFormOpen === "true") {
            reviewForm.classList.remove("d-none"); // Show form if previously opened
        }

        toggleButton.addEventListener("click", function () {
            reviewForm.classList.toggle("d-none"); // Toggle visibility

            // Store the visibility state
            if (reviewForm.classList.contains("d-none")) {
                sessionStorage.setItem("reviewFormOpen", "false");
            } else {
                sessionStorage.setItem("reviewFormOpen", "true");
            }
        });
    }
});
