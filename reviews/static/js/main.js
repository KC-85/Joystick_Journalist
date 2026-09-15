/* jshint esversion: 11 */

document.addEventListener("DOMContentLoaded", function () {
    const mobileMenuButton = document.getElementById("mobile-menu-button");
    const mobileMenu = document.getElementById("mobile-menu");

    if (mobileMenuButton && mobileMenu) {
        mobileMenuButton.addEventListener("click", function () {
            const isHidden = mobileMenu.classList.toggle("hidden");
            mobileMenuButton.setAttribute("aria-expanded", String(!isHidden));
        });
    }

    document.querySelectorAll("[data-confirm]").forEach(element => {
        element.addEventListener("click", function (event) {
            const message = element.getAttribute("data-confirm");
            if (message && !window.confirm(message)) {
                event.preventDefault();
            }
        });
    });

    document.querySelectorAll("[data-flash-close]").forEach(button => {
        button.addEventListener("click", function () {
            const message = button.closest(".flash-message");
            if (message) {
                message.classList.add("opacity-0", "translate-y-1");
                window.setTimeout(() => {
                    message.remove();
                }, 250);
            }
        });
    });
});
