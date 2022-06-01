<?php


// Variables

// Insercion de variables en el sistema de creacion
mysqli_query($conn,"INSERT INTO emails (Email, Dia, Hora) VALUES ('$Email', '$CDia', '$CHora')") or die(mysqli_error());
require_once 'mailer/class.phpmailer.php';

// Formato y creacion de correo electronico
$mail = new PHPMailer(true);
$mailid = $Email;
$subject = "Recordatorio de clinica veterinaria VetPerrito";
$text_message = "Muchas gracias por contar con nosotros.";
$message = "Se recuerda cordialmente que su hora del dia "||$CDia||" a las "||$CHora||" ha sido solicitada correctamente";

try
{
$mail->IsSMTP();
$mail->isHTML(true);
$mail->SMTPDebug = 0;
$mail->SMTPAuth = true;
$mail->SMTPSecure = "ssl";
$mail->Host = "smtp.gmail.com";
$mail->Port = '465';
$mail->AddAddress($mailid);
$mail->Username ="vetperritoveterinaria@gmail.com";
$mail->Password ="Vetperrito22";
$mail->SetFrom('vetperritoveterinaria@gmail.com','Veterinaria VetPerrito');
$mail->AddReplyTo("vetperritoveterinaria@gmail.com","Veterinaria VetPerrito");
$mail->Subject = $subject;
$mail->Body = $message;
$mail->AltBody = $message;
if($mail->Send())
{
echo "Gracias por su preferencia, Se ha enviado un correo electronico como recordatorio.";
}
}
catch(phpmailerException $ex)
{
$msg = "
".$ex->errorMessage()."
";
}
?>