
const pageTitle = document.querySelector('title')
pageTitle.innerHTML = 'Новости'

const activeNavPage = document.querySelectorAll('.navbar-list>li>a')[3]
activeNavPage.classList.add('active')
