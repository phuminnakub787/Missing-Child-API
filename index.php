<?php
header('Access-Control-Allow-Origin: *');
header("Content-type: application/json; charset=utf-8");

$data = file_get_contents("miss_child.json");

echo $data;
?>