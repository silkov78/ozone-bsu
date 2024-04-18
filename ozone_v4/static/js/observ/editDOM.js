
const pageTitle = document.querySelector('title')
pageTitle.innerHTML = 'Наблюдения'

const activeNavPage = document.querySelectorAll('.navbar-list>li>a')[3]
activeNavPage.classList.add('active')

// Color table
function colorByValues(cell) {
   const intCell = parseInt(cell.innerHTML)

   if (intCell < 5){
       cell.classList.add('observ-cell_green')

   } else if (intCell >= 5 && cell < 7) {
       cell.classList.add('observ-cell_yellow')
   } else {
       cell.classList.add('observ-cell_red')
   }
}

const toColorCells = document.querySelectorAll('.observ-ufi, .observ-ufi-max')
console.log(toColorCells)
toColorCells.forEach(colorByValues)
