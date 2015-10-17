

$(document).ready(function() {
  console.log("yep");

// $.getJSON( "/getExperts.json", function (response) {


//   console.log(response);
//     document.getElementById("storyBody").innerHTML = "<div>"+response+"</div>";
//   });
// })


$.getJSON( "/getExperts.json", function (response) {
		for (var i = 0; i < response.length; i++) {

			expert = response[i][0];
			email = response[i][1];
			document.getElementById("experts").innerHTML+="<div class='expert'><h2>"+expert+": "+email+"</h2></div>";
		}
	});
})