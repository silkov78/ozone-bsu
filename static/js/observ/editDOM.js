
const pageTitle = document.querySelector('title')
pageTitle.innerHTML = 'Наблюдения'

const activeNavPage = document.querySelectorAll('.navbar-list>li>a')[2]
activeNavPage.classList.add('active')
