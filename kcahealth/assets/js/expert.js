

$(document).ready(function() {
  console.log("yep");

// $.getJSON( "/getExperts.json", function (response) {


//   console.log(response);
//     document.getElementById("storyBody").innerHTML = "<div>"+response+"</div>";
//   });
// })


$.getJSON( "/getPosts.json?lat="+lat+"&lon="+lon, function (response) {
		for (var i = 0; i < response.length; i++) {

			expert = response[i][0];
			email = response[i][1];
			// <h2>TITLE OF POST</h2>
			// 			<p>BODY OF POST</p>
			// 			<h4>user</h4>
			document.getElementById("forum").innerHTML+="<div class='postBox'><h2>"+expert+"</h2>"+"<h2>"+email+"</h2>"</div>";

			// "<p>OP:"+OP+" body: "+body+"</p>";
		};
	});