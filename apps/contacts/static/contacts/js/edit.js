$(document).ready(function() {
    $('.right').each(function() {
        $(this).parent().parent().appendTo($('.contacts'));
    });
});

function apply_form_field_error(fieldname, error) {
    var container = $("#div_id_" + fieldname),
        error_msg = $("<div></div>").addClass("error").text(error[0]);
    container.prepend(error_msg);
}

function clear_form_field_errors(form) {
    $(".error", $(form)).remove();
}

function disable_inputs(form) {
    $(":input", $(form)).attr('disabled', true);
}

function enable_inputs(form) {
    $(":input", $(form)).removeAttr('disabled');
}

$(document).on("submit", "#edit_form", function(e) {
    e.preventDefault();
    clear_form_field_errors($(this));
    $("#sendwrapper").append($("<span></span>")
            .attr('id', 'sendstatus')
            .addClass('in_process')
            .text("Sending data, please wait"));
    var self = $(this),
        url = self.attr('action'),
        formData = new FormData(self[0]),
        ajax_req = $.ajax({
            url: url,
            type: "POST",
            data: formData,
            processData: false,
            contentType: false,
            success: function(data, textStatus, jqXHR) {
                $("#sendstatus").addClass('success').text("Successfully saved");
                enable_inputs(self);
            },
            error: function(data, textStatus, jqXHR) {
                var errors = $.parseJSON(data.responseText);
                $.each(errors, function(index, value) {
                    if (index === "__all__") {
                        alert('error');
                    } else {
                        apply_form_field_error(index, value);
                    }
                });
                $("#sendstatus").remove();
                enable_inputs(self);
            }
        });
    disable_inputs($(this));
});
