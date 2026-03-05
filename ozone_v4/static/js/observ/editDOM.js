// page setup
const pageTitle = document.querySelector('title')
pageTitle.innerHTML = 'Наблюдения'

const activeNavPage = document.querySelectorAll('.navbar-list>li>a')[3]
activeNavPage.classList.add('active')


// chart initialization
const ctx = document.getElementById('ozoneChart')

const metricConfig = {
    total_ozone: { label: 'ОСО (Dobson)', color: '#2b7cff' },
    surface_ozone: { label: 'ПСО (ppb)', color: '#00a86b' },
    uvi: { label: 'УФ индекс', color: '#f39c12' },
    uvi_max: { label: 'УФ макс', color: '#e74c3c' },
}

let selectedMetric = 'total_ozone'
let cachedData = null

let ozoneChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: [],
        datasets: [
            {
                label: metricConfig[selectedMetric].label,
                data: [],
                borderColor: metricConfig[selectedMetric].color,
                backgroundColor: metricConfig[selectedMetric].color,
                tension: 0.3,
                pointRadius: 2,
            },
        ]
    },
    options: {
        responsive: true,
        layout: {
            padding: {
                top: 30
            }
        },
        plugins: {
            legend: { display: true },
        },
        scales: {
            x: {
                ticks: { maxRotation: 0, autoSkip: true },
            },
            y: {
                beginAtZero: false,
            },
        },
    }
})

function applyMetric(metricKey) {
    selectedMetric = metricKey

    const cfg = metricConfig[selectedMetric] || metricConfig.total_ozone
    ozoneChart.data.datasets[0].label = cfg.label
    ozoneChart.data.datasets[0].borderColor = cfg.color
    ozoneChart.data.datasets[0].backgroundColor = cfg.color

    if (cachedData) {
        ozoneChart.data.labels = cachedData.labels
        ozoneChart.data.datasets[0].data = cachedData[selectedMetric] || []
    }

    ozoneChart.update()
}


// fetch data from django
async function loadChart(range='week') {

    const endpoint = ctx?.dataset?.endpoint || '/observations/chart-data/'
    const response = await fetch(`${endpoint}?range=${range}`)
    const data = await response.json()

    cachedData = data
    applyMetric(selectedMetric)
}


// button controls
const buttons = document.querySelectorAll('.range-btn')
const metricButtons = document.querySelectorAll('.metric-btn')

buttons.forEach(btn => {

    btn.addEventListener('click', () => {

        buttons.forEach(b => b.classList.remove('active'))
        btn.classList.add('active')

        const range = btn.dataset.range
        loadChart(range)

    })

})

metricButtons.forEach(btn => {
    btn.addEventListener('click', () => {
        metricButtons.forEach(b => b.classList.remove('active'))
        btn.classList.add('active')
        applyMetric(btn.dataset.metric)
    })
})


// initial load
loadChart('week')