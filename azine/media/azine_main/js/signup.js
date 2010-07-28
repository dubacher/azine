$(document).ready(function() {
    var loadContent = function(data) {
        $('#signUpDialog').html(data);
    };
    var postSignup = function() {
        $.post("signup/", $("#signupForm").serialize(), loadContent);
    };

    var $dialog = $('<div id="signUpDialog"></div>')
        .dialog({
            autoOpen: false,
            title: 'Sign Up',
            buttons: { "Signup": postSignup }
        });

    $('#signup').click(function() {
        $dialog.dialog('open');
        // prevent the default action, e.g., following a link
        return false;
    });
    $.get('signup/', loadContent);

});
