let numOfClicks = 1, title = "SUPERNATURAL";

$("body").click(function() {
    let shuffled = title.split('').sort(function(){return 0.5-Math.random()}).join('');
    
    $(".navbar").click(function() { getRandomPhrase(false, true, shuffled); });
    
    numOfClicks++ % 5 == 0 ? getRandomPhrase(false, false, shuffled) : getRandomPhrase(true, false, shuffled);
});

function getRandomPhrase(isShuffeled, isReset, shuffeledArr) {
    if (!isShuffeled && !isReset) newTitle = randomPhrasePicker();
    else if(isShuffeled && !isReset) newTitle = shuffeledArr;
    else newTitle = title;
    $('#s_top').html("<span class='col-md-1' id='s_top'><h1 class='glow'>" + newTitle[0] + "</h1></span>");
    $('#u1_top').html("<span class='col-md-1' id='u1_top'><h1 class='glow'>" + newTitle[1] + "</h1></span>");
    $('#p_top').html("<span class='col-md-1' id='p_top'><h1 class='glow'>" + newTitle[2] + "</h1></span>");
    $('#e_top').html("<span class='col-md-1' id='e_top'><h1 class='glow'>" + newTitle[3] + "</h1></span>");
    $('#r1_top').html("<span class='col-md-1' id='r1_top'><h1 class='glow'>" + newTitle[4] + "</h1></span>");
    $('#n_top').html("<span class='col-md-1' id='n_top'><h1 class='glow'>" + newTitle[5] + "</h1></span>");
    $('#a1_top').html("<span class='col-md-1' id='a1_top'><h1 class='glow'>" + newTitle[6] + "</h1></span>");
    $('#t_top').html("<span class='col-md-1' id='t_top'><h1 class='glow'>" + newTitle[7] + "</h1></span>");
    $('#u2_top').html("<span class='col-md-1' id='u2_top'><h1 class='glow'>" + newTitle[8] + "</h1></span>");
    $('#r2_top').html("<span class='col-md-1' id='r2_top'><h1 class='glow'>" + newTitle[9] + "</h1></span>");
    $('#a2_top').html("<span class='col-md-1' id='a2_top'><h1 class='glow'>" + newTitle[10] + "</h1></span>");
    $('#l_top').html("<span class='col-md-1' id='l_top'><h1 class='glow'>" + newTitle[11] + "</h1></span>");
}

function randomPhrasePicker() {
    const phrases = [
        "THISISENOUGH", "HELPMEPLEASE", "HELLOLUCIFER", "IWASDARKNESS", "MYNAMEISJACK", 
        "DEANISEATING", "NEPHILIMHERE"];
    return phrases[Math.floor(Math.random() * 7)];
}