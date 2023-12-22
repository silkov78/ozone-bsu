new Vue ({
    el: "#observations",
    data: {
        dailyMeasures: [],
        annualReports: []
    },
    created: function () {
        axios
         .get('../api/v1/daily_measures/')
         .then(response => this.dailyMeasures = response.data)

        axios
          .get('../api/v1/annual_reports/')
          .then(response => this.annualReports = response.data)

        axios
          .get('../api/v1/annual_reports/')
          .then(response => console.log(response.data))
    }
})

// console.log(apiData.dailyMeasures)
