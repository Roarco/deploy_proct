
//establecemos el tamaño maximo en bytes del archivo a subir
const max_file_size = 2000000;

//referenciamos el elemento file que deseamos subir
const file = document.getElementById("file");
const extensions = /(.pdf)$/i;

file.addEventListener("change", function() {
   // si no hay archivos, regresamos
    if (this.files.length <= 0) return;

    // Validamos el primer archivo únicamente
    const file = this.files[0];

    if (file.size > max_file_size) {
        alert("El archivo excede el tamaño máximo de 2MB");
        return;
    }
});

var _validFileExtensions = [".pdf"];

function ValidateSingleInput(oInput) {
    if (oInput.type == "file") {
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
    }
    return true;
}