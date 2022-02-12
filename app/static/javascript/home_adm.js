
function cerrar(){
    window.history.back();
}

if (window.history.replaceState) {
    window.history.replaceState(null, null, window.location.href);
}