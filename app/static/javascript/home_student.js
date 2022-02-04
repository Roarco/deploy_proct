
//establecemos el tamaño maximo en bytes del archivo a subir
var max_file_size = 2000000;

//referenciamos el elemento file que deseamos subir
var file = document.getElementById("file");

file.addEventListener("change", function() {
   // si no hay archivos, regresamos
    if (this.files.length <= 0) return;

    // Validamos el primer archivo únicamente
    var file = this.files[0];

    if (file.size > max_file_size) {
        alert("El archivo excede el tamaño máximo de 2MB");
        return;
    }
});