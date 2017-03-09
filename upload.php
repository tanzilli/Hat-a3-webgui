<?php
	// In PHP versions earlier than 4.1.0, $HTTP_POST_FILES should be used instead
	// of $_FILES.
	
	$uploaddir = '/var/www/www_acmesystems_it/tanzilli/gui/';
	$uploadfile = $uploaddir . basename($_FILES['userfile']['name']);
	
	echo '<pre>';
	if (move_uploaded_file($_FILES['userfile']['tmp_name'], $uploadfile)) {
	    echo "File is valid, and was successfully uploaded.\n";
	} else {
	    echo "Possible file upload attack!\n";
	}
	
	echo 'Here is some more debugging info:';
	print_r($_FILES);
	
	print "</pre>";


/*
File is valid, and was successfully uploaded.
Here is some more debugging info:Array
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