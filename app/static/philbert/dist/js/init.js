/** *************Init JS*********************

 TABLE OF CONTENTS
 ---------------------------
 1.Ready function
 2.Load function
 3.Full height function
 4.philbert function
 5.Chat App function
 6.Resize function
 ** ***************************************/

"use strict";


/*****Load function start*****/
$(window).on('load', function () {
    $(".preloader-it").delay(500).fadeOut("slow");
    /*Progress Bar Animation*/
    let progressAnim = $('.progress-anim');
    if (progressAnim.length > 0) {
        for (let i = 0; i < progressAnim.length; i++) {
            let $this = $(progressAnim[i]);
            $this.waypoint(function () {
                let progressBar = $(".progress-anim .progress-bar");
                for (let i = 0; i < progressBar.length; i++) {
                    $this = $(progressBar[i]);
                    $this.css("width", $this.attr("aria-valuenow") + "%");
                }
            }, {
                triggerOnce: true,
                offset: 'bottom-in-view'
            });
        }
    }
});
/*****Load function* end*****/

/***** Full height function start *****/
let setHeightWidth = function () {
    let height = $(window).height();
    let width = $(window).width();
    $('.full-height').css('height', (height));
    $('.page-wrapper').css('min-height', (height));

    /*Right Sidebar Scroll Start*/
    if (width <= 1007) {
        $('#chat_list_scroll').css('height', (height - 270));
        $('.fixed-sidebar-right .chat-content').css('height', (height - 279));
        $('.fixed-sidebar-right .set-height-wrap').css('height', (height - 219));

    } else {
        $('#chat_list_scroll').css('height', (height - 204));
        $('.fixed-sidebar-right .chat-content').css('height', (height - 213));
        $('.fixed-sidebar-right .set-height-wrap').css('height', (height - 153));
    }
    /*Right Sidebar Scroll End*/

    /*Vertical Tab Height Cal Start*/
    let verticalTab = $(".vertical-tab");
    if (verticalTab.length > 0) {
        for (let i = 0; i < verticalTab.length; i++) {
            let $this = $(verticalTab[i]);
            $this.find('ul.nav').css(
                'min-height', ''
            );
            $this.find('.tab-content').css(
                'min-height', ''
            );
            height = $this.find('ul.ver-nav-tab').height();
            $this.find('ul.nav').css(
                'min-height', height + 40
            );
            $this.find('.tab-content').css(
                'min-height', height + 40
            );
        }
    }
    /*Vertical Tab Height Cal End*/
};
/***** Full height function end *****/

/***** philbert function start *****/
let $wrapper = $(".wrapper");
let philbert = function () {

    /*Counter Animation*/
    let counterAnim = $('.counter-anim');
    if (counterAnim.length > 0) {
        counterAnim.counterUp({
            delay: 10,
            time: 1000
        });
    }

    /*Tooltip*/
    if ($('[data-toggle="tooltip"]').length > 0)
        $('[data-toggle="tooltip"]').tooltip();

    /*Popover*/
    if ($('[data-toggle="popover"]').length > 0)
        $('[data-toggle="popover"]').popover()


    /*Sidebar Collapse Animation*/
    let sidebarNavCollapse = $('.fixed-sidebar-left .side-nav  li .collapse');
    let sidebarNavAnchor = '.fixed-sidebar-left .side-nav  li a';
    $(document).on("click", sidebarNavAnchor, function (e) {
        if ($(this).attr('aria-expanded') === "false")
            $(this).blur();
        $(sidebarNavCollapse).not($(this).parent().parent()).collapse('hide');
    });

    /*Panel Remove*/
    $(document).on('click', '.close-panel', function (e) {
        let effect = $(this).data('effect');
        $(this).closest('.panel')[effect]();
        return false;
    });

    /*Accordion js*/
    $(document).on('show.bs.collapse', '.panel-collapse', function (e) {
        $(this).siblings('.panel-heading').addClass('activestate');
    });

    $(document).on('hide.bs.collapse', '.panel-collapse', function (e) {
        $(this).siblings('.panel-heading').removeClass('activestate');
    });

    /*Sidebar Navigation*/
    $(document).on('click', '#toggle_nav_btn,#open_right_sidebar,#setting_panel_btn', function (e) {
        $(".dropdown.open > .dropdown-toggle").dropdown("toggle");
        return false;
    });
    $(document).on('click', '#toggle_nav_btn', function (e) {
        $wrapper.removeClass('open-right-sidebar open-setting-panel').toggleClass('slide-nav-toggle');
        return false;
    });

    $(document).on('click', '#open_right_sidebar', function (e) {
        $wrapper.toggleClass('open-right-sidebar').removeClass('open-setting-panel');
        return false;

    });

    $(document).on('click', '.product-carousel .owl-nav', function (e) {
        return false;
    });

    $(document).on('click', 'body', function (e) {
        if ($(e.target).closest('.fixed-sidebar-right,.setting-panel').length > 0) {
            return;
        }
        $('body > .wrapper').removeClass('open-right-sidebar open-setting-panel');
        return;
    });

    $(document).on('show.bs.dropdown', '.nav.navbar-right.top-nav .dropdown', function (e) {
        $wrapper.removeClass('open-right-sidebar open-setting-panel');
        return;
    });

    $(document).on('click', '#setting_panel_btn', function (e) {
        $wrapper.toggleClass('open-setting-panel').removeClass('open-right-sidebar');
        return false;
    });
    $(document).on('click', '#toggle_mobile_nav', function (e) {
        $wrapper.toggleClass('mobile-nav-open').removeClass('open-right-sidebar');
        return;
    });


    $(document).on("mouseenter mouseleave", ".wrapper > .fixed-sidebar-left", function (e) {
        if (e.type == "mouseenter") {
            $wrapper.addClass("sidebar-hover");
        } else {
            $wrapper.removeClass("sidebar-hover");
        }
        return false;
    });

    $(document).on("mouseenter mouseleave", ".wrapper > .setting-panel", function (e) {
        if (e.type == "mouseenter") {
            $wrapper.addClass("no-transition");
        } else {
            $wrapper.removeClass("no-transition");
        }
        return false;
    });

    /*Todo*/
    let random = Math.random();
    $(document).on("keypress", "#add_todo", function (e) {
        if ((e.which == 13) && (!$(this).val().length == 0)) {
            $('<li class="todo-item"><div class="checkbox checkbox-success"><input type="checkbox" id="checkbox' + random + '"/><label for="checkbox' + random + '">' + $('.new-todo input').val() + '</label></div></li><li><hr class="light-grey-hr"/></li>').insertAfter(".todo-list li:last-child");
            $('.new-todo input').val('');
        } else if (e.which == 13) {
            alert('Please type somthing!');
        }
        return;
    });

    /*Chat*/
    $(document).on("keypress", "#input_msg_send", function (e) {
        if ((e.which == 13) && (!$(this).val().length == 0)) {
            $('<li class="self mb-10"><div class="self-msg-wrap"><div class="msg block pull-right">' + $(this).val() + '<div class="msg-per-detail mt-5"><span class="msg-time txt-grey">3:30 pm</span></div></div></div><div class="clearfix"></div></li>').insertAfter(".fixed-sidebar-right .chat-content  ul li:last-child");
            $(this).val('');
        } else if (e.which == 13) {
            alert('Please type somthing!');
        }
        return;
    });
    $(document).on("keypress", "#input_msg_send_widget", function (e) {
        if ((e.which == 13) && (!$(this).val().length == 0)) {
            $('<li class="self mb-10"><div class="self-msg-wrap"><div class="msg block pull-right">' + $(this).val() + '<div class="msg-per-detail mt-5"><span class="msg-time txt-grey">3:30 pm</span></div></div></div><div class="clearfix"></div></li>').insertAfter(".chat-for-widgets .chat-content  ul li:last-child");
            $(this).val('');
        } else if (e.which == 13) {
            alert('Please type somthing!');
        }
        return;
    });
    $(document).on("keypress", "#input_msg_send_chatapp", function (e) {
        if ((e.which == 13) && (!$(this).val().length == 0)) {
            $('<li class="self mb-10"><div class="self-msg-wrap"><div class="msg block pull-right">' + $(this).val() + '<div class="msg-per-detail mt-5"><span class="msg-time txt-grey">3:30 pm</span></div></div></div><div class="clearfix"></div></li>').insertAfter(".chat-for-widgets-1 .chat-content  ul li:last-child");
            $(this).val('');
        } else if (e.which == 13) {
            alert('Please type asomthing!');
        }
        return;
    });

    $(document).on("click", ".fixed-sidebar-right .chat-cmplt-wrap .chat-data", function (e) {
        $(".fixed-sidebar-right .chat-cmplt-wrap").addClass('chat-box-slide');
        return false;
    });
    $(document).on("click", ".fixed-sidebar-right #goto_back", function (e) {
        $(".fixed-sidebar-right .chat-cmplt-wrap").removeClass('chat-box-slide');
        return false;
    });

    /*Chat for Widgets*/
    $(document).on("click", ".chat-for-widgets.chat-cmplt-wrap .chat-data", function (e) {
        $(".chat-for-widgets.chat-cmplt-wrap").addClass('chat-box-slide');
        return false;
    });
    $(document).on("click", "#goto_back_widget", function (e) {
        $(".chat-for-widgets.chat-cmplt-wrap").removeClass('chat-box-slide');
        return false;
    });
    /*Horizontal Nav*/
    $(document).on("show.bs.collapse", ".top-fixed-nav .fixed-sidebar-left .side-nav > li > ul", function (e) {
        e.preventDefault();
    });

    /*Slimscroll*/
    $('.nicescroll-bar').slimscroll({
        height: '100%',
        color: '#878787',
        disableFadeOut: true,
        borderRadius: 0,
        size: '4px',
        alwaysVisible: false
    });
    $('.message-nicescroll-bar').slimscroll({
        height: '229px',
        size: '4px',
        color: '#878787',
        disableFadeOut: true,
        borderRadius: 0
    });
    $('.message-box-nicescroll-bar').slimscroll({
        height: '350px',
        size: '4px',
        color: '#878787',
        disableFadeOut: true,
        borderRadius: 0
    });
    $('.product-nicescroll-bar').slimscroll({
        height: '346px',
        size: '4px',
        color: '#878787',
        disableFadeOut: true,
        borderRadius: 0
    });
    $('.app-nicescroll-bar').slimscroll({
        height: '162px',
        size: '4px',
        color: '#878787',
        disableFadeOut: true,
        borderRadius: 0
    });
    $('.todo-box-nicescroll-bar').slimscroll({
        height: '310px',
        size: '4px',
        color: '#878787',
        disableFadeOut: true,
        borderRadius: 0
    });
    $('.users-nicescroll-bar').slimscroll({
        height: '370px',
        size: '4px',
        color: '#878787',
        disableFadeOut: true,
        borderRadius: 0
    });
    $('.users-chat-nicescroll-bar').slimscroll({
        height: '257px',
        size: '4px',
        color: '#878787',
        disableFadeOut: true,
        borderRadius: 0
    });
    $('.chatapp-nicescroll-bar').slimscroll({
        height: '543px',
        size: '4px',
        color: '#878787',
        disableFadeOut: true,
        borderRadius: 0
    });
    $('.chatapp-chat-nicescroll-bar').slimscroll({
        height: '483px',
        size: '4px',
        color: '#878787',
        disableFadeOut: true,
        borderRadius: 0
    });

    /*Product carousel*/
    if ($('.product-carousel').length > 0 && $.fn.owlCarousel) {
        $('.product-carousel').owlCarousel({
            loop: true,
            margin: 15,
            nav: true,
            navText: ["<i class='zmdi zmdi-chevron-left'></i>", "<i class='zmdi zmdi-chevron-right'></i>"],
            dots: false,
            autoplay: true,
            responsive: {
                0: {
                    items: 1
                },
                400: {
                    items: 2
                },
                767: {
                    items: 3
                },
                1399: {
                    items: 4
                }
            }
        });
    }


    /*Refresh Init Js*/
    let refreshMe = '.refresh';
    $(document).on("click", refreshMe, function (e) {
        let panelToRefresh = $(this).closest('.panel').find('.refresh-container');
        let dataToRefresh = $(this).closest('.panel').find('.panel-wrapper');
        let loadingAnim = panelToRefresh.find('.la-anim-1');
        panelToRefresh.show();
        setTimeout(function () {
            loadingAnim.addClass('la-animate');
        }, 100);

        function started() {
        } //function before timeout
        setTimeout(function () {
            function completed() {
            } //function after timeout
            panelToRefresh.fadeOut(800);
            setTimeout(function () {
                loadingAnim.removeClass('la-animate');
            }, 800);
        }, 1500);
        return false;
    });

    /*Fullscreen Init Js*/
    $(document).on("click", ".full-screen", function (e) {
        $(this).parents('.panel').toggleClass('fullscreen');
        $(window).trigger('resize');
        return false;
    });

    /*Nav Tab Responsive Js*/
    $(document).on('show.bs.tab', '.nav-tabs-responsive [data-toggle="tab"]', function (e) {
        let $target = $(e.target);
        let $tabs = $target.closest('.nav-tabs-responsive');
        let $current = $target.closest('li');
        let $parent = $current.closest('li.dropdown');
        $current = $parent.length > 0 ? $parent : $current;
        let $next = $current.next();
        let $prev = $current.prev();
        $tabs.find('>li').removeClass('next prev');
        $prev.addClass('prev');
        $next.addClass('next');
        return;
    });
};
/***** philbert function end *****/

/***** Chat App function Start *****/
let chatAppTarget = $('.chat-for-widgets-1.chat-cmplt-wrap');
let chatApp = function () {
    $(document).on("click", ".chat-for-widgets-1.chat-cmplt-wrap .chat-data", function (e) {
        let width = $(window).width();
        if (width <= 1007) {
            chatAppTarget.addClass('chat-box-slide');
        }
        return false;
    });
    $(document).on("click", "#goto_back_widget_1", function (e) {
        let width = $(window).width();
        if (width <= 1007) {
            chatAppTarget.removeClass('chat-box-slide');
        }
        return false;
    });
};
/***** Chat App function End *****/

let boxLayout = function () {
    if ((!$wrapper.hasClass("rtl-layout")) && ($wrapper.hasClass("box-layout")))
        $(".box-layout .fixed-sidebar-right").css({right: $wrapper.offset().left + 300});
    else if ($wrapper.hasClass("box-layout rtl-layout"))
        $(".box-layout .fixed-sidebar-right").css({left: $wrapper.offset().left});
}
boxLayout();

/***** Resize function start *****/
$(window).on("resize", function () {
    setHeightWidth();
    boxLayout();
    chatApp();
}).resize();
/***** Resize function end *****/



/*****Ready function start*****/
$(document).ready(function () {
    philbert();
    let $preloader = $(".preloader-it > .la-anim-1");
    $preloader.addClass('la-animate');
});
/*****Ready function end*****/