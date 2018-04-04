<?php
	if ($_POST['cmd']=="save") {
		$written_bytes=file_put_contents("/var/www/html/slides.json",$_POST['data']);
		if ($written_bytes===FALSE) {
			die("Save error. Check the /var/www/html/slides.json access by www-data user");
		} else {
			die("File saved ($written_bytes bytes)");
		}
	}

	if ($_POST['cmd']=="play") { 
		$written_bytes=file_put_contents("/run/ledplay","play");
		if ($written_bytes===FALSE) {
			die("Save error. Check the /run/ledplay access by www-data user");
		} else {
			die("Success ! Saved \"play\" in /run/ledplay");
		}
	}
	
	if ($_POST['cmd']=="stop") {
		$written_bytes=file_put_contents("/run/ledplay","stop");
		if ($written_bytes===FALSE) {
			die("Save error. Check the /run/ledplay access by www-data user");
		} else {
			die("Success ! Saved \"stop\" in /run/ledplay");
		}
	}	
?>

