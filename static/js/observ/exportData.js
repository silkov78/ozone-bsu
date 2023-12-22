
axios
  .get('../api/v1/daily_measures/')
  .then(response => jsonToCSV(response.data))


function jsonToCSV(inputData) {

    const headers = Object.keys(inputData[0]).toString()

    const values = inputData.map(item => {
        return Object.values(item).toString()
    })

    const csv = [headers, ...values].join('\n')

    csvDownload(csv)
}

function csvDownload(input) {

    const blob = new Blob([input], {type: 'measures/csv'})

    const url = URL.createObjectURL(blob)

    const downloadButton = document.querySelector('#exportCSV')

    downloadButton.download = 'observations.csv'
    downloadButton.href = url
}