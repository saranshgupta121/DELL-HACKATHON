<?php
if( count($_GET)==1  &&  isset($_REQUEST['id']) ) 
{
$dd=$_REQUEST['id'];

$con=mysqli_connect("localhost:3306","root","$7dev7&7muj7$"); 
$db=mysqli_select_db($con,"dell's db");

if($con)
{

$a="INSERT INTO db (name)  VALUES ('$dd')";

$result=mysqli_query($con,$a);

}

mysqli_close($con);

}
?>


