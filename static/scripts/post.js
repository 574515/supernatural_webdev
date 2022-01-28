$(document).ready(function () {
    $("#togglePostComments").click(function () {
        const div = document.querySelector("#postComments");
        if (div.classList.contains("d-none")) {
            $("#postComments").removeClass("d-none").addClass("d-block");
            $(this).addClass("active");
            $("#togglePostComments").html("Hide Comments");
        } else {
            $("#postComments").removeClass("d-block").addClass("d-none");
            $(this).removeClass("active");
            $("#togglePostComments").html("Show Comments");
        }
    });
});
