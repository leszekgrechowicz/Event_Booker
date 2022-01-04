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

    if (messageToDelete) {
        setTimeout(function () {


            messageToDelete.forEach(function (element) {
                element.remove();
            })

        }, 3000);
    }

});
