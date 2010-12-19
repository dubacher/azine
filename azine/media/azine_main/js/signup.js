$(document).ready(function() {
    // If this is not the signup page:
    if ($('#signupForm').length == 0) {
        
        return;
            
        var loadContent = function(data) {
            $('#signUpDialog').html($(data).find('#content-main'));
        };

        var postSignup = function() {
            //$.post("signup/", $("#signupForm").serialize(), loadContent);
            $('#signupForm').submit();
        };

        var $dialog = $('<div id="signUpDialog"></div>')
            .dialog({
                autoOpen: false,
                title: 'Sign Up',
                buttons: { "Signup": postSignup }
            });

        $('#signup').click(function(event) {
            event.preventDefault()
            $dialog.dialog('open');
        });
    
        $.get($('#signup').attr('href'), loadContent);
    }
});
