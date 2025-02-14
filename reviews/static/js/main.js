document.addEventListener("DOMContentLoaded", function () {
    console.log("✅ JavaScript Loaded!"); // Debugging check

    const toggleButton = document.getElementById("toggle-review-form");
    const reviewForm = document.querySelector(".review-form");

    if (!toggleButton || !reviewForm) {
        console.error("🚨 Missing elements: Check button and form class.");
        return; // Exit if elements not found
    }

    console.log("✅ Found button & form."); // Debugging check

    // Restore form visibility based on session storage
    const isFormOpen = sessionStorage.getItem("reviewFormOpen");

    if (isFormOpen === "true") {
        reviewForm.style.display = "block";
    }

    toggleButton.addEventListener("click", function () {
        console.log("📝 Button clicked!"); // Debugging check
        if (reviewForm.style.display === "none" || reviewForm.style.display === "") {
            reviewForm.style.display = "block";
            sessionStorage.setItem("reviewFormOpen", "true");
        } else {
            reviewForm.style.display = "none";
            sessionStorage.setItem("reviewFormOpen", "false");
        }
    });
});
