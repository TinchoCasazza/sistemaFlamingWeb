$(document).ready(function() {  
    
    $('#TableProductos').DataTable( {
                    "ordering": false,
                    "info": false,
                    "bLengthChange": false,
                    "bFilter": false,
                    "language": {
                        "url": "//cdn.datatables.net/plug-ins/1.10.19/i18n/Spanish.json"
                    },
                    "aoColumnDefs": [{ "bVisible": false, "aTargets": [0] }]
    });

    $('#buttonBorrar').addClass('btn btn-danger disabled');
    $('#EditarProductoBtn').addClass('btn btn-primary disabled');
    $( "#TableProductos_paginate" ).add('');
            
    var table = $('#TableProductos').DataTable();

            $('#TableProductos tbody').on( 'click', 'tr', function () {
                $('#buttonBorrar').removeClass('btn btn-danger disabled');
                $('#buttonBorrar').addClass('btn btn-danger');
                $('#EditarProductoBtn').removeClass('btn btn-primary disabled');
                $('#EditarProductoBtn').addClass('btn btn-primary');
                if ( $(this).hasClass('selected') ) {
                    $(this).removeClass('selected');
                    $('#buttonBorrar').removeClass('btn btn-danger');
                    $('#buttonBorrar').addClass('btn btn-danger disabled');
                    $('#EditarProductoBtn').removeClass('btn btn-primary');
                    $('#EditarProductoBtn').addClass('btn btn-primary disabled');
                }
                else {
                    
                    table.$('tr.selected').removeClass('selected');
                    borrarDato = this.cells[0].innerText;
                    $(this).addClass('selected');
                }
            } );

    // Alta Producto

    $('#AltaProductoBtn').click( function () {
        $('form input[name$="Cantidad"]').prop('disabled', true);
        $("#AltaProductoModal").modal();
    } );

    // Editar Producto

    $('#EditarProductoBtn').click( function () {
        var pdata = table.row('.selected').data()
        $('form input[name$="Nombre"]').val(pdata[1]),
        $('form input[name$="Cantidad"]').val(pdata[2]),
        $('form input[name$="Cantidad"]').prop('disabled', true);
        $('form input[name$="PrecioVenta"]').val(parseFloat(pdata[3])),
        $('form input[name$="PrecioCosto"]').val(parseFloat(pdata[4])),
        $('input:hidden[name=PK]').val(pdata[0])
        console.log(pdata)
    } );

           
    $("#EditarProductoBtn").click(function(){
        $("#EditarProductoModal").modal();
    });



} );

function altaElemento(idFormulario , urlRequest) {

    var pdata = $("#" + idFormulario).serialize();
    $.ajax({
        type: 'POST',
        url: urlRequest, //direccion a donde hace las requets
        data: pdata,
        success: function (data) {
            window.location.href = urlRequest; 
        },
        error: function(data) {
        }
    });
}

function editarElemento(idFormulario , urlRequest ) {
    var pdata = $('#' + idFormulario).serialize();
    var pk = $('#id_pk').val();
    $.ajax({
        type: 'POST',
        url: urlRequest,
        data: pdata,
        success: function (data) {
            window.location.href = '/productos/'; 
        },
        error: function(data) {
        }
    })
};

function borrarElemento(idTabla, urlRequest , idBoton) {
    tabla = $("#" + idTabla).DataTable();
    var pdata = tabla.row('.selected').indexes()[0]
    console.log(pdata)
    tabla.row('.selected').remove().draw( false );

        $.ajax({
            type: 'POST',
            url: urlRequest,
            data: { "indice" : pdata },
                success: function (data) {
                console.log(data)
                },
                error: function(data) {
                    console.log(data)
                }
            });

    $('#' + idBoton).removeClass('btn btn-danger');
    $('#' + idBoton).addClass('btn btn-danger disabled');
    console.log("Borraste " + borrarDato);
        
};



// Js de productos
