function guardar() {

    let idC = document.getElementById("txtIdCliente").value
    let f = document.getElementById("txtFecha").value
    let m = document.getElementById("txtMonto").value
    let de = document.getElementById("txtDireccionEntrega").value
    let e = document.getElementById("txtEstado").value
    


    // Pedido

    let pedido = {
        idCliente: idC,
        fecha: f,
        monto: m,
        direccionEntrega: de,
        estado: e
        
    }
    let url = "http://localhost:5000/pedidos"
    var options = {
        body: JSON.stringify(pedido),
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
       // redirect: 'follow'
    }
    fetch(url, options)
        .then(function () {
            console.log("creado")
            alert("Grabado")

            // Handle response we get from the API
        })
        .catch(err => {
            //this.errored = true
            alert("Error al grabar" )
            console.error(err);
        })


    
        
    
}
