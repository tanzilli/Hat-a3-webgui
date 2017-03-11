<?php
	echo $_POST['cmd'];
	echo " "; 
	echo $_POST['value']; 
	
	file_put_contents("/dev/shm/slides.env",$_POST['value']);
?>

