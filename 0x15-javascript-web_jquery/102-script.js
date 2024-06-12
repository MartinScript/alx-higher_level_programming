$(document).ready(function () {
    $('#btn_translate').click(function () {
        var languageCode = $('#language_code').val();
        var url = 'https://www.fourtonfish.com/hellosalut/?lang=' + languageCode + '&callback=?';

        $.ajax({
            url: url,
            dataType: 'jsonp',
            success: function (data) {
                $('#hello').text(data.hello);
            },
            error: function () {
                $('#hello').text('Error fetching translation');
            }
        });
    });
});
