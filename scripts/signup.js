function validaciones(evt) {
    var email = document.getElementById("EmailPer").value;
    var pass = document.getElementById("Pass").value;
    var passCom = document.getElementById("PassCom").value;
    var emailCont = document.getElementById("EmailCont").value;
    var nombres = document.getElementById("Nombres").value;
    var NomArt = document.getElementById("NomArt").value;
    var formulario = document.getElementById("")
    if (pass.length == 0 || /^\s+$/.test(pass)) {
        alert("No pueden haber campos vacios")
        evt.preventDefault();               
    } else {
        alert("a")
    }

}