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

    $("#toggleApproved").click(function () {
        const div = document.querySelector('#approvedCommentsDiv');        
        if(div.classList.contains('d-none')) {
            $("#approvedCommentsDiv").removeClass("d-none").addClass("d-block")
            $(this).addClass("active");
        }
        else {
            $("#approvedCommentsDiv").removeClass("d-block").addClass("d-none")
            $(this).removeClass("active");
        }
    });

    $("#toggleUnapproved").click(function () {
        const div = document.querySelector('#unapprovedCommentsDiv');        
        if(div.classList.contains('d-none')) {
            $("#unapprovedCommentsDiv").removeClass("d-none").addClass("d-block")
            $(this).addClass("active");
        }
        else {
            $("#unapprovedCommentsDiv").removeClass("d-block").addClass("d-none")
            $(this).removeClass("active");
        }
    });



    $("#togglePublished").click(function () {
        const div = document.querySelector('#publishedPostsDiv');        
        if(div.classList.contains('d-none')) {
            $("#publishedPostsDiv").removeClass("d-none").addClass("d-block")
            $(this).addClass("active");
        }
        else {
            $("#publishedPostsDiv").removeClass("d-block").addClass("d-none")
            $(this).removeClass("active");
        }
    });

    $("#toggleUnpublished").click(function () {
        const div = document.querySelector('#unpublishedPostsDiv');        
        if(div.classList.contains('d-none')) {
            $("#unpublishedPostsDiv").removeClass("d-none").addClass("d-block")
            $(this).addClass("active");
        }
        else {
            $("#unpublishedPostsDiv").removeClass("d-block").addClass("d-none")
            $(this).removeClass("active");
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