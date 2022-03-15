//-----------------------------------------------------------
// AJAX REST call to server to fetch data for select2 Slaves
//-----------------------------------------------------------
function loadSelectDataSlave(elem) {
    $(".my_select2_ajax_slave").each(function (index) {
        let elem = $(this),
            master_id = elem.attr('master_id'),
            $master = $('#' + master_id),
            master_val = $master.val();

        if (master_val) {
            let endpoint = elem.attr('endpoint');
            endpoint = endpoint.replace("{{ID}}", master_val);
            $.get(endpoint, function (data) {
                elem.select2({data: data, placeholder: "Select", allowClear: true});
            });
        } else {
            elem.select2({data: {id: "", text: ""}, placeholder: "Select", allowClear: true});
        }

        $master.on("change", function (e) {
            let val = $(this).val(),
                endpoint = elem.attr('endpoint');
            if (val) {
                endpoint = endpoint.replace("{{ID}}", val);
                $.get(endpoint, function (data) {
                    elem.select2({data: data, placeholder: "Select", allowClear: true});
                });
            }
        })
    });
}


//----------------------------------------------------
// AJAX REST call to server to fetch data for select2
//----------------------------------------------------
function loadSelectData() {
    $(".my_select2_ajax").each(function (index) {
        let elem = $(this);
        $.get($(this).attr('endpoint'), function (data) {
            elem.select2({data: data, placeholder: "Select", allowClear: true});
        });
    });
}


//---------------------------------------
// Setup date time modal views, select2
//---------------------------------------
// $(function () {
$(window).on('load', function () {

    $('.appbuilder_datetime').datetimepicker({pickTime: false});
    $('.appbuilder_date').datetimepicker({
        pickTime: false
    });
    $(".my_select2").select2({
        placeholder: {
            id: '-1', // the value of the option
            text: 'Select an option'
        }, allowClear: true
    });
    loadSelectData();
    loadSelectDataSlave();
    $(".my_select2.readonly").attr("readonly", "readonly");
    $("a").tooltip({container: '.row', 'placement': 'bottom'});
});


$(".my_change").on("change", function (e) {
    let theForm = document.getElementById("model_form");
    theForm.action = "";
    theForm.method = "get";
    theForm.trigger('submit');
})


//---------------------------------------
// Bootstrap modal, javascript alert
//---------------------------------------
function ab_alert(text) {
    $('#modal-alert').on('show.bs.modal', function (e) {
            $('.modal-text').text(text);
        }
    );
    $('#modal-alert').modal('show');
};


//---------------------------------------
// Modal confirmation JS support
//---------------------------------------

// On link attr "data-text" is set to the modal text
$(function () {
    $(".confirm").on('click', function () {
        $('.modal-text').text($(this).data('text'));
    });
});

// If positive confirmation on model follow link
$('#modal-confirm').on('show.bs.modal', function (e) {
    $(this).find('#modal-confirm-ok').attr('href', $(e.relatedTarget).data('href'));
});

