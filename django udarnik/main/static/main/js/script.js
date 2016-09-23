$(document).ready(function(){

	var hdoc = 0;
	var hfoot = 0;
	hdoc = $(document).height();
	hfoot = $("#footer").height();
	$("#footer").offset({top:hdoc - hfoot - 6, left:0});

	$("#moon").css({"left": "-400px", "top": "200px"});
	setTimeout(function() {
		    		$("#day").fadeToggle(1000);
		    		$("#sun").css({"left": "-400px", "top": "200px"});
	}, 4000);
	setTimeout(function() {
		    		$("#night").fadeToggle(1000);
		    		$("#moon").css({"left": "-5vw", "top": "-5vw"});
	}, 5000);
	setTimeout(function() {
		    		$("#night").fadeToggle(1000);
		    		$("#moon").css({"left": "-400px", "top": "200px"});
	}, 9000);
	setTimeout(function() {
		    		$("#day").fadeToggle(1000);
		    		$("#sun").css({"left": "-5vw", "top": "-5vw"});
	}, 10000);
	setInterval(function(){
				$("#moon").css({"left": "-400px", "top": "200px"});
				setTimeout(function() {
		    		$("#day").fadeToggle(1000);
		    		$("#sun").css({"left": "-400px", "top": "200px"});
				}, 4000);
				setTimeout(function() {
		    		$("#night").fadeToggle(1000);
		    		$("#moon").css({"left": "-5vw", "top": "-5vw"});
				}, 5000);
				setTimeout(function() {
		    		$("#night").fadeToggle(1000);
		    		$("#moon").css({"left": "-400px", "top": "200px"});
				}, 9000);
				setTimeout(function() {
		    		$("#day").fadeToggle(1000);
		    		$("#sun").css({"left": "-5vw", "top": "-5vw"});
				}, 10000);
	}, 10000);

});