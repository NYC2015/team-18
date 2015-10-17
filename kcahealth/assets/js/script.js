




var diameter = 300,
    format = d3.format(",d"),
    color = d3.scale.category20c();

var bubble = d3.layout.pack()
    .sort(null)
    .size([diameter, diameter])
    .padding(1.5);

var svg = d3.select("#statsSVG").append("svg")
    .attr("width", diameter)
    .attr("height", diameter)
    .attr("class", "bubble");


// Returns a flattened hierarchy containing all leaf nodes under the root.
function classes(root) {
  var classes = [];

  function recurse(name, node) {
    if (node.children) node.children.forEach(function(child) { recurse(node.name, child); });
    else classes.push({packageName: name, className: node.name, value: node.size});
  }

  recurse(null, root);
  return {children: classes};
}




$(document).ready(function() {
	// uganda
	// var lat = 0.340617;
	// var lon = 32.584360;
	
	// rwanda
	var lat = -1.964558;
	var lon = 30.104879;
    $.getJSON( "/getPosts.json?lat="+lat+"&lon="+lon, function (response) {
		for (var i = 0; i < response.length; i++) {

			OP = response[i][0];
			body = response[i][1];
			votes = response[i][2];
			comments = response[i][3];
			title = response[i][4];
			// <h2>TITLE OF POST</h2>
			// 			<p>BODY OF POST</p>
			// 			<h4>user</h4>
			document.getElementById("forum").innerHTML+="<div class='postBox'><h2>"+title+"</h2>"+"<h5>"+body+"</h5>"+"<h4>"+OP+"</h4></div>";

			// "<p>OP:"+OP+" body: "+body+"</p>";
		};
	});



d3.json("/bubbleData.json", function(error, root) {
  if (error) throw error;

  var node = svg.selectAll(".node")
      .data(bubble.nodes(classes(root))
      .filter(function(d) { return !d.children; }))
    .enter().append("g")
      .attr("class", "node")
      .attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });

  node.append("title")
      .text(function(d) { return d.className + ": " + format(d.value); });

  node.append("circle")
      .attr("r", function(d) { return d.r; })
      .style("fill", function(d) { return color(d.className); });

  node.append("text")
      .attr("dy", ".2em")
      .style("text-anchor", "middle")
      .style("font-size",function(d){return d.value*10})
      // made it *100, change it back later
      .text(function(d) { return d.className.substring(0, d.r / 3)+":\n"+d.value; });
});

d3.select(self.frameElement).style("height", diameter + "vw");


});


