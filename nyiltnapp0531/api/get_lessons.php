<?php
	//include connection file 
	include_once("connection.php");

	$sql = "select * from lessons";
	if($_POST['ts']) {
		$sql += "where lastupd > ".$_POST['ts'];
	}

	$result = mysqli_query($conn, $sql); 
	
	if($result = mysqli_query($conn, $sql)){
  
	echo json_encode($result);
?>