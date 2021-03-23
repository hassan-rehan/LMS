$(document).ready(function() {
	// Header Scroll
	$(window).on('scroll', function() {
		var scroll = $(window).scrollTop();

		if (scroll >= 50) {
			$('#header').addClass('fixed');
			$('.nav-clearfix').addClass('nav-clearfix-scroll');
		} else {
			$('#header').removeClass('fixed');
			$('.nav-clearfix').removeClass('nav-clearfix-scroll');
		}
	});

	// Waypoints
	$('.work').waypoint(function() {
		$('.work').addClass('animated fadeIn');
	}, {
		offset: '75%'
	});
	$('.download').waypoint(function() {
		$('.download .btn').addClass('animated tada');
	}, {
		offset: '75%'
	});

	// Fancybox
	$('.work-box').fancybox();

	// Flexslider
	$('.flexslider').flexslider({
		animation: "fade",
		directionNav: false,
	});

	// Page Scroll
	var sections = $('section')
		nav = $('nav[role="navigation"]');

	$(window).on('scroll', function () {
	  	var cur_pos = $(this).scrollTop();
	  	sections.each(function() {
	    	var top = $(this).offset().top - 76
	        	bottom = top + $(this).outerHeight();
	    	if (cur_pos >= top && cur_pos <= bottom) {
	      		nav.find('a').removeClass('active');
	      		nav.find('a[href="#'+$(this).attr('id')+'"]').addClass('active');
	    	}
	  	});
	});
	nav.find('a').on('click', function () {
	  	var $el = $(this)
	    id = $el.attr('href');
		if($(id).length){
			$('html, body').animate({
				scrollTop: $(id).offset().top - 75
			}, 500);
			return false;
		}
		else
			window.location.replace('/'+id);
	});

	// Mobile Navigation
	$('.nav-toggle').on('click', function() {
		$(this).toggleClass('close-nav');
		nav.toggleClass('open');
		return false;
	});	
	nav.find('a').on('click', function() {
		$('.nav-toggle').toggleClass('close-nav');
		nav.toggleClass('open');
	});

	$("#messages").fadeTo(5000, 500).slideUp(500, function(){
		$("#messages").slideUp(600);
	});
	$("#errors").fadeTo(5000, 500).slideUp(500, function(){
		$("#errors").slideUp(600);
	});

	$('#nav-logo').click(function(e){
		e.preventDefault();
		if($("section#banners").length){
		$('html, body').animate({ scrollTop: $("section#banners").offset().top - 75 });
		}
		else
			window.location.replace('/');
	});
	
	if($(window.location.hash).length > 0){
		setTimeout(() => {
			$('html, body').animate({ scrollTop: $(window.location.hash).offset().top - 75 });
		}, 1500);
	}
});