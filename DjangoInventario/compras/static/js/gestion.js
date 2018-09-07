$(document).ready(function() {  
    
    $('#TablaCompras').DataTable( {
                    "ordering": false,
                    "info": false,
                    "bLengthChange": false,
                    "bFilter": false,
                    "language": {
                        "url": "//cdn.datatables.net/plug-ins/1.10.19/i18n/Spanish.json"
                    },
                    
    });

    $('#buttonBorrar').addClass('btn btn-danger disabled');
    $('#EditarProductoBtn').addClass('btn btn-primary disabled');
    $( "#TablaCompras_paginate" ).add('');
            
    var table = $('#TablaCompras').DataTable();

            $('#TablaCompras tbody').on( 'click', 'tr', function () {
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