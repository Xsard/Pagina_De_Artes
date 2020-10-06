function login(evt) {
    var email = document.getElementById("InputEmail").value;
    var pass = document.getElementById("InputPassword").value;
    if (email == "a@a" & pass=="a") {
        location.href = "home.html"
        evt.preventDefault();
    } else {
        alert("El correo y la contraseña no coinciden")
    }
}
