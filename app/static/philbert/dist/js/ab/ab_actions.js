// This js work is based on:
// Copyright (c) 2014, Serge S. Koval and contributors. See AUTHORS
// for more details.
//

//------------------------------------------------------
// AdminActions holds methods to handle UI for actions
//------------------------------------------------------
var AdminActions = function() {

    var chkAllFlag = true;
    var multiple = false;
    var single = false;
    var single_delete = false;
    var action_name = '';
    var action_url = '';
    var action_confirmation = '';
    var row_checked_class = 'success';

    this.execute_multiple = function(name, confirmation) {
        multiple = true;
        action_name = name;
        action_confirmation = confirmation;
        var selected = $('input.action_check:checked').length;

        if (selected == 0) {
            ab_alert('No row selected');
            return false;
        }

        if (!!confirmation) {
            $('#modal-confirm').modal('show');
        }
        else {
            form_submit();
        }
    };

    function single_form_submit() {
        form = $('#action_form');
        $(form).attr('action', action_url);
        form.trigger("submit");
        return false;
    }

    this.execute_single = function(url, confirmation, title = 'User confirmation needed!') {
        single = true;
        action_url = url;
        action_confirmation = confirmation;

        if (!!confirmation) {
            $('#modal-confirm').modal('show');
        }
        else {
            single_form_submit();
        }

        let $title = $('#modal-confirm #myModalLabel')
            $title.text(title)
    };

    this.execute_single_delete = function(url, confirmation) {
        single_delete = true;
        action_url = url;
        action_confirmation = confirmation;
        $("#modal-confirm .modal-body").text(confirmation);
        $('#modal-confirm').modal('show');
    };

    function form_submit() {
        // Update hidden form and submit it
        var form = $('#action_form');
        $('#action', form).val(action_name);

        $('input.action_check', form).remove();
        $('input.action_check:checked').each(function() {
            form.append($(this).clone());
        });

        form.trigger('submit');
        return false;
    }

    //----------------------------------------------------
    // Event for checkbox with class "action_check_all"
    // will check all checkboxes with class "action_check
    //----------------------------------------------------
    $('.action_check_all').on('click', function() {
        $('.action_check').prop('checked', chkAllFlag).trigger("change");
        chkAllFlag = !chkAllFlag;
    });

    //----------------------------------------------------
    // Event for checkbox with class "action_check"
    // will add class 'active' to row
    //----------------------------------------------------
    $('.action_check').on('change', function() {
        var thisClosest = $(this).closest('tr'),
        checked = this.checked;
        $(this).closest('tr').add(thisClosest )[checked ? 'addClass' : 'removeClass'](row_checked_class);
    });

    //------------------------------------------
    // Event for modal OK button click (confirm.html)
    // will submit form or redirect
    //------------------------------------------
    $('#modal-confirm-ok').on('click', function(e) {
        if (multiple) {
            form_submit();
        }
        if (single) {
            single_form_submit();
        }
        // POST for delete endpoint necessary to send CSRF token from list view
        if (single_delete) {
            var form = undefined;
            if ( $('#action_form').length ) {
                form = $('#action_form');
            }
            else {
                form = $('#delete_form');
            }            $(form).attr('action', action_url);
            form.trigger('submit');
            return false;
        }
    });

    //------------------------------------------
    // Event for modal show (confirm.html)
    // will replace modal inside text (div class modal-text) with confirmation text
    //------------------------------------------
    $('#modal-confirm').on('show.bs.modal', function(e) {
        if (multiple || single) {
            $('.modal-text').html(action_confirmation);
        }
    });

};






$(document).ready(function () {
    $("body").on("click", "[data-act=ajax-modal]", function () {
        var data = {ajaxModal: 1},
            url = $(this).attr("data-href"),
            modalSize = $(this).attr("data-modal-size"),
            title = $(this).attr("data-title"),
            position = $(this).attr("data-position") ? '-' + $(this).attr("data-position") : '';

        let modal_id = "#ajax-modal" + position;

        if (!url) {
            console.log("BS Ajax Modal: Set data-href!");
            return false;
        }
        if (title) {
            $(modal_id + " #ajax-modal-title").html(title);
        } else {
            $(modal_id + " #ajax-modal-title").html(
                $(modal_id + " #ajax-modal-title").attr("data-title")
            );
        }

        $(modal_id + " #ajax-modal-content").html($(modal_id + " #ajax-modal-original-content").html());

        $(modal_id + " #ajax-modal-content")
            .find(".original-modal-body")
            .removeClass("original-modal-body")
            .addClass("modal-body");

        $(modal_id).modal("show");

        $(this).each(function () {
            $.each(this.attributes, function () {
                if (this.specified && this.name.match("^data-post-")) {
                    var dataName = this.name.replace("data-post-", "");
                    data[dataName] = this.value;
                }
            });
        });

        ajaxModalXhr = $.ajax({
            url: url,
            data: data,
            cache: false,
            type: "GET",
            success: function (response) {
                var modalDialog = $(modal_id).find(".modal-dialog");

                if (modalSize !== 'undefined' && modalSize.length > 0) {

                    modalDialog
                        .removeClass("modal-sm")
                        .removeClass("modal-md")
                        .removeClass("modal-lg");
                    // modalDialog.addClass(modalSize + " w-100");
                    modalDialog.addClass(modalSize);
                }

                $(modal_id + " #ajax-modal-content").html(response);
                let $scroll = $(modal_id + " #ajax-modal-content").find(".modal-body"),
                    height = $scroll.height(),
                    maxHeight = $(window).height() - 200;
                if (height > maxHeight) {
                    height = maxHeight;
                    if ($.fn.mCustomScrollbar) {
                        $scroll.mCustomScrollbar({setHeight: height, theme: "minimal-dark", autoExpandScrollbar: true});
                    }
                }
            },
            statusCode: {
                404: function () {
                    $(modal_id + " #ajax-modal-content")
                        .find(".modal-body")
                        .html(
                            '<div class="alert alert-danger m-b-0" role="alert">Request failed, please try again later.</div>'
                        );
                    // toastr.error("404: Page not found.");
                }
            },
            error: function () {
                $(modal_id + " #ajax-modal-content")
                    .find(".modal-body")
                    .html(
                        '<div class="alert alert-danger m-b-0" role="alert">Request failed, please try again later.</div>'
                    );
                // toastr.error("500: Internal Server Error.");
            }
        });
        return false;
    });


    $("body").on("click", "[id^=ajax-modal] form.ajax-submit [type=submit]", function (e) {
        e.preventDefault();
        let $this = $(this),
            $form = $this.parents('form'),
            url = $form.attr('action'),
            data = $form.serialize();

        axios.post(url, data)
            .then(function (response) {
                let data = response.data;
                if (data.status === 1) {
                    $this.parents('[id^=ajax-modal].modal').modal('hide');
                    Fripz.select2();
                }

            })
            .catch(function (error) {

            });

    });

    $("[id^=ajax-modal]").on("hidden.bs.modal", function (e) {
        ajaxModalXhr.abort();
        $("#ajax-modal")
            .find(".modal-dialog")
            .removeClass("modal-lg")
            .removeClass("modal-xs")
            .addClass("modal-sm");

        $("#ajax-modal-content").html("");
    });
});
