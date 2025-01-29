document.addEventListener("DOMContentLoaded", function () {
    const toggleButton = document.getElementById("toggle-review-form");
    const reviewForm = document.querySelector(".card.shadow-sm.border-info");

    if (toggleButton && reviewForm) {
        reviewForm.style.display = "none"; // Hide form initially

        toggleButton.addEventListener("click", function () {
            if (reviewForm.style.display === "none") {
                reviewForm.style.display = "block"; // Show form
            } else {
                reviewForm.style.display = "none"; // Hide form
            }
        });
    } else {
        console.error("Review form or button not found!"); // Debugging
    }
});
