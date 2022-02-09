
function add(){
    let container = document.getElementById('container');
    let ed = document.getElementById('ed');
    let ad = document.getElementById('ad');
    let btn = document.getElementById('btn');

    let codigo_Student = document.getElementById('codigo_Student').value = '';
    let name = document.getElementById('name').value = '';
    let lastname = document.getElementById('lastname').value = '';
    let IDNumber = document.getElementById('IDNumber').value = '';

    if (container.style.display === 'none') {
        container.style.display = 'block';
        ed.style.display = 'none';
        ad.style.display = 'block';
        btn.innerHTML = 'Agregar';
    }
    else{
        container.style.display = 'none';
    }
}

function delet(){
    let container = document.getElementById('container');

    if (container.style.display === 'none') {
        container.style.display = 'block';
    }
    else{
        container.style.display = 'none';
    }
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
