function login(evt) {
    var email = document.getElementById("InputEmail").value;
    var pass = document.getElementById("InputPassword").value;
    if (email == "a@a" & pass == "a") {
        document.location.href = "homeloged.html";
        evt.preventDefault();
        document.getElementById("InputEmail").value = "";
        document.getElementById("InputPassword").value = "";
        return true;
    } else {
        evt.preventDefault();
        alert("El correo y la contraseña no coinciden");
        document.getElementById("InputPassword").value = "";
        return false;
    }
}