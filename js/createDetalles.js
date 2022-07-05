function guardar() {

    
    let idPe = document.getElementById("txtIdPedido").value
    let idPr = document.getElementById("txtIdProducto").value
    let p = document.getElementById("txtPrecio").value
    let c = document.getElementById("txtCantidad").value


    // Detalle
    
    let detalle = {
        idPedido: idPe,
        idProducto: idPr,
        precio: p,
        cantidad: c
        
        
    }
    let url = "http://localhost:5000/detalles"
    var options = {
        body: JSON.stringify(detalle),
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
