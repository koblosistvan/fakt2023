<?php
	//include connection file 
	include_once("connection.php");

	// session
	if(isset($_GET['sid'])) {
		$sid = $_GET["sid"];
		$sql = "update log set session_end = CURRENT_TIMESTAMP() where sid = '{$sid}'";
		$result = mysqli_query($conn, $sql);
	} else {
		$ip = $_SERVER["REMOTE_ADDR"];
		$agent = $_SERVER["HTTP_USER_AGENT"];
		$time = date("Y-m-d H:i:s", time());
		$sid = md5($ip . $agent . $time);
		$sql = "insert into log (sid, ip, agent, time) values ('$sid', '$ip', '$agent', '$time')";
		$result = mysqli_query($conn, $sql);
	};

	$sql = "select * from lessons";
	if($_GET['time']) {
		$sql = $sql." where last_upd > '".urldecode($_GET['time'])."'";
		var_dump($sql);
	};
	$result = mysqli_query($conn, $sql); 

	if(!$result){
		$res = array("status" => "database error");
	} else {
		$rows = array();
		while($r = mysqli_fetch_assoc($result)) {
			$rows[] = $r;
		};

		$sql = "select max(last_upd) as update_time from lessons";
				
		$result = mysqli_query($conn, $sql); 
		$update_time = mysqli_fetch_assoc($result);
		$res = array("status" => "ok", "sid" => $sid, "update_time" => $update_time["update_time"], "lessons" => $rows);
		//var_dump($res);

	};
	//echo $res;
	echo( json_encode($res));
?>