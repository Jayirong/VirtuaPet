<?php
    $DBServer ='localhost';
    $DBUser ='root';
    $DBPass ='';
    $DBName ='virtuapet2';

    $conn = new mysqli($DBServer, $DBUser, $DBPass, $DBName);
    if($conn->connect_error){
        echo $conn-> connect_error;
    }
       
?>