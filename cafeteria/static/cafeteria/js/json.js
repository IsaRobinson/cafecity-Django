// $("#buscar").click(function() {
//     $.getJSON('http://127.0.0.1:8000/api/lista_alimentos?format=json', function(data) {
//         var indicadores = data;
//         $("#1").html('$' + indicadores.Alimento.nombre);
//     });
// });


$("#buscar").click(function() {
    $.getJSON('http://127.0.0.1:8000/api/lista_alimentos?format=json', function(data) {
        var alimento = data;

        $.each(alimento, function(i, item) {
            $('#alimentos').append("<tr><td>" + item.nombre + "</td><td>" +
                item.precio + "</td><td>" + item.descripcion + "</td></tr>");

        });


    }).fail(function() {
        console.log('Error al consumir la API!');
    });

});