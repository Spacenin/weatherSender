<?php
    //Get details from html file
    $name = $_POST["name"];
    $zipcode = $_POST["zipcode"];
    $number = $_POST["number"];

    //Get JSON contents
    $jsonFile = file_get_contents("data/db.json");
    $jsonFiled = json_decode($jsonFile, false);

    //Setup mysql db connection
    $dbuser = $jsonFiled->user;
    $dbpass = $jsonFiled->pass;
    $dbhost = $jsonFiled->hostname;
    $dbbase = $jsonFiled->db;

    $dbconn = new mysqli($dbhost, $dbuser, $dbpass, $dbbase);

    if ($dbconn->connect_error) {
        die("Connection failed..." . $dbconn->connect_error);
    }

    //Insert new information into database
    else {
        $query = "INSERT INTO numberSet VALUES (" . $zipcode . ", \"" . $name . "\", \"" . $number . "\");";

        if ($dbconn->query($query) == true) {
            echo "Got you!";
        }

        else {
            echo $dbconn->error;
        }
    }
?>