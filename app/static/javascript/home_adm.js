
function cerrar(){
    window.history.back();
}

if (window.history.replaceState) {
    window.history.replaceState(null, null, window.location.href);
}
function search() {
var tabla = document.getElementById("tablaDocument");
var busqueda = document.getElementById("inputSearch").value.toLowerCase();
var cellsOfRow = "";
var found = false;
var compareWith = "";
for (var i = 1; i < tabla.rows.length; i++) {
    cellsOfRow = tabla.rows[i].getElementsByTagName("td");
    found = false;
    for (var j = 0; j < cellsOfRow.length && !found; j++) {
        compareWith = cellsOfRow[j].innerHTML.toLowerCase();
    if (busqueda.length == 0 || compareWith.indexOf(busqueda) > -1) {
        found = true;
    }
    }
    if (found) {
        tabla.rows[i].style.display = "";
    } else {
        tabla.rows[i].style.display = "none";
    }
    }
}

//funcion para cambiar color de letra dependiendo el estado de tabla

var tabla = document.getElementById("tablaDocument");
var cellsOfRow = "";
for (var i = 1; i < tabla.rows.length; i++) {
    cellsOfRow = tabla.rows[i].getElementsByTagName("td");
    if(cellsOfRow[4].innerHTML == "Rechazado"){
        cellsOfRow[4].style.color = "#820933";
    }
    if(cellsOfRow[4].innerHTML == "Aceptado"){
        cellsOfRow[4].style.color = "#315C2B";
    }
    if(cellsOfRow[4].innerHTML == "En revision"){
        cellsOfRow[4].style.color = "#2196f3";
    }
}
