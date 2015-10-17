



$(document).ready(function() {   
    $.getJSON( "/getPosts.json", function (response) {
		for (var i = 0; i < response.length; i++) {
			OP = response[i][0];
			body = response[i][1];
			document.getElementById("forum").innerHTML+="<p>OP:"+OP+" body: "+body+"</p>";
		};
	});

});