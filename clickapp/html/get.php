<?php

require_once dirname(__FILE__) . '/../db.php';

$conn = initDB();
$stmt = $conn->prepare("select x,y from points");
$stmt->execute();

$stmt->bind_result($x, $y);

$results = array();
while($stmt->fetch()) {
    $x = array('x' => $x, 'y' => $y);
    $results[] = $x;
}


header('Content-Type: application/json');
echo json_encode($results);

$stmt->close();
$conn->close();

?>
