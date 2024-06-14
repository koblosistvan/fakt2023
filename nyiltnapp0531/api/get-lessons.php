<?php
	//include connection file 
	include_once("connection.php");

	$sql = "select * from lessons";
	if($_POST['time']) {
		$sql += "where last_upd > ".$_POST['ts'];
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
		if($_POST['time']) {
			$sql += "where last_upd > ".$_POST['ts'];
		}
		var_dump($sql);
		$result = mysqli_query($conn, $sql); 
		$update_time = mysqli_fetch_assoc($result);
		$res = array("status" => "ok", "update_time" => $update_time["update_time"], "lessons" => $rows);
	}
	echo json_encode($res);
?>