document.addEventListener("DOMContentLoaded", function () {
    console.log("✅ JavaScript Loaded!");

    // 🎭 Toggle Review Form
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

    // ✅ Smooth Scroll for anchor links
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

    // ✅ Auto-close Mobile Navbar after clicking a link
    const navbarToggler = document.querySelector(".navbar-toggler");
    const navLinks = document.querySelectorAll(".navbar-nav .nav-link");

    if (navbarToggler) {
        navLinks.forEach(link => {
            link.addEventListener("click", function () {
                if (window.innerWidth <= 992) {
                    navbarToggler.click(); // Closes mobile navbar
                }
            });
        });
    }

    // 🚀 Loading Screen Effect
    const loader = document.getElementById("loading-screen");
    if (loader) {
        setTimeout(() => {
            loader.style.opacity = "0"; // Fade out
            setTimeout(() => loader.style.display = "none", 500); // Hide after fade
        }, 1000); // Simulated load time
    }

    // ⚠️ Confirm Before Deletion
    document.querySelectorAll(".delete-btn").forEach(button => {
        button.addEventListener("click", function (event) {
            const confirmDelete = confirm("🚨 Are you sure you want to delete this? This action cannot be undone.");
            if (!confirmDelete) {
                event.preventDefault(); // Prevent deletion if user cancels
            }
        });
    });

    // 🟢 Hover Effect for Cards
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
});
