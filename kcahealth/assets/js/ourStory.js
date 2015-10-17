

$(document).ready(function() {
  console.log("yep");

$.getJSON( "/getStory.json", function (response) {

  console.log(response);
    document.getElementById("storyBody").innerHTML = "<div>"+response+"</div>";
  });
})