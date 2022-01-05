window.addEventListener('DOMContentLoaded', (event) => {

    let div_zoom = document.getElementsByClassName('zoom')

    for (let i = 0; i < div_zoom.length; i++) {

        div_zoom[i].addEventListener('mouseenter', (e) => {
            e.preventDefault()
            let button = document.createElement('a')
            button.innerText = 'Book your seat Today !'
            button.href = div_zoom[i].firstElementChild.getAttribute('data-url')
            button.classList.add('book-button')
            div_zoom[i].appendChild(button)

        });

        div_zoom[i].addEventListener('mouseleave', (e) => {
            e.preventDefault()
            div_zoom[i].lastElementChild.remove()
        });
    }

    let messageToDelete = document.getElementsByClassName('alert')

    if (messageToDelete.length > 0) {
        setTimeout(function () {
            messageToDelete[0].remove()

        }, 6000);
    }

    let freeSpaces = document.getElementsByClassName('free-spaces')

        for (let i =0; i < freeSpaces.length; i++) {
            if (freeSpaces[i].getAttribute('data-spaces') < 20) {
                freeSpaces[i].parentElement.classList.add('fully-booked')
                freeSpaces[i].nextElementSibling.style.color = "red"

            }

            freeSpaces[i].parentElement.addEventListener('mousenter', (e) => {
                coverDiv = document.createElement()
            } )
    }

});
