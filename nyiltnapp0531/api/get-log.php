<?php
    //include connection file
    include_once("connection.php");

    $sql = "select * from log";
    $result = mysqli_query($conn, $sql);
    $row_ctr = 0;

    if (mysqli_num_rows($result) > 0) {
        // output data of each row
        echo "Struktúra {<br>";
        echo "sorszám;<br> sid;<br> ip;<br> agent;<br> time;<br> events;<br> event_count;<br> session_start;<br> session_end; <br>}<br><br>";
        while ($row = mysqli_fetch_assoc($result)) {
            echo "==================================================================================<br>";
            echo "sorszám: ".$row_ctr."<br>";
            echo $row["sid"]. "<br>" . $row["ip"]. "<br>" . $row["agent"]. "<br>" . $row["time"]. "<br>" . $row["events"]. "<br>" . $row["event_count"]. "<br>" . $row["session_start"]. "<br>" . $row["session_end"]. "<br><br><br>";
            $row_ctr++;
        };
      } else {
        echo "db error";
      }
?>