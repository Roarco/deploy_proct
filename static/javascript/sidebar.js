//Ejecutar funcione el evento click
document.getElementById("btn_open").addEventListener("click", open_close_menu);
// Ejecutar funcion en evento click
var side_menu = document.getElementById("menu_side");
var btn_open = document.getElementById("btn_open");
var body = document.getElementById("body");
var header = document.getElementById("header");

//evento para mostrar y ocultar
    function open_close_menu(){
        body.classList.toggle("body_move");
        side_menu.classList.toggle("menu__side_move");
        header.classList.toggle("header_move")
    }