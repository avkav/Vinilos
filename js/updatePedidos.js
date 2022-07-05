var args = location.search.substr(1).split('&');
// lee los argumentos pasados a este formulario
var parts = []
for (let i = 0; i < args.length; ++i) {
    parts[i] = args[i].split('=');
}
console.log(args)
document.getElementById("txtId").value = parts[0][1]
document.getElementById("txtIdCliente").value = parts[1][1]
document.getElementById("txtFecha").value = parts[2][1]
document.getElementById("txtMonto").value = parts[3][1]
document.getElementById("txtDireccionEntrega").value = parts[4][1]
document.getElementById("txtEstado").value = parts[5][1]

function modificar() {
    let id = document.getElementById("txtId").value
    let idC = document.getElementById("txtIdCliente").value
    let f = document.getElementById("txtFecha").value
    let m = document.getElementById("txtMonto").value
    let de = document.getElementById("txtDireccionEntrega").value
    let e = document.getElementById("txtEstado").value


    let pedido = {
        idCliente: idC,
        fecha: f,
        monto: m,
        direccionEntrega: de,
        estado: e

    }

    let url = "http://localhost:5000/pedidos/"+id
    var options = {
        body: JSON.stringify(pedido),
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
