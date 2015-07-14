<?php
$server = "localhost";
$username = "root";
$password = "apbw3N7elB";
$dbname = "myapp";
#$server = $_ENV["MYSQL_HOST"];
#$user = $_ENV["MYSQL_USER"];
#$dname = $_ENV["MYSQL_DB"];
#$password = $_ENV["MYSQL_PASS"];

$conn = new mysqli($server, $username, $password, $dbname);
$stmt = $conn->prepare("insert into points (x, y) values(?, ?)");
$stmt->bind_param('dd', $_POST["x"], $_POST["y"]);
$stmt->execute();

$stmt->close();
$conn->close();
?>
