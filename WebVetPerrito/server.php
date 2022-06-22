<?php
    session_start();

    //variables
    $Nombre = "";
    $Apellido = "";
    $Numero = "";
    $Nombre_Mascota = "";
    $Raza_Mascota = "";
    $Sexo_Mascota = "";
    $Hora = "";

    $Email = "";

    $Fecha = "";
    $FDia = "";
    $FMes = "";
    $FAno = "";

    $errores = array();

    //conexion a BBDD
    require_once 'conexion.php';


    //registro
    if (isset($_POST["botonsubida"])) {

        function cleanup($data){
            return mysql_real_escape_string(trim(htmlentities(strip_tags($data))));
        }

        $Nombre = mysqli_real_escape_string($conn, $_POST["Nombre"]);
        $Apellido = mysqli_real_escape_string($conn, $_POST["Apellido"]);
        $Numero = mysqli_real_escape_string($conn, $_POST["Numero"]);
        $Nombre_Mascota = mysqli_real_escape_string($conn, $_POST["Nombre_Mascota"]);
        $Raza_Mascota = mysqli_real_escape_string($conn, $_POST["Raza_Mascota"]);
        $Sexo_Mascota = mysqli_real_escape_string($conn, $_POST["Sexo_Mascota"]);
        $Hora = mysqli_real_escape_string($conn, $_POST["Hora"]);

        $Email = mysqli_real_escape_string($conn, $_POST["Email"]);

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


        // Confirmacion de Fechas
        $sql = "SELECT * FROM fechas
        WHERE (Hora = '".$Hora."' AND Dia = '".$FDia."' AND Mes = '".$FMes."' AND Año = '".$FAno."')";

        $resultado = $conn -> query($sql);
        $row_count = $resultado -> num_rows;

        // Validacion

        if($row_count){
            $errores['mensaje']='Ya esta ingresado';}
            

        if(!empty($errores)){

            echo 'Hay errores en los datos del sistema. ';

        } else {

            // Registro 
            $query = "INSERT INTO agenda (Mes, Dia, Hora, Nombre, Apellido, Numero, Nombre_Mascota, Sexo_Mascota, Raza_Mascota) 
            VALUES('$FMes', '$FDia', '$Hora', '$Nombre', '$Apellido', '$Numero', '$Nombre_Mascota', '$Sexo_Mascota', '$Raza_Mascota')";
            mysqli_query($conn, $query) or die(mysqli_error());
            $_SESSION['Nombre'] = $Nombre;
            $_SESSION['success'] = "Registro Exitoso";
            header('location: index.php');

            $query = "INSERT INTO emails (Email) 
            VALUES('$Email')";
            mysqli_query($conn, $query) or die(mysqli_error());

            $query = "INSERT INTO fechas (Fechaentera, Dia, Mes, Año, Hora) 
            VALUES('$Fecha', '$FDia', '$FMes', '$FAno', '$Hora')";
            mysqli_query($conn, $query) or die(mysqli_error());

            if($conn->query($sql)===TRUE){
                echo "Registro Exitoso";
            }

        }

        if($row_count){
            echo 'Ha ocurrido un error en su solicitud, esta hora ya esta registrada.';
        }
        

        // Sistema de PHP Mailer implementado, pero no funcional.

        require_once "PHPMailer/PHPMailer.php";
        require_once "PHPMailer/SMTP.php";
        require_once "PHPMailer/Exception.php";

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
    }
?>