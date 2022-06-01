<?php

    include_once 'server.php';
    session_start();

    //variables
    $Nombre = "";
    $Apellido = "";
    $Numero = "";
    $Nombre_Mascota = "";
    $Raza_Mascota = "";
    $Sexo_Mascota = "";
    $Dia = "";
    $Hora = "";

    $Email = "";

    $Fecha = "";
    $FDia = "";
    $FMes = "";
    $FAno = "";

    //conexion a BBDD
    $db = mysqli_connect('localhost', 'root', '', 'virtuapet2');
    if(!$db){
        die('Error en la conexion con la Base de Datos:' .mysql_error());
       }


    //registro
    if (isset($_POST["botonsubida"])) {
        $Nombre = mysqli_real_escape_string($db, $_POST["Nombre"]);
        $Apellido = mysqli_real_escape_string($db, $_POST["Apellido"]);
        $Numero = mysqli_real_escape_string($db, $_POST["Numero"]);
        $Nombre_Mascota = mysqli_real_escape_string($db, $_POST["Nombre_Mascota"]);
        $Raza_Mascota = mysqli_real_escape_string($db, $_POST["Raza_Mascota"]);
        $Sexo_Mascota = mysqli_real_escape_string($db, $_POST["Sexo_Mascota"]);
        $Hora = mysqli_real_escape_string($db, $_POST["Hora"]);

        $Email = mysqli_real_escape_string($db, $_POST["Email"]);

        // Separacion de datos de la fecha
        $Fecha = $_POST["Fecha"];
        list($FAno, $FMes, $FDia) = explode('-', $Fecha);
        if ($FMes == "1") {$FMes = "ENERO";}
        if ($FMes == "2") {$FMes = "FEBRERO";}
        if ($FMes == "3") {$FMes = "MARZO";}
        if ($FMes == "4") {$FMes = "ABRIL";}
        if ($FMes == "5") {$FMes = "MAYO";}
        if ($FMes == "6") {$FMes = "JUNIO";}
        if ($FMes == "7") {$FMes = "JULIO";}
        if ($FMes == "8") {$FMes = "AGOSTO";}
        if ($FMes == "9") {$FMes = "SEPTIEMBRE";}
        if ($FMes == "10") {$FMes = "OCTUBRE";}
        if ($FMes == "11") {$FMes = "NOVIEMBRE";}
        if ($FMes == "12") {$FMes = "DICIEMBRE";}

        // Filtro para zonas en blanco ( Espacios requeridos )
        if (empty($Nombre)) {array_push($errors, "Nombre Requerido");}
        if (empty($Apellido)) {array_push($errors, "Apellido Requerido");}
        if (empty($Numero)) {array_push($errors, "Numero de telefono Requerido");}
        if (empty($Nombre_Mascota)) {array_push($errors, "Nombre de la Mascota Requerido");}
        if (empty($Raza_Mascota)) {array_push($errors, "Especie de la Mascota Requerido");}
        if (empty($Sexo_Mascota)) {array_push($errors, "Sexo de la Mascota Requerido");}
        if (empty($Hora)) {array_push($errors, "Hora Requerido");}
        if (empty($Email)) {array_push($errors, "Correo electronico Requerido");}
        if (empty($Fecha)) {array_push($errors, "Fecha de reserva Requerida");}

        // Registro 
        $query = "INSERT INTO agendamaxima (Nombre, Apellido, Numero, Nombre_Mascota, Raza_Mascota, Sexo_Mascota, Hora, Dia, Mes, Año, Email) 
            VALUES('$Nombre', '$Apellido', '$Numero', '$Nombre_Mascota', '$Raza_Mascota', '$Sexo_Mascota', '$Hora', '$FDia', '$FMes', '$FAno', '$Email')";
        mysqli_query($db, $query) or die(mysqli_error());
        $_SESSION['Nombre'] = $Nombre;
        $_SESSION['success'] = "Registro Exitoso";
        header('location: index.php');

        $query = "INSERT INTO emails (Email) 
            VALUES('$Email')";
        mysqli_query($db, $query) or die(mysqli_error());

        // require_once "PHPMailer/PHPMailer.php";
        // require_once "PHPMailer/SMTP.php";
        // require_once "PHPMailer/Exception.php";

        // $mail = new PHPMailer;

       
        // $mail->isSMTP();
        // $mail->Host = "smtp.gmail.com";
        // $mail->SMTPAuth = true;
        // $mail->Username = "vetperritoveterinaria@gmail.com";
        // $mail->Password = 'Vetperrito22';
        // $mail->SMTPSecure = 'ssl';
        // $mail->Port = 465;

        // $mail->isHTML(isHTML: true);
        // $mail->setFrom('vetperritoveterinaria@gmail.com', 'Veterinaria');
        // $mail->addAddress(address: $Email);

        // $mail->Subject = 'Here is the subject';
        // $mail->Body    = 'This is the HTML message body <b>in bold!</b>';
        // $mail->AltBody = 'This is the body in plain text for non-HTML mail clients';

        // if(!$mail->send()) {
        //     echo 'Message could not be sent.';
        //     echo 'Mailer Error: ' . $mail->ErrorInfo;
        // } else {
        //     echo 'Message has been sent';
        // }
    }
?>