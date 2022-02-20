window.addEventListener('DOMContentLoaded', (event) => {
	btns = document.getElementsByClassName('show_text_button');
	Array.from(btns).forEach(element => {

		element.addEventListener('click', function (event) {
			console.log(element)
			/* element.children[1].classList.toggle('rotate_arrow') */
			element.nextElementSibling.classList.toggle('hide')
		})
	});

});