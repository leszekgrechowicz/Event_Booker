


window.addEventListener('DOMContentLoaded', (event) => {

    let div_zoom = document.getElementsByClassName('zoom')

    for (let i=0; i<div_zoom.length; i++) {

        div_zoom[i].addEventListener('mouseenter', (e) => {
            e.preventDefault()
            // div_zoom[i].children[2].style.display = 'unset'
            let button = document.createElement('a')
            button.innerText = 'Make Reservation'
            button.href = '{% url %}'
            button.classList.add('book-button')
            div_zoom[i].appendChild(button)

        });

        div_zoom[i].addEventListener('mouseleave', (e) => {
            e.preventDefault()
            // div_zoom[i].children[2].style.display = 'none'
            div_zoom[i].lastElementChild.remove()
        });
    }

});
