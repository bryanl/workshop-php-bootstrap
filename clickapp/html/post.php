<?php

require_once dirname(__FILE__) . '/../db.php';

$conn = initDB();

$conn = new mysqli($server, $username, $password, $dbname);
$stmt = $conn->prepare("insert into points (x, y) values(?, ?)");
$stmt->bind_param('dd', $_POST["x"], $_POST["y"]);
$stmt->execute();

$stmt->close();
$conn->close();
?>
