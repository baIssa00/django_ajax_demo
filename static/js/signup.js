$(document).ready(function() {
    $('#btn-connect').click(function (event) {
        event.preventDefault();
        var email = $('#email').val()
        var password = $('#password').val()
        $.ajax({
            // data: $(this).serialize(),
            data: {email:email, password:password},
            type: $(this).attr('method'),
            url: $(this).attr('action'),
            success: function () {
                $('#message').html("<p>email : " + $("#email").val() + " & Password : " + $("#password").val() + "</p>");
            },
            error: function (error) {
                alert(error);
                 }
        }); 
    });

});