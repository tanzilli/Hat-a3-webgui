<?php
	// In PHP versions earlier than 4.1.0, $HTTP_POST_FILES should be used instead
	// of $_FILES.

	$uploaddir = '/var/www/html/slides/';
	$uploadfile = $uploaddir . basename($_FILES['userfile']['name']);

	if (move_uploaded_file($_FILES['userfile']['tmp_name'], $uploadfile)) {
		printf(basename($uploadfile) . "," . $_FILES['userfile']['type']);
	} else {
		printf("error");
	}

	/*
	print_r($_FILES);

	Array
	(
		[userfile] => Array
			(
				[name] => nome.gif
				[type] => image/gif
				[tmp_name] => /tmp/phpPhtW4q
				[error] => 0
				[size] => 92381
			)

	)
	*/
?>