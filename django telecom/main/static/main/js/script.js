$(document).ready(function(){
	var hdoc = 0;
	var hfoot = 0;
	hdoc = $(document).height();
	hfoot = $("#footer_box").height();
	$("#footer_box").offset({top:hdoc - hfoot, left:0});


	var sidebar = $("#sidebar_box").offset().top;
	$(window).scroll(function(){

		var scroll = $(this).scrollTop()+62;
		if (sidebar < scroll) {
		    $("#sidebar_box").css({"position" : "fixed", "top" : -1});
		}
		else{
			$("#sidebar_box").css({"position" : "relative"});
		}
	});

	$(".navbar-collapse").each(function(){
	$(".navbar-collapse").css({ maxHeight: $(window).height() - $(".navbar-header").height() + "px" });
	});
	
});