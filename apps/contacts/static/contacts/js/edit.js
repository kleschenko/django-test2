$(document).ready(function() {
    $('.right').each(function() {
        $(this).parent().parent().appendTo($('.contacts'));
    });
});
