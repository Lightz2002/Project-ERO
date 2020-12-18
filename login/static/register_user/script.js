/*jshint esversion : 6 */

var input_email = document.querySelector('input[type="email"]');
var label = document.querySelector('label[for="id_email"]');

input_email.addEventListener('change', function(){
	label.style.transform = 'translateY(-15px)';
	label.style.color = '#003366';
});

input_email.addEventListener('empty', function(){
	label.style.transform = 'none';
	label.style.color = 'grey';
});




// Eye (Show Password)
var eye = document.querySelectorAll('i.fa-eye');
var input_password = document.querySelectorAll('input[type = "password"]');


eye[0].addEventListener('click', function() {
		if (input_password[0].type == 'password') {
				eye[0].setAttribute('class', 'fa fa-eye-slash');
				eye[0].style.position = 'absolute';
				eye[0].style.right = '21%';
				input_password[0].type = 'text';
		} else {
			eye[0].setAttribute('class', 'fa fa-eye');	
			input_password[0].type = 'password';
		}
});



eye[1].addEventListener('click', function() {
		if (input_password[1].type == 'password') {
				eye[1].setAttribute('class', 'fa fa-eye-slash');
				eye[1].style.position = 'absolute';
				eye[1].style.right = '21%';
				input_password[1].type = 'text';
		} else {
			eye[1].setAttribute('class', 'fa fa-eye');	
			input_password[1].type = 'password';
		}
});
