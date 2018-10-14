$(document).ready(function() {
    $('#portpholio').lightSlider({
        item:4,
        loop:false,
        slideMove:2,
		slideMargin: 36,
		prevHtml: "&#8249;",
		nextHtml: "&#8250;",
        easing: 'cubic-bezier(0.25, 0, 0.25, 1)',
        speed:600,
		pager: false,
		controls: true,
        responsive : [
            {
                breakpoint:960,
                settings: {
                  }
            }
        ]
    });
	
	$(".filter_but").click(function(){
		$(".filter").toggleClass("active");
	});
	
 });
  
$(window).scroll(function(){

if ($(window).scrollTop() > 70) {
	$('.left_menu').addClass('fixed');
}
else {
	$('.left_menu').removeClass('fixed')
}
});