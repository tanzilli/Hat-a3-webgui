<?php
	if ($_POST['cmd']=="play") {
		file_put_contents("/var/www/html/slides.env",$_POST['value']);
		file_put_contents("/var/www/html/slides.json",$_POST['data']);
	}
	
	if ($_POST['cmd']=="stop") {
		file_put_contents("/var/www/html/slides.env"," ");
	}	
?>

