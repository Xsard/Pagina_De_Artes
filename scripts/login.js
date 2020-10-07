function login(evt) {
    var email = document.getElementById("InputEmail").value;
    var pass = document.getElementById("InputPassword").value;
    if (email == "a@a" & pass == "a") {
        window.close();
        window.open("homeloged.html")
    } else {
        alert("El correo y la contraseña no coinciden")
    }
}

function logout(){
    window.close();
    window.open("login.html")
}