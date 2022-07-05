

if (document.getElementById("app")) {
    const app = new Vue({
        el: "#app",
        data: {
            detalles: [],
            errored: false,
            loading: true
        },
        created() {
            var url = 'http://localhost:5000/detalles'
            this.fetchData(url)
        },
        methods: {
            fetchData(url) {
                fetch(url)
                    .then(response => response.json())
                    .then(data => {
                        this.detalles = data;
                        this.loading = false;
                    })
                    .catch(err => {
                        this.errored = true
                    })
            },
            eliminar(detalle) {
                const url = 'http://localhost:5000/detalle/' + detalle;
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
