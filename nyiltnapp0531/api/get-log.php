<?php
    //include connection file
    include_once("connection.php");

    $sql = "select * from log";
    $res = mysqli_query($conn, $sql);

    echo $res;
?>