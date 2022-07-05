function guardar() {

    let n = document.getElementById("txtNombre").value
    let e = document.getElementById("txtEmail").value
    let t = document.getElementById("txtTelefono").value
    

    let cliente = {
        nombre: n,
        email: e,
        telefono: t
        
    }
    let url = "http://localhost:5000/clientes"
    var options = {
        body: JSON.stringify(cliente),
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
