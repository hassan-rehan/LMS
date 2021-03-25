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

	//Updating book clicks
	$(".store-book-link").click(function(){
		$.post($(this).attr('href')+'/update-clicks', 
			{csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()},
			function(data){
				if(data="success")
					console.log("Clicks updated successfully.");
				else
					console.log("Clicks not updated successfully.");
			}
		);
	});

	//book reservation
	$("#reserve-button").click(function(e){
		e.preventDefault();
		var btn = $(this);
		btn.attr('disabled',true);
		btn.html('<i class="fas fa-spinner fa-spin"></i>');
		$.post(btn.attr('href'), 
			{csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()},
			function(data){
				if(data == "success"){
					btn.html("Reserved successfully.");
				}
				else{
					btn.attr('disabled',false);
					btn.html("Reserve");
					alert(data);
				}
			}
		);
	});

	$('.search-panel .dropdown-menu').find('a').click(function(e) {
		e.preventDefault();
		var param = $(this).attr("href").replace("#","");
		var concept = $(this).text();
		$('.search-panel label#search_concept').text(concept);
		$('.input-group #search_param').val(param);
	});
	
	if($('#search').length){
		$('#search').on('keyup', function(evt){
			if(evt.keyCode === 13){
				alert('You pressed enter');
			} 
		}); 
	}
});