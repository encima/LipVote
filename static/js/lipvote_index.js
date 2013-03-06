$(document).ready(function() {
	$(".row").click(function() {
		var $id = $(this).children().first();
		var $ votes = $(this).children().last();
	});
});