$(document).ready(function(){

	$(".nav a[href='"+document.location.pathname+"']").css({
		"text-decoration" : "underline"
	});
	
	var hdoc = 0;
	var hfoot = 0;
	hdoc = $(document).height();
	hfoot = $("#footer").height();
	$("#footer").offset({top:hdoc - hfoot - 6, left:0});

	$(document).mousemove(function(e){
		$("#logo").css({
			"transform" : "rotateX("+ e.pageY /2 +"deg) rotateY("+ e.pageX /2 +"deg)",
			"-moz-transform" : "rotateX("+ e.pageY /2 +"deg) rotateY("+ e.pageX /2 +"deg)",
			"-o-transform" : "rotateX("+ e.pageY /2 +"deg) rotateY("+ e.pageX /2 +"deg)",
			"-webkit-transform" : "rotateX("+ e.pageY /2 +"deg) rotateY("+ e.pageX /2 +"deg)"
		});
	});

    /*$('.dropdown-submenu>a').unbind('click').click(function(e){
    	$(this).parent().addClass('test');
  		$(this).next('ul').toggle();
   		e.stopPropagation();
    	e.preventDefault();
    });
    $('.dropdown-submenu').mouseleave(function(){
    	$(this).removeClass('test');
        $('.dropdown-submenu .dropdown-menu').css("display","none");
    });
	$("#button-sidebar .icon-bar").css("border", "1px solid #2780e3");
	$(".navbar-collapse").each(function(){
	$(".navbar-collapse").css({ maxHeight: $(window).height() - $(".navbar-header").height() + "px" });
	});


	var sidebar = $("#sidebar").offset().top;
	$(window).scroll(function(){

		var scroll = $(this).scrollTop()+50;
		if (sidebar < scroll) {
			$("#content").css("border-top", "6px solid #fff");
			$("#nav-sidebar").addClass("navbar-inverse");
			$("#containersidebar").css({"position" : "fixed",
				"opacity" : "0.9"
			});
			$("#button-sidebar .icon-bar").css("border", "");
		}
		else{
			$("#content").css("border-top", "6px solid #000099");
			$("#nav-sidebar").removeClass("navbar-inverse");
			$("#containersidebar").css({"position" : "relative",
				"opacity" : "1"
			});
			$("#button-sidebar .icon-bar").css("border", "1px solid #2780e3");
		};
	});*/
});