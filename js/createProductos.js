function guardar() {

    let n = document.getElementById("txtNombre").value
    let p = parseFloat(document.getElementById("txtPrecio").value)
    let s = parseInt(document.getElementById("txtStock").value)
    let i = document.getElementById("txtImagen").value
    let a = document.getElementById("txtAutor").value
    let f = document.getElementById("txtFecha").value

    let producto = {
        nombre: n,
        precio: p,
        stock: s,
        imagen: i,
        autor: a,
        fecha: f
    }
    let url = "http://localhost:5000/productos"
    var options = {
        body: JSON.stringify(producto),
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
