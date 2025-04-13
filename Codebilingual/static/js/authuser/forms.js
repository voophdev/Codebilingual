function showTooltip() {
  document.getElementById("password-tooltip").style.display = "block";
}

function hideTooltip() {
  document.getElementById("password-tooltip").style.display = "none";
}

function checkPassword() {
  var password = document.getElementById("password").value;
  var length = document.getElementById("length");
  var uppercase = document.getElementById("uppercase");
  var number = document.getElementById("number");
  var special = document.getElementById("special");

  // Check password length
  if (password.length >= 8) {
    length.classList.remove("invalid");
    length.classList.add("valid");
  } else {
    length.classList.remove("valid");
    length.classList.add("invalid");
  }

  // Check for uppercase letter
  if (/[A-Z]/.test(password)) {
    uppercase.classList.remove("invalid");
    uppercase.classList.add("valid");
  } else {
    uppercase.classList.remove("valid");
    uppercase.classList.add("invalid");
  }

  // Check for number
  if (/[0-9]/.test(password)) {
    number.classList.remove("invalid");
    number.classList.add("valid");
  } else {
    number.classList.remove("valid");
    number.classList.add("invalid");
  }

  // Check for special character
  if (/[^A-Za-z0-9]/.test(password)) {
    special.classList.remove("invalid");
    special.classList.add("valid");
  } else {
    special.classList.remove("valid");
    special.classList.add("invalid");
  }
}

function validatePassword() {
  var password = document.getElementById("password").value;
  var confirmPassword = document.getElementById("confirm_password").value;

  // Ensure confirm password matches
  if (password !== confirmPassword) {
    alert("Passwords do not match.");
    return false;
  }

  // Final validation before submission
  if (document.querySelectorAll(".tooltip .invalid").length === 0) {
    return true;
  } else {
    alert("Password does not meet the requirements.");
    return false;
  }
}
