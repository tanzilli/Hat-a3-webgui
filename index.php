

<!doctype html>
<html lang="en">
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
	<title>LedPanel admin</title>

	<link rel="stylesheet" href="bootstrap/css/bootstrap.min.css">
	<link rel="stylesheet" href="bootstrap/css/bootstrap-theme.min.css">
	
	<script src="jquery/jquery-3.1.1.min.js"></script>
	<script src="bootstrap/js/bootstrap.min.js"></script>
	
	<link rel="stylesheet" href="jquery-ui/jquery-ui.css">
	
	<!--<script src="https://cdnjs.cloudflare.com/ajax/libs/tether/1.4.0/js/tether.min.js"></script>-->
	<script src="jquery-ui/jquery-ui.js"></script>
	<script src="main.js"></script>
</head>
<body>
 
<div class="container">
	<div class="row">
		<div class="col">
			<h2>RGB led panel web GUI</h2>

			<button type='button' id="save" class='btn btn-primary'><span class='glyphicon glyphicon-save' aria-hidden='true'></span> Save</button>
			<button type='button' id="play" class='btn btn-success'><span class='glyphicon glyphicon-play' aria-hidden='true'></span> Play</button>
			<button type='button' id="stop" class='btn btn-warning'><span class='glyphicon glyphicon-stop' aria-hidden='true'></span> Stop</button>
			<button type='button' id="add_ptime" class='btn btn-default'><span class='glyphicon glyphicon-time' aria-hidden='true'></span> Add time</button>
			<button type='button' id="add_pweather" class='btn btn-default'><span class='glyphicon glyphicon-cloud' aria-hidden='true'></span> Add weather</button>
			<br/>
			<br/>
		</div>	
	</div>

	<!----------------->
	<!-- palimpsest  -->
	<!----------------->

	<div class="row">
		<div class="col">
			<div id="sortable">
			</div>
		</div>	
	</div>
	
	<!----------------->
	<!-- File upload -->
	<!----------------->
	
	<div class="row">
		<div class="col">
			<div class="alert alert-info">
				<!-- The data encoding type, enctype, MUST be specified as below -->
				<form  id="upload_form" class="form-inline" enctype="multipart/form-data" action="upload.php" method="POST">
				    <div class="form-group">
	
						<!-- MAX_FILE_SIZE must precede the file input field -->
						<input type="hidden" name="MAX_FILE_SIZE" value="200000000" />
						<!-- Name of input element determines name in $_FILES array -->
						<label>Drop here the file to add to the palimpsest (gif jpg png m4v mp4):</label>
						<br/>
						<input class="form-control btn btn-default"" name="userfile" type="file" />
						
						<!-- <input class="form-control btn btn-primary" type="submit" value="Upload" /> -->
						
					</div>
				</form>
			</div>
		</div>	
	</div>

	<!----------------->
	<!-- Messages    -->
	<!----------------->

	<div class="row">
		<div class="col">
			<div class="alert alert-warning">
				<pre id="warning">
				</pre>
			</div>
		</div>	
	</div>

	<div class="row">
		<div class="col">
			<p>
				Sergio Tanzilli &copy; 2018 - <a href="https://github.com/tanzilli/Hat-a3-webgui" target="_blank">Fork me on GitHub</a></li>
			</p>
		</div>	
	</div>

</div> 


 

</body>
</html>