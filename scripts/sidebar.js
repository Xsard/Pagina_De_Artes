const toggle = document.querySelector('.toggle-btn');
function toggleBtn(){
    document.getElementById('sidebar').classList.toggle('acti');
}
function logout(){
    window.close();
    window.open("login.html")
}