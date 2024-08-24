
 // Regex patterns
 const namePattern = /^[a-zA-Z ]{3,50}$/;
 const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
 const passwordPattern = /^[a-zA-Z0-9]{6,}$/;

 // Validation functions
 function NameValidation() {
     const name = document.getElementById('name').value.trim();
     const nameError = document.getElementById('nameError');

     if (name === '') {
         nameError.innerHTML = 'Name is required';
         return false;
     } else if (!namePattern.test(name)) {
         nameError.innerHTML = 'Please enter a valid name';
         return false;
     } else {
         nameError.innerHTML = '';
         return true;
     }
 }

 function EmailValidation() {
     const email = document.getElementById('email').value.trim();
     const emailError = document.getElementById('emailError');

     if (email === '') {
         emailError.innerHTML = 'Email is required';
         return false;
     } else if (!emailPattern.test(email)) {
         emailError.innerHTML = 'Please enter a valid email';
         return false;
     } else {
         emailError.innerHTML = '';
         return true;
     }
 }

 function PasswordValidation() {
     const password = document.getElementById('password').value.trim();
     const passwordError = document.getElementById('passwordError');

     if (password === '') {
         passwordError.innerHTML = 'Password is required';
         return false;
     } else if (!passwordPattern.test(password)) {
         passwordError.innerHTML = 'Password must  contiane alpha,special-char,numbers.';
         return false;
     } else {
         passwordError.innerHTML = '';
         return true;
     }
 }

 function ConfirmPasswordValidation() {
     const confirmPassword = document.getElementById('confirmPassword').value.trim();
     const confirmPasswordError = document.getElementById('confirmPasswordError');
     const password = document.getElementById('password').value.trim();

     if (confirmPassword === '') {
         confirmPasswordError.innerHTML = 'Confirm password is required';
         return false;
     } else if (confirmPassword !== password) {
         confirmPasswordError.innerHTML = 'Passwords do not match';
         return false;
     } else {
         confirmPasswordError.innerHTML = '';
         return true;
     }
 }