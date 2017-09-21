

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
			<h2>Insegna NetHome - Pannello di controllo</h2>

			<button type='button' id="play" class='btn btn-success'><span class='glyphicon glyphicon-play' aria-hidden='true'></span> Save & Play</button>
			<button type='button' id="stop" class='btn btn-warning'><span class='glyphicon glyphicon-stop' aria-hidden='true'></span> Stop</button>
			<br/>
			<br/>
		</div>	
	</div>

	<div class="row">
		<div class="col">
			<div id="sortable">
			</div>
		</div>	
	</div>
	
	
	<div class="row">
		<div class="col">
			<div class="alert alert-info">
				<!-- The data encoding type, enctype, MUST be specified as below -->
				<form  id="upload_form" class="form-inline" enctype="multipart/form-data" action="upload.php" method="POST">
				    <div class="form-group">
	
						<!-- MAX_FILE_SIZE must precede the file input field -->
						<input type="hidden" name="MAX_FILE_SIZE" value="2000000" />
						<!-- Name of input element determines name in $_FILES array -->
						<label>Drop the image file here to add a new slide:</label>
						<br/>
						<input class="form-control btn btn-default"" name="userfile" type="file" />
						
						<!-- <input class="form-control btn btn-primary" type="submit" value="Upload" /> -->
						
					</div>
				</form>
			</div>
		</div>	
	</div>

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
			<h2>Come preparare nuove slides</h2>
			
			<p>
				Le nuove slides devono essere dei file grafici in formato gif, jpg o png con un rapporto tra larghezza ed altezza di 3:6. 
				<br/>
				La risoluzione minima deve essere di 96x192 pixel.
			</p>
			<p>
				E' possible preparare nuove immagini usano i seguenti editor on-line:
			</p>

			<ul>
				<li><a href="https://www.aviary.com" target="_blank">https://www.aviary.com</a></li>
			</ul>	
		</div>	
	</div>

</div> 


 

</body>
</html>