function login(evt) {
    var email = document.getElementById("InputEmail").value;
    var pass = document.getElementById("InputPassword").value;
    if (email == "a@a" & pass == "a") {
        window.close();
        window.open("homeloged.html");
        return true;
    } else {
        alert("El correo y la contraseña no coinciden");
        evt.preventDefault();
        return false;
    }
}
