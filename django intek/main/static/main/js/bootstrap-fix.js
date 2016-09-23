$(document).ready(function () {

    $('.dropdown-submenu>a').unbind('click').click(function(e){
    $(this).next('ul').toggle();
    e.stopPropagation();
    e.preventDefault();
    });
    $('.dropdown-submenu').mouseleave(function(){
        $('.dropdown-submenu .dropdown-menu').css("display","none");
    });

        $('.nav li.dropdown-submenu').hover(function () {
            $(this).addClass('sss');
        }, function () {
            $(this).removeClass('sss');
        });
    });
 
    $('ul.dropdown-menu [data-toggle=dropdown]').on('mouseover', function (event) {
        // Avoid following the href location when clicking
        event.preventDefault();
        // Avoid having the menu to close when clicking
        event.stopPropagation();
        // If a menu is already open we close it
        //$('ul.dropdown-menu [data-toggle=dropdown]').parent().removeClass('open');
        // opening the one you clicked on
        $(this).parent().addClass('sss');
 
        var menu = $(this).parent().find("ul");
        var menupos = menu.offset();
 
        var newpos;
        if ((menupos.left + menu.width()) + 30 > $(window).width()) {
            newpos = -menu.width();
        } else {
            newpos = $(this).parent().width();
        }
 
        menu.css({left: newpos});
 
    });
 
    $('a.dropdown-toggle').on('click', function (event) {
        window.location = $(this).prop("href");
    });