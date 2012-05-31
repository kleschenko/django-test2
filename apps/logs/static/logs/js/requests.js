$(document).ready(function() {
    $('.minus').click(function() {
        changePriority($(this).attr('href'), -1);
        return false;
    });
    $('.plus').click(function() {
        changePriority($(this).attr('href'), 1);
        return false;
    });
    $('.sort a').click(function() {
        clearErrors();
        disableInputs();
        var url = $(this).attr('href'),
        ajax_req = $.ajax({
            url: url,
            type: "GET",
            success: function(data, textStatus, jqXHR) {
                var container = $('ul');
                $('li', $(container)).remove();
                $.each(data, function(index, value) {
                    var element = $('<li></li>')
                        .append($('<a></a>')
                            .attr('href', value['url'])
                            .text('['+value['dtime']+']'+' "'+value['method']+' '+value['path']+'"'))
                        .append($('<div></div>')
                            .addClass('priority')
                            .append($('<a></a>')
                                .attr('href', value['url'])
                                .addClass('plus')
                                .text(' + '))
                            .append($('<div></div>')
                                .attr('id', 'req'+value['id'])
                                .text(value['priority']))
                            .append($('<a></a>')
                                .attr('href', value['url'])
                                .addClass('minus')
                                .text(' - '))
                            );
                        $(container).append(element);
                }
                );
                enableInputs();
            },
            error: function(data, textStatus, jqXHR) {
                addErrors(data);
                enableInputs();
            }
        });
        return false;
    });
});

function changePriority(url, rate) {
    clearErrors();
    disableInputs();
    var ajax_req = $.ajax({
        url: url,
        type: "POST",
        data: {'rate': rate},
        success: function(data, textStatus, jqXHR) {
            $('#req'+data['id']).text(data['priority']);
            enableInputs();
        },
        error: function(data, textStatus, jqXHR) {
            addErrors(data.responseText);
            enableInputs();
        }
    });
}

function disableInputs() {
    var container = $("body"),
        placeholder = $("<div></div>").addClass("placeholder");
    container.prepend(placeholder);
    $(placeholder).fadeIn(180);
}

function enableInputs(form) {
    $(".placeholder").fadeOut(180);
}

function addErrors(error) {
    var container = $("ul"),
        errorMsg = $("<div></div>").addClass("error").text(error);
    container.prepend(errorMsg);
}

function clearErrors(form) {
    $(".error", $(form)).remove();
}
