function delet() {
  window.history.back();
}

function edit() {
  let container = document.getElementById("container");
  let ad = document.getElementById("ad");
  let ed = document.getElementById("ed");
  let btn = document.getElementById("btn");
  let form = document.getElementById("form");

  if (container.style.display === "none") {
    container.style.display = "block";
    ad.style.display = "none";
    ed.style.display = "block";
    btn.innerHTML = "Editar";
    form.action = "/update_student";
  } else {
    container.style.display = "none";
  }
}
