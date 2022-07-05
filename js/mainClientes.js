

if (document.getElementById("app")) {
    const app = new Vue({
        el: "#app",
        data: {
            clientes: [],
            errored: false,
            loading: true
        },
        created() {
            var url = 'http://localhost:5000/clientes'
            this.fetchData(url)
        },
        methods: {
            fetchData(url) {
                fetch(url)
                    .then(response => response.json())
                    .then(data => {
                        this.clientes = data;
                        this.loading = false;
                    })
                    .catch(err => {
                        this.errored = true
                    })
            },
            eliminar(cliente) {
                const url = 'http://localhost:5000/cliente/' + cliente;
                var options = {
                    method: 'DELETE',
                }
                fetch(url, options)
                    .then(res => res.text()) // or res.json()
                    .then(res => {
                        location.reload();
                    })
            }
        }
    })
}
