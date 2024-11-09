<?php
	//include connection file 
	include_once("connection.php");

	var_dump($_POST);
 	$sid = $_POST["sid"];
	if(isset($_POST["day"])) {
		$day = $_POST["day"];
		$sql = "update log set events = concat(events, '{$day}', ';'), event_count = event_count + 1, session_end = CURRENT_TIMESTAMP() where sid = '{$sid}'";
		echo $sql;
	} else if(isset($_POST["subject"])) {
		$subject = $_POST["subject"];
		$sql = "update log set events = concat(events, '{$subject}', ';'), event_count = event_count + 1, session_end = CURRENT_TIMESTAMP() where sid = '{$sid}'";
	}
	$result = mysqli_query($conn, $sql);
 ?>