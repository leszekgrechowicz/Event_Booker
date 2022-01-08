window.addEventListener('DOMContentLoaded', (event) => {

    // Footer date current year

    let dateYearNow = new Date().getFullYear()
    let yearSpan = document.getElementById('year')
    yearSpan.innerText = dateYearNow.toString()

    // Zoom div and create book event button on mouseenter

    let div_zoom_list = document.getElementsByClassName('zoom')
    zoomCreateBookButton(div_zoom_list);

    // Clear django message/alert after 6 seconds

    let messageToDelete = document.getElementsByClassName('alert')
    clearMessage(messageToDelete);

    // Check available free spaces and if non make div dim and link inaccessible

    let freeSpaces = document.getElementsByClassName('free-spaces')

    checkFreeSpaces(freeSpaces);

    // hidden admin login link

    let masterPin = "4891"

    let noFour = document.getElementById('4')
    let noEight = document.getElementById('8')
    let noNine = document.getElementById('9')
    let noOne = document.getElementById('1')

    let pin = '4891'
    let pinProvided = ''

    noNine.addEventListener('click', (e) => {
        pinProvided += '9'

    })

    noEight.addEventListener('click', (e) => {
        pinProvided += '8'

    })

    noFour.addEventListener('click', (e) => {
        pinProvided += '4'

    })

    noOne.addEventListener('click', (e) => {
        pinProvided += '1'

        if (pinProvided === masterPin) {

            let header = document.getElementById('header-tag')
            console.log(header)

            header.style.position = 'relative'
            let linkDiv = document.createElement('div')
            let link = document.createElement('a')
            link.setAttribute('href', '/829admin976/')
            link.innerText = 'Admin Link'
            link.style.position = 'absolute'
            link.style.right = '10%'
            link.style.top = '40px'
            link.style.textDecoration = 'none'
            link.classList += 'book-button'
            linkDiv.appendChild(link)
            header.appendChild(linkDiv)

        }
    })
});


function zoomCreateBookButton(divList) {

    for (let i = 0; i < divList.length; i++) {

        divList[i].addEventListener('mouseenter', (e) => {
            e.preventDefault()
            let button = document.createElement('a')
            button.innerText = 'Book your seat Today !'
            button.href = divList[i].firstElementChild.getAttribute('data-url')
            button.classList.add('book-button')
            button.setAttribute('id', 'buttonBook')
            divList[i].appendChild(button)

        });

        divList[i].addEventListener('mouseleave', (e) => {
            e.preventDefault()
            divList[i].lastElementChild.remove()
        });
    }
}

function clearMessage(message) {

    if (message.length > 0) {
        setTimeout(function () {
            message[0].remove()

        }, 6000);
    }
}

function checkFreeSpaces(eventsList) {

    for (let i = 0; i < eventsList.length; i++) {

        if (eventsList[i].getAttribute('data-spaces') < 20) {
            eventsList[i].parentElement.classList.add('fully-booked')
            eventsList[i].nextElementSibling.style.color = "red"
            eventsList[i].parentElement.addEventListener('mouseenter', (e) => {
                let button = document.getElementById('buttonBook')
                button.innerText = "Fully Booked !"
                button.style.background = 'red'
                button.style.color = 'white'
                button.setAttribute('href', 'javascript:void(0)')
            })
        }
    }
}


