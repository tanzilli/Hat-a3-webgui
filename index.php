

<!doctype html>
<html lang="en">
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
	<title>LedPanel admin</title>

	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">
	<script src="https://code.jquery.com/jquery-3.1.1.js"></script>
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
	
	<link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
	<script src="https://cdnjs.cloudflare.com/ajax/libs/tether/1.4.0/js/tether.min.js"></script>
	<script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
	<script src="main.js?random=<? echo uniqid(); ?>"></script>
</head>
<body>
 
<div class="container">
	<div class="row">
		<div class="col">
			<h2>LedPanel admin</h2>

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
						<label>Drop the image file here:</label>
						<br/>
						<input class="form-control btn btn-default"" name="userfile" type="file" />
						
						<!-- <input class="form-control btn btn-primary" type="submit" value="Upload" /> -->
						
					</div>
				</form>
			</div>
		</div>	
	</div>
</div> 


 

</body>
</html>