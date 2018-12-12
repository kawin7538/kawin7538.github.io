$(document).ready(function() {

	$('form').on('submit', function(event) {

		$.ajax({
			data : {
				starting_point : $('#starting_point').val(),
				destination : $('#destination').val()
			},
			type : 'POST',
			url : {{url_for('show_answer')}}
		})
		.done(function(data) {

			if (data.error) {
				$('#errorAlert').text(data.error).show();
				$('#successAlert').hide();
			}
			else {
				$('#successAlert').text(data.name).show();
				$('#errorAlert').hide();
			}

		});

	});

});