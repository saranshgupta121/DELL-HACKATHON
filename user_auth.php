<?php
if( count($_GET)==2  &&  isset($_REQUEST['id1'])  &&  isset($_REQUEST['id2'])) 
{
$dd1=$_REQUEST['id1'];
$dd2=$_REQUEST['id2'];
$con=mysqli_connect("localhost:3306","root","$7dev7&7muj7$"); 
$db=mysqli_select_db($con,"dell's db");

if($con)
{
$heroes = array(); 
$a="select * from info_officials ";
$result=mysqli_query($con,$a);
while($row=mysqli_fetch_array($result))
{
    if($row[1]==$dd1 && $row[2]==$dd2)
    {
$temp = ['id'=>$row[0]];
	array_push($heroes, $temp);
	break;
    }
}

echo json_encode($heroes);

}

mysqli_close($con);

}
?>


