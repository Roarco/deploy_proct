
//establecemos el tamaño maximo en bytes del archivo a subir
const max_file_size = 2000000;

//referenciamos el elemento file que deseamos subir
const file = document.getElementById("file");
const extensions = /(.pdf)$/i;

var _validFileExtensions = [".pdf"];

function ValidateSingleInput(oInput) {
    if (oInput.type == "file") {
        // validamos que la extension sea pdf
        var sFileName = oInput.value;
         if (sFileName.length > 0) {
            var blnValid = false;
            for (var j = 0; j < _validFileExtensions.length; j++) {
                var sCurExtension = _validFileExtensions[j];
                if (sFileName.substr(sFileName.length - sCurExtension.length, sCurExtension.length).toLowerCase() == sCurExtension.toLowerCase()) {
                    blnValid = true;
                    break;
                }
            }

            if (!blnValid) {
                alert("Solo se aceptan archivos con extensiones: " + _validFileExtensions.join(" , "));
                oInput.value = "";
                return false;
            }
        }
        // validamos que el archivo no sea mayor a 2MB
        if (oInput.files[0].size > max_file_size) {
            alert("El archivo excede el tamaño máximo de 2MB");
            oInput.value = "";
            return false;
        }
    }
    return true;
}
const navToggle = document.querySelector(".nav-toggle");
const navMenu = document.querySelector(".nav-menu");

navToggle.addEventListener("click", () => {
    navMenu.classList.toggle("nav-menu_visible");

    if (navMenu.classList.contains("nav-menu_visible")){
        navToggle.setAttribute("arial-label", "Cerrar menú");
    } else {
        navToggle.setAttribute("arial-label", "Abrir menú");
    }
});