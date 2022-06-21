$(document).ready(function () {
    $('#formSubmit').on('submit', function(e) {
        e.preventDefault();
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        $.ajax({
            type: $(this).attr('method'), // GET or POST
            url: $(this).attr('action'),
            data: {
                login: $('#login').val(),
                headers: {'X-CSRFToken': csrftoken},
                password: $('#password').val(),
                csrfmiddlewaretoken: '{{ csrf_token }}',
                dataType: 'json',
            },
            success: function(data) {
                $('#message').html(data)
            }
        })
    })
})