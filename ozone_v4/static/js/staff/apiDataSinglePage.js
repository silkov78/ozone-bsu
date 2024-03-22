new Vue ({
// API request for worker's data

    el: "#main",
    data: {
        workerInfo: [],
    },
    created: function () {

        const workerId = window.location.pathname.split('/')[2]

        const url = '../../api/staff/v1/workers/' + workerId + '/'

        axios
         .get(url)
         .then(response => this.workerInfo = response.data)

         axios
         .get(url)
         .then(response => console.log(response.data))

    }
})


