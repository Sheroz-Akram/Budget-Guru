
// Toggle Login and Registration Form
const loginText = document.querySelector(".title-text .login");
const loginForm = document.querySelector("form.login");
const loginBtn = document.querySelector("label.login");
const signupBtn = document.querySelector("label.signup");
const signupLink = document.querySelector("form .signup-link a");
signupBtn.onclick = (() => {
    loginForm.style.marginLeft = "-50%";
    loginText.style.marginLeft = "-50%";
});
loginBtn.onclick = (() => {
    loginForm.style.marginLeft = "0%";
    loginText.style.marginLeft = "0%";
});
signupLink.onclick = (() => {
    signupBtn.click();
    return false;
});

// Function that get POST Request data to registor of a User also validate input fields
function registorUser() {

    // Get all the field values
    let registorEmail = document.getElementById("registorEmail").value;
    let registorPassword = document.getElementById("registorPassword").value;
    let registorConfirmPassword = document.getElementById("registorConfirmPassword").value;
    let errorMessage = document.getElementById("errorMessage");

    // Regex to validate email address
    var validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;

    // Validate the Input Fields
    // validate Email Address
    if (!(registorEmail.match(validRegex))) {
        errorMessage.style.display = "block";
        document.querySelector(".errorMessage p").innerText = "Email is Invalid. Check you email address.";
        return false;
    } 

    // Check Password Length
    else if(registorPassword.length < 8){
        errorMessage.style.display = "block";
        document.querySelector(".errorMessage p").innerText = "Weak Password. increase the size of password to atleast 8 characters.";
        return false;
    }

    // Check If Both Confirm and Password Matches
    else if(!(registorConfirmPassword === registorPassword)){
        errorMessage.style.display = "block";
        document.querySelector(".errorMessage p").innerText = "Password and Confirm Password does not match. Type same passwords on both fields.";
        return false;
    }
    // Everything Seems to be Okay. ready to send registration request
    else{
        errorMessage.style.display = "none";
        return true;
    }
}


// Function that validates login request data
function loginUser() {

    // Get all the field values
    let loginEmail = document.getElementById("loginEmail").value;
    let loginPassword = document.getElementById("loginPassword").value;
    let errorMessage = document.getElementById("errorMessage");

    // Regex to validate email address
    var validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;

    // Validate the Input Fields
    // validate Email Address
    if (!(loginEmail.match(validRegex))) {
        errorMessage.style.display = "block";
        document.querySelector(".errorMessage p").innerText = "Email is Invalid. Check you email address.";
        return false;
    } 
    // Check Password Length
    else if(loginPassword.length < 8){
        errorMessage.style.display = "block";
        document.querySelector(".errorMessage p").innerText = "Weak Password. increase the size of password to atleast 8 characters.";
        return false;
    }
    // Everything Seems to be Okay. ready to send registration request
    else{
        errorMessage.style.display = "none";
        return true;
    }
}
