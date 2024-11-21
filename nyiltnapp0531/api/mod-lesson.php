<?php
	//include connection file 
	include_once("connection.php");

	var_dump($_POST);
	if(isset($_POST["id"])) {
		$id = $_POST["id"];
		$valid = $_POST["valid"];
		$sql = "update lesson set valid = {$valid} where id = {$id}";
		$result = mysqli_query($conn, $sql);
	}
