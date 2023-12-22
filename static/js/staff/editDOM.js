
const pageTitle = document.querySelector('title')
pageTitle.innerHTML = 'Сотрудники'

const activeNavPage = document.querySelectorAll('.navbar-list>li>a')[4]
activeNavPage.classList.add('active')

function dropComma () {
    console.log('Time2')


    const interestList = document.querySelectorAll('.science-interests__item')

    console.log(interestList)

}




// const interestList = document.querySelectorAll('.science-interests__item')

// console.log(interestList)


// const lastInterest = interests[interests.length - 1]

// console.log(lastInterest)

// const inText = lastInterest.innerText
// lastInterest.innerText = inText.slice(0, -1)

