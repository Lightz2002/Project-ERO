// Eye (Show Password)
var eye = document.querySelector('i.fa-eye');
var input_password = document.getElementById('id_password');


function showPassword() {
	eye.setAttribute('class', 'fa fa-eye-slash');
	eye.style.position = 'absolute';
	eye.style.right = '21%';
	input_password.type = 'text';
}

function hidePassword() {
	eye.setAttribute('class', 'fa fa-eye');
	input_password.type = 'password';
}

eye.addEventListener('click', function() {
	if (input_password.type == 'password') {
		showPassword();
	} else {
		hidePassword();
	}
	
});
