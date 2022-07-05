const app = new Vue({
    el: "#app",
    data: {
        info: {},
    },
    created() {
        this.fetchData('http://127.0.0.1:5000/productos')
    },
    methods: {
        fetchData(url) {
            fetch(url)
                .then(response => response.json())
                .then(data => {
                    this.info = data
                })
                .catch(err => {
                    console.error(err);
                })
            
        }
    }
})

