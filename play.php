<?php
	if ($_POST['cmd']=="play") {
		file_put_contents("/var/www/html/slides.json",$_POST['data']);
		file_put_contents("/run/ledplay","running");
	}
	
	if ($_POST['cmd']=="stop") {
		file_put_contents("/run/ledplay","");
	}	
?>

