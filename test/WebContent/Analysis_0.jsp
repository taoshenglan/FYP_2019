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
		<a class="nav-item nav-link active" href="index.jsp">Home </a>
		<a class="nav-item nav-link" href="Analysis_0.jsp">Analysis<span
			class="sr-only">(current)</span></a> <a class="nav-item nav-link"
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
			Huang et al. </p>
	</div>
</div>

</head>
<body>
	<div class="container">
		<div class="row">
			<div class="col" id="table1">
				<h4 class="display-4">
					<a href="visual.html">Table1: Analysis of Original Graph</a>
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
					d3.csv('anal_table.csv', function(data) {
						var col = [ 'Item', 'Value' ]
						tabulate(data, col)
					})
				</script>
			</div>
			
		</div>
	</div>

</body>
</html>