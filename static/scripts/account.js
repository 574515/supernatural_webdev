$(document).ready(function() {

    $(".form-control").prop("readonly", true);
    $("#saveChanges").prop("disabled", true);

    $("#editProfile").click(function() {
        if($(this).html() == "Edit profile") {
            $(".form-control").prop("readonly", false);
            $("#saveChanges").prop("disabled", false);
            $("#fname").focus();
            if($(this).html() == "Edit profile") $(this).html("Cancel");
        }
        else {
            $(".form-control").prop("readonly", true);
            $("#saveChanges").prop("disabled", true);
            if($(this).html() == "Cancel") $(this).html("Edit profile");
        }
    });

    $("#togglePosts").click(function () {
        const div = document.querySelector('#accPostsDiv');        
        if(div.classList.contains('d-none')) {
            $("#accPostsDiv").removeClass("d-none").addClass("d-block")
            $(this).addClass("active");
        }
        else {
            $("#accPostsDiv").removeClass("d-block").addClass("d-none")
            $(this).removeClass("active");
        }
    });

    $("#toggleComments").click(function () {
        const div = document.querySelector('#accCommsDiv');        
        if(div.classList.contains('d-none')) {
            $("#accCommsDiv").removeClass("d-none").addClass("d-block")
            $(this).addClass("active");
        }
        else {
            $("#accCommsDiv").removeClass("d-block").addClass("d-none")
            $(this).removeClass("active");
        }
    });
});