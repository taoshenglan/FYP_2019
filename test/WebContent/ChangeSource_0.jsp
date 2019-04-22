<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>

<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>changecode</title>

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
		<a class="nav-item nav-link" href="Analysis_0.jsp">Analysis</a> 
		<a class="nav-item nav-link" href="ChangeSource_0.jsp">ChangeSource<span class="sr-only">(current)</span></a>
		<a class="nav-item nav-link" href="code_0.jsp">Code</a>
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
			<div class="col-sm-6">
			<h4>If you want to change the source of graph...</h4>
			<h5>Please input the path of your file in the input box, then click submit.</h5>
			</div>
			<div class="col">
			<input id="filepath" type="text" name="path" size="30">
			<input type="button" value="select" onclick="FindPath()">
			
			</div>
		</div>
	</div>
<script type="text/javascript">
	function FindPath(){
		try{
			var path = $("#filepath");
			var Message = "\u8bf7\u9009\u62e9\u6587\u4ef6\u5939";
			var Shell = new ActiveXObject("Shell.Application");
			var Folder = Shell.BrowseForFolder(0, Message,0);
			if(Folder !=null){
				Folder = Folder.items();
				Folder = Folder.item();
				Folder = Folder.Path;
				if(Folder.charAt(Folder.length-1)!=""){
					Folder = Folder+"";
				}
				 $("#filepath").val()=Folder;
				 return Folder;
			}
		}catch(e){
			alert(e.message);
		}
		
	}
</script>
</body>
</html>