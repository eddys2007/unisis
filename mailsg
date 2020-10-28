<?php


$subject = $_POST['subject'];
$to = $_POST['to'];
//$to_name = $_POST['to_name'];
$text = $_POST['text'];

$to_name = "-";

include "classes/class.phpmailer.php";
$mail = new PHPMailer;
$mail->IsSMTP();
$mail->SMTPSecure = 'ssl';
$mail->Host = "smtp.gmail.com"; //hostname masing-masing provider email
$mail->SMTPDebug = 2;
$mail->Port = 465;
$mail->SMTPAuth = true;
$mail->Username = "mymail@gmail.com"; //user email
$mail->Password = "passoword"; //password email
$mail->SetFrom("mymail@gmail.com","Company: ");

//set email pengirim
$mail->Subject = $subject; //subyek email
$mail->AddAddress($to, $to_name);
//tujuan email

$mail->MsgHTML($text);
//$mail->Send();
if($mail->Send()) echo "Message has been sent";
else echo "Failed to sending message";

?>
