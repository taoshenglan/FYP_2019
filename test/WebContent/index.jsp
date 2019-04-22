
<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>

<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
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


<title>Summary of DAG-00</title>
<style>
<!--
style of collapsible tree -->.node {
	cursor: pointer;
}

.node circle {
	fill: #fff;
	stroke: steelblue;
	stroke-width: 0.1px;
}

.node text {
	font: 3px sans-serif;
}

.link {
	fill: none;
	stroke: #ccc;
	stroke-width: 0.5px;
}

.button {
	font-size: 8px;
	height: 14px;
	width: 28px;
	margin: 60px;
}
</style>
<nav class="navbar navbar-expand-lg navbar-light bg-light"> <a
	class="navbar-brand" href="#">Summary of DAG</a>
<button class="navbar-toggler" type="button" data-toggle="collapse"
	data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup"
	aria-expanded="false" aria-label="Toggle navigation">
	<span class="navbar-toggler-icon"></span>
</button>
<div class="collapse navbar-collapse" id="navbarNavAltMarkup">
	<div class="navbar-nav">
		<a class="nav-item nav-link active" href="index.jsp">Home <span class="sr-only">(current)</span></a> 
			<a class="nav-item nav-link" href="Analysis_0.jsp">Analysis</a> 
			
		<a class="nav-item nav-link" href="code.jsp">Code</a>
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

</head>

<body>



	<div class="container">

		<div class="row">
			<div id="Summarization" class="form-inline">

				<p class="font-weight-bold"
					style="font-size: 20px; margin-left: 20px;">Get Start!</p>
				<p style="font-size: 10px; margin-left: 20px">Set the number of
					nodes you want to display:</p>
				<input type="text" name="number" id="userInput"
					style="margin-left: 20px;" /> <input type="button" value="Submit"
					onclick="test()">
				<p style="font-size: 8px; font-color: gray; margin-left: 20px;">(Valid
					Value: 1 to 20000)</p>

			</div>

		</div>

		<div class="row">

			<div id="visualization" style="margin-left: 100px;">
			<iframe width=1000 height=150 scrolling=yes src="visual.html">
				</iframe>
			

			</div>



		</div>

	</div>






	<script>
		function test() {
			var value=$("#userInput").val();
			if(value<1||value>20000){
				alert("Invalid value");
			}else{
				$.ajax({
					url : 'src/HelloServlet',
					dataType : "text",
					data : {
						number : $("#userInput").val()
					},
					type : 'GET',
					success : function(data) {
						alert(data);
						window.location.href = "index_update.jsp";
					}
				});
			}

			
		}
	</script>
</body>
</html>