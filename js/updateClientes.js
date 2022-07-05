var args = location.search.substr(1).split('&');
// lee los argumentos pasados a este formulario
var parts = []
for (let i = 0; i < args.length; ++i) {
    parts[i] = args[i].split('=');
}
console.log(args)
document.getElementById("txtId").value = parts[0][1]
document.getElementById("txtNombre").value = parts[1][1]
document.getElementById("txtEmail").value = parts[2][1]
document.getElementById("txtTelefono").value = parts[3][1]


function modificar() {
    let id = document.getElementById("txtId").value
    let n = document.getElementById("txtNombre").value
    let e = document.getElementById("txtEmail").value
    let t = document.getElementById("txtTelefono").value
 
    let cliente = {
        nombre: n,
        email: e,
        telefono: t
    }

    let url = "http://localhost:5000/clientes/"+id
    var options = {
        body: JSON.stringify(cliente),
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
