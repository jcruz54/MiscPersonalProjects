var lowercase = "abcdefghijklmnopqrstuvwxyz";
var uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
var numbers = "0123456789";
var special = "!@#$%^&*";

var passwordLength;

var hasUppercase = false;
var hasLowercase = false;
var hasNumbers = false;
var hasSpecial = false;

function toggleUppercase(){
    if (!hasUppercase) {hasUppercase = true;}
    else {hasUppercase = false}
}
function toggleLowercase(){
    if (!hasLowercase) {hasLowercase = true;}
    else {hasLowercase = false}
}
function toggleNumbers(){
    if (!hasNumbers) {hasNumbers = true;}
    else {hasNumbers = false}
}
function toggleSpecial(){
    if (!hasSpecial) {hasSpecial = true;}
    else {hasSpecial = false}
}
function setPasswordLength() {
    passwordLength = window.prompt("Enter desired password length:");
}

function makePassword() {
    setPasswordLength();
    var password = "";
    var passwordFeatures = "";

    if (hasLowercase) {passwordFeatures += lowercase;}
    if (hasUppercase) {passwordFeatures += uppercase;}
    if (hasNumbers) {passwordFeatures += numbers;}
    if (hasSpecial) {passwordFeatures += special;}

    for (var i=0; i < passwordLength; i++) {
        password += passwordFeatures.charAt(Math.floor(Math.random() * passwordFeatures.length));
    }
    return password;
}

function showNewPassword() {
    document.getElementById("password").innerHTML = makePassword();
}