
function generatePassword() {
    const length = parseInt(document.getElementById("passwordLength").value); 
    const charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-="; // Character set for the password
    let password = "";

    for (let i = 0; i < length; i++) {
        const randomIndex = Math.floor(Math.random() * charset.length); 
        password += charset.charAt(randomIndex); 
    }

    // Display the generated password
    const passwordDisplay = document.getElementById("passwordDisplay");
    passwordDisplay.textContent = password;
}
