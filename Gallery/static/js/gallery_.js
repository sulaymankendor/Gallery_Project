$(document).ready(function() {

	$('.post').on('click', function() {
		if ($('.file_uploader').val() === '') {

			 $('.img-error-msg').show()
		}else{
			$('.img-error-msg').hide()
		}
		
	})
})