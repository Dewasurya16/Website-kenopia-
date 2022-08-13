(function ($) {
  "use strict";

  /* Navbar Scripts */
    // jQuery to collapse the navbar on scroll
    $(window).on('scroll load', function() {
      if ($(".navbar").offset().top > 60) {
        $(".fixed-top").addClass("top-nav-collapse");
      } else {
        $(".fixed-top").removeClass("top-nav-collapse");
      }
      });

$(function () {
  $(document).on('click', 'a.page-scroll', function(event){
var $anchor = $(this);
    $('html, body').stop().animate({
      scrollTop: $($anchor.attr('href')).offset().top
    }, 600, 'easeInOutExpo');
    event.preventDefault();
  });
});

//offcanvas script from bootstrap
$('[data-toggle="offcanvas"], .navbar-nav li a:not(.dropdown-toggle').on('click', function () {
  $('.offcanvas-collapse').toggleClass('open')
})

$('body').prepend('<a href="body" class="back-to-top page-scroll">Back to Top</a>');
var amountScrolled = 700;
$(window).scroll(function() {
  if ($(window).scrollTop() > amountScrolled) {
    $('a.back-to-top').fadeIn('500'); 
  } else { 
    $('a.back-to-top').fadeOut('500');   
  }
});

}) (jQuery);
