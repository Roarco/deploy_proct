function add() {
  let container = document.getElementById("container");
  let ed = document.getElementById("ed");
  let ad = document.getElementById("ad");
  let btn = document.getElementById("btn");

  let codigo_Student = (document.getElementById("codigo_Student").value = "");
  let name = (document.getElementById("name").value = "");
  let lastname = (document.getElementById("lastname").value = "");
  let IDNumber = (document.getElementById("IDNumber").value = "");

  if (container.style.display === "none") {
    container.style.display = "block";
    ed.style.display = "none";
    ad.style.display = "block";
    btn.innerHTML = "Agregar";
  } else {
    container.style.display = "none";
  }
}

function delet() {
  let container = document.getElementById("container");

  if (container.style.display === "none") {
    container.style.display = "block";
  } else {
    container.style.display = "none";
  }
}

function search() {
  var tabla = document.getElementById("tablaStudent");
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
