<?php
    require 'config.php';

//conexion XAMPP
    $servername = "localhost";  
    $username = "root";  
    $password = "";  
    $conn = mysql_connect ($servername , $username , $password) or die("Fallo al conectar con la Base de Datos");  
    $sql = mysql_select_db ('test',$conn) or die("Fallo al conectar con la Base de Datos"); 



//filtros varios
    function filtro($datos){
        $datos = trim($datos); // Elimina espacios antes y después de los datos
        $datos = stripslashes($datos); // Elimina backslashes (\)
        $datos = htmlspecialchars($datos); // Traduce caracteres especiales en entidades HTML
        return $datos;
    }

//post a las variables
    if(isset($_POST["submit"]) && $_SERVER["REQUEST_METHOD"] == "POST"){
        $nombre = filtro($_POST["Nombre"]);
        $apellido = filtro($_POST["Apellido"]);
        $numero = filtro($_POST["Numero"]);
        $nombre_mascota = filtro($_POST["Nombre_Mascota"]);
        $raza_mascota = filtro($_POST["Raza_Mascota"]);
        $sexo_mascota = filtro($_POST["Sexo_Mascota"]);
        $dia = filtro($_POST["Dia"]);
        $hora = filtro($_POST["Hora"]);
    }

//filtro interno
    if(isset($_POST["submit"]) && $_SERVER["REQUEST_METHOD"] == "POST"){
        // El campos obligatorios
        if(empty($_POST["Nombre"])){
            $errores[] = "Su nombre es requerido";
        }
        if(empty($_POST["Apellido"])){
            $errores[] = "Su Apellido es requerido";
        }
        if(empty($_POST["Numero"]) || strlen($_POST["Numero"]) < 5){
            $errores[] = "Su numero tiene fallos y debe ser de 9 caracteres";
        }
        if(empty($_POST["Nombre_Mascota"])){
            $errores[] = "El nombre de su mascota es requerido";
        }
        if(empty($_POST["Raza_Mascota"])){
            $errores[] = "La especie es requerida";
        }
        if(empty($_POST["Sexo_Mascota"])){
            $errores[] = "El sexo de su mascota es requerido";
        }
        if(empty($_POST["Dia"])){
            $errores[] = "El dia es requerido";
        }
        if(empty($_POST["Hora"])){
            $errores[] = "La hora es requerida";
        }
        // Si no hay errores, se aceptan los datos.
        if(empty($errores)) {
            $nombre = filtro($_POST["Nombre"]);
            $apellido = filtro($_POST["Apellido"]);
            $numero = filtro($_POST["Numero"]);
            $nombre_mascota = filtro($_POST["Nombre_Mascota"]);
            $raza_mascota = filtro($_POST["Raza_Mascota"]);
            $sexo_mascota = filtro($_POST["Sexo_Mascota"]);
            $dia = filtro($_POST["Dia"]);
            $hora = filtro($_POST["Hora"]);
        }
    }

    //post
    if(isset($_POST['botonsubida'])){
        $_SESSION['Nombre'] = $nombre;
        $_SESSION['Apellido'] = $apellido;
        $_SESSION['Numero'] = $numero;
        $_SESSION['Nombre_Mascota'] = $nombre_mascota;
        $_SESSION['Raza_Mascota'] = $raza_mascota;
        $_SESSION['Sexo_Mascota'] = $sexo_mascota;
        $_SESSION['Dia'] = $dia;
        $_SESSION['Hora'] = $hora;

        $query = mysqli_query($con, "INSERT INTO agenda VALUES ('', '$nombre', '$apellido', '$numero', '$nombre_mascota', '$raza_mascota', '$sexo_mascota', '$dia', '$hora')");
    }

?>