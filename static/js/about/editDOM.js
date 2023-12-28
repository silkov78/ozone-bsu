const pageTitle = document.querySelector('title')
pageTitle.innerHTML = 'О нас'

const activeNavPage = document.querySelectorAll('.navbar-list>li>a')[1]
activeNavPage.classList.add('active')