var modal = document.getElementById("001");
var btn = document.getElementsByClassName("topicos-add")[0];
var span = document.getElementsByClassName("close")[0];
var btnCancelar = document.getElementById("002");

btn.onclick = function() {
    modal.style.display = "block";
}

span.onclick = function() {
    modal.style.display = "none";
}

btnCancelar.onclick = function() {
    modal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
