const pageTitle = document.querySelector('title')
pageTitle.innerHTML = 'О нас'

const activeNavPage = document.querySelectorAll('.navbar-list>li>a')[4]
activeNavPage.classList.add('active')