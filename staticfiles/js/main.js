/* jshint esversion: 11 */

document.addEventListener("DOMContentLoaded", function () {
    console.log("✅ JavaScript Loaded!");

    // 🎭 TOGGLE REVIEW FORM
    const toggleButton = document.getElementById("toggle-review-form");
    const reviewForm = document.querySelector(".review-form");

    if (toggleButton && reviewForm) {
        console.log("✅ Found button & form.");
        const isFormOpen = sessionStorage.getItem("reviewFormOpen");

        if (isFormOpen === "true") {
            reviewForm.style.display = "block";
        }

        toggleButton.addEventListener("click", function () {
            console.log("📝 Button clicked!");
            reviewForm.style.display = reviewForm.style.display === "none" || reviewForm.style.display === "" ? "block" : "none";
            sessionStorage.setItem("reviewFormOpen", reviewForm.style.display === "block" ? "true" : "false");
        });
    }

    // ✅ SMOOTH SCROLL TO REVIEWS
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener("click", function (event) {
            event.preventDefault();
            const targetId = this.getAttribute("href").substring(1);
            const targetElement = document.getElementById(targetId);

            if (targetElement) {
                targetElement.scrollIntoView({ behavior: "smooth" });
            }
        });
    });

    // ✅ AUTO-CLOSE MOBILE NAVBAR
    const navbarToggler = document.querySelector(".navbar-toggler");
    const navLinks = document.querySelectorAll(".navbar-nav .nav-link");

    if (navbarToggler) {
        navLinks.forEach(link => {
            link.addEventListener("click", function () {
                if (window.innerWidth <= 992) {
                    navbarToggler.click();
                }
            });
        });
    }

    // ⚠️ CONFIRM BEFORE DELETION
    document.querySelectorAll(".delete-btn").forEach(button => {
        button.addEventListener("click", function (event) {
            const confirmDelete = confirm("🚨 Are you sure you want to delete this?");
            if (!confirmDelete) {
                event.preventDefault();
            }
        });
    });

    // ✅ HOVER EFFECT FOR CARDS
    document.querySelectorAll(".card").forEach(card => {
        card.addEventListener("mouseover", () => {
            card.style.transform = "scale(1.05)";
            card.style.boxShadow = "0 0 20px rgba(0, 255, 0, 0.8)";
        });

        card.addEventListener("mouseleave", () => {
            card.style.transform = "scale(1)";
            card.style.boxShadow = "0 0 15px rgba(0, 255, 0, 0.5)";
        });
    });

    // ✅ HERO BUTTON CLICK FIX
    document.querySelectorAll(".hero-btn").forEach(button => {
        button.addEventListener("click", function (event) {
            console.log("✅ Hero Button Clicked:", event.target);
            event.stopPropagation();  // Ensures JavaScript does not block navigation
        });
    });
}); // <--- Ensure this closing bracket is here
