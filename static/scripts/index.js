$(document).ready(function () {

    let numOfClicks = 1, title = "SUPERNATURAL";

    $("#snlogo span").html(title);

    $(".navbar").click(function () {
        $('#snlogo span').html(title);
    });

    $("#snlogo").click(function () {
        var shuffled = title.split('').sort(function () { return 0.5 - Math.random() }).join('');
        numOfClicks++ % 5 == 0 ? getRandomPhrase(false, shuffled) : getRandomPhrase(true, shuffled);
    });

    function getRandomPhrase(isShuffeled, shuffeledArr) {
        if (isShuffeled) {
            newTitle = shuffeledArr;
            $('#snlogo span').html(newTitle);
            $('#snlogo').css("background-color", "rgba(0, 0, 0, 0.3)");
        } else {
            jQuery.get('/static/assets/phrases.txt', function (data) {
                phrases = data.split("\n");
                $('#snlogo span').html(String(phrases[Math.floor(Math.random() * phrases.length)]));
                $('#snlogo').css("background-color", "rgba(0, 0, 0, 0.5)");
            });
        }
    }
});
