<?php
	//include connection file 
	include_once("connection.php");

	$sql = "select * from lessons";
	if($_GET['time']) {
		$sql = $sql." where last_upd > ".$_GET['time'];
	}
	$result = mysqli_query($conn, $sql); 

	if(!$result){
		$res = array("status" => "database error");
	} else {
		$rows = array();
		while($r = mysqli_fetch_assoc($result)) {
			$rows[] = $r;
		};

		$sql = "select max(last_upd) as update_time from lessons";
		if($_GET['time']) {
			$sql = $sql."where last_upd > ".$_GET['time'];
		}
		
		$result = mysqli_query($conn, $sql); 
		$update_time = mysqli_fetch_assoc($result);
		$res = array("status" => "ok", "update_time" => $update_time["update_time"], "lessons" => $rows);
	}
	echo json_encode($res);
?>