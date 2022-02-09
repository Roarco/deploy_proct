function delet(){
    // devolvemos a la pagina anterior
    window.history.back();
}

function edit(){
    // let data = document.getElementById('data').value;
    // //convertimos aun array
    // let array = data.split(',');

    // //recorremos el array
    // for (let i = 0; i < array.length; i++) {
    //     let codigo_Student = document.getElementById('codigo_Student').value = parseInt(array[0]);
    //     let name = document.getElementById('name').value = array[1];
    //     let lastname = document.getElementById('lastname').value = array[2];
    //     let IDNumber = document.getElementById('IDNumber').value = parseInt(array[4]);
    // }

    let container = document.getElementById('container');
    let ad = document.getElementById('ad');
    let ed = document.getElementById('ed');
    let btn = document.getElementById('btn');
    let form = document.getElementById('form');

    if (container.style.display === 'none') {
        container.style.display = 'block';
        ad.style.display = 'none';
        ed.style.display = 'block';
        btn.innerHTML = 'Editar';
        form.action = '/update_student'
    }
    else{
        container.style.display = 'none';
    }
}
