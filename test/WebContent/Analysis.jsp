<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>

<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Anal</title>

<link rel="stylesheet"
	href="http://cdn.static.runoob.com/libs/bootstrap/3.3.7/css/bootstrap.min.css">
<script
	src="http://cdn.static.runoob.com/libs/jquery/2.1.1/jquery.min.js"></script>
  
<script
	src="http://cdn.static.runoob.com/libs/bootstrap/3.3.7/js/bootstrap.min.js"></script>

<script type="text/javascript" src="http://d3js.org/d3.v3.min.js"></script>
<script src="d3.v4.js"></script>
<script type="text/javascript" src="jquery-3.3.1.min.js"></script>
<script src="d3.layout.cloud.js" type="text/javascript"></script>

<nav class="navbar navbar-expand-lg navbar-light bg-light"> <a
	class="navbar-brand" href="index_update.jsp">Summary of DAG</a>
<button class="navbar-toggler" type="button" data-toggle="collapse"
	data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup"
	aria-expanded="false" aria-label="Toggle navigation">
	<span class="navbar-toggler-icon"></span>
</button>
<div class="collapse navbar-collapse" id="navbarNavAltMarkup">
	<div class="navbar-nav">
		<a class="nav-item nav-link active" href="index_update.jsp">Home </a>
		<a class="nav-item nav-link" href="Analysis.jsp">Analysis<span
			class="sr-only">(current)</span></a>  <a class="nav-item nav-link"
			href="code.jsp">Code</a>
	</div>
</div>
</nav>
<div class="jumbotron jumbotron-fluid" style="background-color: #ccddff">
	<div class="container">
		<h1 class="display-4">Summary of DAG</h1>
		<p style="font-size: 10px;">The FYP for Shenglan TAO in 2018-2019
			at HKBU. The work is to show the efficacy of kVDO method in doing
			Big-Data Visualization, a unique way of data summarization. The work
			is greatly based on by a theory published on the short paper
			Ontology-based Graph Visualization for Summarized View by Dr. Xin
			Huang et al.</p>
	</div>
</div>
<style type="text/css">
path {
	stroke: blue;
	stroke-width: 2;
	fill: none;
}

.axis path, .axis line {
	fill: none;
	stroke: grey;
	stroke-width: 1;
	shape-rendering: crispEdges;
}

.stroke_width {
	stroke-width: 0.3vmin;
}

.linecircle {
	fill: #2E8B57;
	stroke: #2E8B57;
	stroke-width: 0.3;
}

.gridline {
	stroke: #cc;
}

.tips {
	pointer-events: none;
	display: none;
}

.tips-border {
	fill: #F3E4E4;
	stroke: gray;
	stroke-width: 2;
}
</style>


</head>
<body onload=loadFile();>

	<script type="text/javascript">
function loadFile(){
	$.ajax({
		url:'src/UpdateServlet',
		dataType : "text",
		type:'GET',
		data : {
			fname : "ScoreResult.csv"
		},
		success:function(data){
			//alert(data);
			loadGraph(data);
		}
			
	})
} 
</script>
	<div class="container">
		<div class="row">
			<div class="col-sm-6" id="table1">
				<h4 class="display-4">
					<a href="#">Table1: Analysis of Original Graph</a>
				</h4>
				<script type="text/javascript">
					var tabulate = function(data, col) {
						var table = d3.select('#table1').append('table');
						var thead = table.append('thead');
						var tbody = table.append('tbody');
						table
								.attr('class',
										'table table-striped table-hover table-bordered')

						thead.append('tr').selectAll('th').data(col).enter()
								.append('th').text(function(d) {
									return d
								});
						var rows = tbody.selectAll('tr').data(data).enter()
								.append('tr');
						var cells = rows.selectAll('td').data(function(row) {
							return col.map(function(cl) {
								return {
									cl : cl,
									value : row[cl]
								}
							})
						}).enter().append('td').text(function(d) {
							return d.value
						});

						return table;

					}
					d3.csv('anal_table_Japan.csv', function(data) {
						var col = [ 'Item', 'Value' ]
						tabulate(data, col)
					})
				</script>
			</div>
			<div class="col-sm-6" id="table_update">
				<h4 class="display-4">
					<a href="visual-summarized.html">Table2: Performance of
						Summarization</a>
				</h4>


				<div id="linergraph">
					<script>
					var margin = {
						top : 30,
						right : 20,
						bottom : 30,
						left : 50
					}, width = 600 - margin.left - margin.right, height = 270
							- margin.top - margin.bottom;

					// Adds the svg canvas
					var svg = d3.select("#linergraph").append("svg").attr(
							"width", width + margin.left + margin.right).attr(
							"height", height + margin.top + margin.bottom)
							.append("g").attr(
									"transform",
									"translate(" + margin.left + ","
											+ margin.top + ")");

					// Get the data
					var dataset = [];
					var x_value = new Array();
					var y_value = new Array();
					d3.csv("http://localhost:8080/test/src/UpdateServlet?fname=ScoreResult.csv", function(error, data) {
						data.forEach(function(d) {
							
							var i = parseInt(d.Item);
							var k = parseInt(d.Value);
							dataset.push({
								num : i,
								value : k
							});
							x_value.push(i);
							y_value.push(k);
							
						});
						
						//alert(x_value);
						//alert(dataset[0].num);
						// Scale the range of the data
						// Set the ranges
						var x = d3.scale.linear().range([ 0, width ]);
						var y = d3.scale.linear().range([ height, 0 ]);
						//alert(d3.min(x_value,function(d){return d;}));
						//alert(d3.max(x_value,function(d){return d;}));
						
						x.domain([d3.min(x_value,function(d){return d;})-1,d3.max(x_value, function(d) {
							
							return d;
						})*1.1]);
						
						y.domain([ 0, d3.max(y_value, function(d) {
							return d;
						})*1.1 ]);
						
						var xAxis = d3.svg.axis().scale(x).orient('bottom').ticks(5);
						var yAxis = d3.svg.axis().scale(y).orient('left').ticks(5);
						
						
						// Add the X Axis
						svg.append("g").attr("class", "x axis").attr(
								"transform", "translate(0," + height + ")")
								.call(xAxis)
								.append("text")
								.text("Number of node")
								.attr("transform","translate("+width+",0)");
						

						// Add the Y Axis
						svg.append("g").attr("class", "y axis")
						.call(yAxis)
						.append("text")
						.text("Score");
						
						var line = d3.svg.line()
						.x(function(d){return x(d.num);})
						.y(function(d){return y(d.value);})
						.interpolate("linear");
						
						var path = svg.append('path')
						.attr('class','line')
						.attr('d',line(dataset));
						
						
						var g = svg.selectAll('circle')
						  .data(dataset)
						  .enter()
						  .append('g')
						  .append('circle')
						  .attr('class', 'linecircle')
						  .attr('cx', line.x())
						  .attr('cy', line.y())
						  .attr('r', 3.5)
						  .on('mouseover', function() {
						    d3.select(this).transition().duration(500).attr('r', 5);
						  })
						  .on('mouseout', function() {
						    d3.select(this).transition().duration(500).attr('r', 3.5);
						  });
						
						var tips = svg.append('g').attr('class', 'tips');
						 
						tips.append('rect')
						  .attr('class', 'tips-border')
						  .attr('width', 220)
						  .attr('height', 50)
						  .attr('rx', 10)
						  .attr('ry', 10);
						 
						var wording1 = tips.append('text')
						  .attr('class', 'tips-text')
						  .attr('x', 10)
						  .attr('y', 20)
						  .text('');
						 
						var wording2 = tips.append('text')
						  .attr('class', 'tips-text')
						  .attr('x', 10)
						  .attr('y', 40)
						  .text('');

						
						
						d3.select("#linergraph")
						  .on('mousemove', function() {
						    var m = d3.mouse(this),
						      cx = m[0] - margin.left;
						 
						    var x0 = x.invert(cx);
						    var i = (d3.bisector(function(d) {
						      return d.num;
						    }).left)(dataset, x0, 1);
						 
						    var d0 = dataset[i - 1],
						      d1 = dataset[i] || {},
						      d = x0 - d0.num > d1.num - x0 ? d1 : d0;
						 
						    function formatWording(d) {
						      return 'number of node in result set:' + d.num;
						    }
						    wording1.text(formatWording(d));
						    wording2.text('Score:' + d.value);
						 
						    var x1 = x(d.num),
						      y1 = y(d.value);
						 
						    
						    var dx = x1 > width ? x1 - width + 200 : x1 + 200 > width ? 200 : 0;
						 
						    var dy = y1 > height ? y1 - height + 50 : y1 + 50 > height ? 50 : 0;
						 
						    x1 -= dx;
						    y1 -= dy;
						 
						    d3.select('.tips')
						      .attr('transform', 'translate(' + x1 + ',' + y1 + ')');
						 
						    d3.select('.tips').style('display', 'block');
						  })
						  .on('mouseout', function() {
						    d3.select('.tips').style('display', 'none');
						  });
					});
				</script>
				</div>
				<div id="table2">
					<script type="text/javascript">
					var tabulate2 = function(data,Items, Values,col) {
						var table = d3.select('#table2').append('table');
						var thead = table.append('thead');
						var tbody = table.append('tbody');
						table
								.attr('class',
										'table table-striped table-hover table-bordered')

						thead.append('tr').selectAll('th').data(col).enter()
								.append('th').text(function(d) {
									return d
								});
						var rows = tbody.selectAll('tr').data(data).enter()
								.append('tr');
						var cells = rows.selectAll('td').data(function(row){
							var temp=row.split(",");
							return col.map(function(cl,i) {
								//alert(temp[i])
								
								return {
									cl : cl,
									value : temp[i]
								}
							})
							
						
						}).enter().append('td').text(function(d){return d.value});
						

						return table;

					};
					function loadGraph(data){
						//alert(data)
						var itemlist = data.split("\n");
						var Items=[];
						var Values=[];
						var rela=[];
						for(var i =0; i<itemlist.length;i++){
							if(i==0){
								continue;
							}
							var tmp = itemlist[i].split(",");
							if(tmp[0]!=null && tmp[1]!=null){
								Items.push(tmp[0]);
								Values.push(tmp[1]);
								rela.push(itemlist[i]);
							}
						
						}
						
						//alert(Items)
						var col = [ 'Item', 'Value' ];
						tabulate2(rela,Items, Values,col);
					}
					
					
				</script>
				</div>
			</div>

		</div>
	</div>

</body>
</html>