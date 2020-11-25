function validaciones(evt) {
    var email = document.getElementById("EmailPer").value;
    var pass = document.getElementById("Pass").value;
    var passCom = document.getElementById("PassCom").value;
    var emailCont = document.getElementById("EmailCont").value;
    var nombres = document.getElementById("Nombres").value;
    var NomArt = document.getElementById("NomArt").value;
    var Edad = document.getElementById("Edad").value;
    if (pass.length == 0 || /^\s+$/.test(pass) || email.length == 0 || /^\s+$/.test(email) || emailCont.length == 0 || /^\s+$/.test(emailCont) || nombres.length == 0 || /^\s+$/.test(nombres) || passCom.length == 0 || /^\s+$/.test(passCom) || NomArt.length == 0 || /^\s+$/.test(NomArt) || Edad.length == 0 || /^\s+$/.test(Edad)) {
        alert("No pueden haber campos vacios")
        evt.preventDefault();
    } else {
        if (pass === passCom) {
            if (Edad < 8 || isNaN(parseInt(Edad))) {
                alert("La edad no es un número o es menor a 18")
                evt.preventDefault();
            } 
        } else {
            alert("Las contraseñas no coinciden")
            evt.preventDefault();
        }
    }

}