<?php
	echo $_POST['cmd'];
	echo " : ";
	echo $_POST['value'];

	file_put_contents("/var/www/html/slides.env",$_POST['value']);
?>

