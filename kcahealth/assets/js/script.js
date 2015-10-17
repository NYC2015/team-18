



$(document).ready(function() {   
    $.getJSON( "/getPosts.json", function (response) {
		for (var i = 0; i < response.length; i++) {

			OP = response[i][0];
			body = response[i][1];
			votes = response[i][2];
			title = response[i][3];
			// <h2>TITLE OF POST</h2>
			// 			<p>BODY OF POST</p>
			// 			<h4>user</h4>
			document.getElementById("forum").innerHTML+="<h2>"+title+"</h2>"+"<p>"+body+"</p>"+"<h4>"+OP+"</h4>"+"<h5>"+votes+"</h5>";

			// "<p>OP:"+OP+" body: "+body+"</p>";
		};
	});

});

