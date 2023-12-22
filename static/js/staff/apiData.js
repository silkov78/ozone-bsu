new Vue ({
    el: "#main",
    data: {
        workersList: [],
    },
    created: function () {
        axios
         .get('../api/staff/v1/workers/')
         .then(response => this.workersList = response.data)

         axios
         .get('../api/staff/v1/workers/')
         .then(response => console.log(response.data))
    }
})

