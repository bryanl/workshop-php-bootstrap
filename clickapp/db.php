<?php

function initDB() {
    $ini = parse_ini_file("db.ini");
    $conn = new mysqli($ini["server"], $ini["username"], $ini["password"], $ini["dbname"]);
    return $conn;
}



?>
