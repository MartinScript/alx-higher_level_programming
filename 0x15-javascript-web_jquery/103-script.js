$(document).ready(function () {
    function fetchTranslation() {
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
    }

    // Event listener for button click
    $('#btn_translate').click(fetchTranslation);

    // Event listener for pressing Enter key
    $('#language_code').keypress(function (event) {
        if (event.which == 13) { // Enter key code is 13
            fetchTranslation();
        }
    });
});

