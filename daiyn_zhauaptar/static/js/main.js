$(".link-nav").click(function () {
    $(this).toggleClass("link-nav-open");
});

$(".humb-icons").click(function () {
    $(".left-navbar").toggleClass("nav-open");
    $("html").toggleClass("scroll-none");
});
$(".sub-link a").click(function () {
    $(".left-navbar").toggleClass("nav-open");
    $("html").toggleClass("scroll-none");
});
$(".overlay-menu").click(function () {
    $(".left-navbar").toggleClass("nav-open");
    $("html").toggleClass("scroll-none");
});

$(".search-icons").click(function () {
    $(".header-right .input-search").toggleClass("search-open");
});
$(".more-load").click(function () {
    $(this).css('display', 'none')
    $(".school-subject-description").toggleClass("school-subject-d-open");
});
// якари
$(function () {
    $(".answer-menu a").click(function () {
        var _href = $(this).attr("href");
        $("html, body").animate({
            scrollTop: $(_href).offset().top + "px"
        });
        return false;
    });
});

$(document).ready(function () {
    var owl = $('.popular-books');
    owl.owlCarousel({
        nav: true,
        navText: ['<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M14.2981 5.98959L8.28772 12L14.2981 18.0104L15.7123 16.5962L11.1161 12L15.7123 7.40381L14.2981 5.98959Z" fill="#8D9FBB"/></svg>', '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M9.70193 18.0104L15.7123 12L9.70194 5.98959L8.28772 7.40381L12.8839 12L8.28772 16.5962L9.70193 18.0104Z" fill="#8D9FBB"/></svg>'],
        margin: 20,
        loop: false,
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 2
            },
            1000: {
                items: 4
            }
        }
    })
});
$(document).ready(function() {
    var owl = $(".popular-books");
    owl.owlCarousel({
        nav: true,
    });
  });


