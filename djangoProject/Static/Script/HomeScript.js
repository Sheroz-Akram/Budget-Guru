// Toggle Menu For Navigation Bar Mobile Menu
let navBarMobile = 0;
function toggleMenu() {

    // get Nav Bar Menu For Mobile
    let mobileMenu = document.getElementById("navBarMobileMenu");

    // Toggle On
    if (navBarMobile == 1) {
        mobileMenu.style.display = "none";
        navBarMobile = 0;
    }
    // Toggle Off
    else {
        mobileMenu.style.display = "block";
        navBarMobile = 1;
    }

}