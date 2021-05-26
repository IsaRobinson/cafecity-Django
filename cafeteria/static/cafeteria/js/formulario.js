var nombre = document.getElementById('uname');
var email = document.getElementById('email');
var comentarios = document.getElementById('comentarios');
var error = document.getElementById('error');
error.style.color = 'red';

function enviarformulario() {
    console.log('enviando mensaje');

    var mensajesError = [];

    if (nombre.value === null || nombre.value === '') {
        mensajesError.push('ingrese su nombre')
    } else
    if (email.value === null || email.value === '') {
        mensajesError.push('ingrese su email')
    } else
    if (comentarios.value === null || comentarios.value === '') {
        mensajesError.push('ingrese su comentario')
    } else {
        alert("se envio su sugerencia");
    }
    error.innerHTML = mensajesError.join(' , ');

    return false;

}

function enviarcorreo() {
    var nombre = $("#uname").val();
    var email = $("#email").val();
    var comentario = $("#comentarios").val();

    alert($nombre + " entrego sugerencia ");

}
$(document).ready(function() {


    $("#botan").click(function() {
        Alert("se envio su sugerencia");




    });

});