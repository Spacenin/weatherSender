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

        //Go to landing page if entered correctly
        if ($dbconn->query($query) == true) {   
            header("Location: landing.html");
            die();
        }

        //Otherwise print out error
        else {
            echo "
            <!DOCTYPE html>
            <html lang=\"en\">
                <head>
                    <meta charset=\"UTF-8\">
                    <title>Uh oh....</title>
                    <link rel=\"stylesheet\" href=\"style.css\">
                    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
                </head>
                <body style=\"background-color: #22223B;\">
                    <div id=\"landingPage\">
                        <p>
                            Error! This is what has happened:<br>
                            " . $dbconn->error . "
                        </p>
                    </div>
                </body>
            </html>";
        }
    }
?>