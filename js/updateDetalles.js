var args = location.search.substr(1).split('&');
// lee los argumentos pasados a este formulario
var parts = []
for (let i = 0; i < args.length; ++i) {
    parts[i] = args[i].split('=');
}
console.log(args)
document.getElementById("txtId").value = parts[0][1]
document.getElementById("txtIdPedido").value = parts[1][1]
document.getElementById("txtIdProducto").value = parts[2][1]
document.getElementById("txtPrecio").value = parts[3][1]
document.getElementById("txtCantidad").value = parts[4][1]


function modificar() {
    let id = document.getElementById("txtId").value
    let idPe = document.getElementById("txtIdPedido").value
    let idPr = document.getElementById("txtIdProducto").value
    let p = document.getElementById("txtPrecio").value
    let c = document.getElementById("txtCantidad").value
    


    let detalle = {
        idPedido: idPe,
        idProducto: idPr,
        precio: p,
        cantidad: c
        

    }

    let url = "http://localhost:5000/detalles/"+id
    var options = {
        body: JSON.stringify(detalle),
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        redirect: 'follow'
    }
    fetch(url, options)
        .then(function () {
            console.log("modificado")
            alert("Registro modificado")
            // Handle response we get from the API
        })
        .catch(err => {
            //this.errored = true
            console.error(err);
            alert("Error al Modificar")
        })      
}
