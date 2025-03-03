<?php
    //include connection file
    include_once("connection.php");

    /* 
    lekér minden adatot a 'log' táblából, debugolásra.
    */

    $sql = "select * from log";
    $result = mysqli_query($conn, $sql);
    $row_ctr = 0;

    if (mysqli_num_rows($result) > 0) {
        // output data of each row
        echo "Struktúra {<br>";
        echo "sorszám;<br> sid;<br> ip;<br> agent;<br> time;<br> events: ha napválasztó gombot nyomnak meg, akkor dátum kerül bele (pl. 11.26.), ha keresés gombot akkor a tantárgy neve. egymás mellé kerülnek ;-vel elválasztva;<br> event_count;<br> session_start;<br> session_end; <br>}<br><br>";
        while ($row = mysqli_fetch_assoc($result)) {
            echo "==================================================================================<br>";
            echo "sorszám: ".$row_ctr."<br>";
            echo "<br>sid: ".$row["sid"]. "<br>ip: " . $row["ip"]. "<br>agent: " . $row["agent"]. "<br>time: " . $row["time"]. "<br>events: " . $row["events"]. "<br>event_count: " . $row["event_count"]. "<br>session_start: " . $row["session_start"]. "<br>session_end: " . $row["session_end"]. "<br><br><br>";
            $row_ctr++;
        };
      } else {
        echo "db error";
      }
?>