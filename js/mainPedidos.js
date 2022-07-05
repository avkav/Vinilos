

if (document.getElementById("app")) {
    const app = new Vue({
        el: "#app",
        data: {
            pedidos: [],
            errored: false,
            loading: true
        },
        created() {
            var url = 'http://localhost:5000/pedidos'
            this.fetchData(url)
        },
        methods: {
            fetchData(url) {
                fetch(url)
                    .then(response => response.json())
                    .then(data => {
                        this.pedidos = data;
                        this.loading = false;
                    })
                    .catch(err => {
                        this.errored = true
                    })
            },
            eliminar(pedido) {
                const url = 'http://localhost:5000/pedido/' + pedido;
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
