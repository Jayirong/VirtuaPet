<?php 
    include ('server.php');

?>

<!DOCTYPE html> 
<html lang="en"> 
  <head> 
    <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
        <meta name="description" content="" />
        <meta name="author" content="" />
        <title>Registro</title>
        <!-- Favicon-->
        <link rel="icon" type="image/x-icon" href="assets/favicon.png" />
        <!-- Fuente -->
        <script src="https://use.fontawesome.com/releases/v6.1.0/js/all.js" crossorigin="anonymous"></script>
        <!-- Google fonts -->
        <link href="https://fonts.googleapis.com/css?family=Montserrat:400,700" rel="stylesheet" type="text/css" />
        <link href="https://fonts.googleapis.com/css?family=Roboto+Slab:400,100,300,700" rel="stylesheet" type="text/css" />
        <!-- Core CSS -->
        <link href="css/styles.css" rel="stylesheet" />
 
</head> 



<body> 
  <!-- Barra de Navegacion Superior -->
  <nav class="navbar navbar-expand-lg navbar-dark fixed-top" id="mainNav">
    <div class="container">
        <a class="navbar-brand" href="index.php"><img src="assets/img/navbar-logo.png" alt="..." /></a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
            Menu
            <i class="fas fa-bars ms-1"></i>
        </button>
        <div class="collapse navbar-collapse" id="navbarResponsive">
            <ul class="navbar-nav text-uppercase ms-auto py-4 py-lg-0">
                <li class="nav-item"><a class="nav-link" href="registro.php">Reservas</a></li>
                <li class="nav-item"><a class="nav-link" href="contacto.php">Contacto</a></li>
                <li class="nav-item"><a class="nav-link" href="redes.php">Redes</a></li>
            </ul>
        </div>
    </div>
    </nav>

  <!-- Item Grid -->
    <section class="page-section bg-light" id="portfolio" >
    <div class="container">
        <div class="text-center">
            <h2 class="section-heading text-uppercase">Reservas</h2>
            <h3 class="section-subheading text-muted">Nuestro nuevo motor de reservas le asegura un uso comodo y rapido.</h3>
        </div>

        <div class="row">
            <div class="col-lg-4 col-sm-6 mb-4">
                <!-- Item de portafolio 1 -->
                <div class="portfolio-item">
                    <a class="portfolio-link" data-bs-toggle="modal" href="#portfolioModal1">
                        <div class="portfolio-hover">
                            <div class="portfolio-hover-content"><i class="fas fa-plus fa-3x"></i></div>
                        </div>
                        <img class="img-fluid" src="assets/img/portfolio/1.jpg" alt="..." />
                    </a>
                    <div class="portfolio-caption">
                        <div class="portfolio-caption-heading">Ingrese sus datos personales aqui.</div>
                        <div class="portfolio-caption-subheading text-muted">Digite sus datos para iniciar su proceso de reserva.</div>
                    </div>
                </div>
            </div>
    </section>

    <!-- Grid -->
    <section>

    <!-- Contenido del item del prtaforlio 1 -->
    <div class="portfolio-modal modal fade" id="portfolioModal1" tabindex="-1" role="dialog" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="close-modal" data-bs-dismiss="modal"><img src="assets/img/close-icon.svg" alt="Close modal" /></div>
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-lg-8">
                        <div class="modal-body">
                            <!-- Contenido y formulario de entrada 1 --> 
                            <h2 class="text-uppercase">Ingrese sus datos</h2>
                            <p class="item-intro text-muted">Digite sus datos para iniciar su proceso de reserva.</p>
                            <form action="registro.php" method="post" onsubmit="return validar();">

                                <!-- Fecha -->
                                <div class="form-group"> 
                                    <label for="Fecha">Fecha: </label>
                                    <input type="date" class="form-control" id="Fecha" name="Fecha" required value="<?php echo $Fecha; ?>">
                                </div> 
                                <br>

                                <!-- Hora -->
                                <div class="form-group">    
                                    <label for="Hora">Ingrese su hora:</label>
                                    <?php
                                        $conexion = mysqli_connect("localhost","root","","virtuapet2");
                                        $s = mysqli_query($conexion,"SELECT * FROM Horarios")
                                    ?>
                                    <select class="form-control" id="Hora" name="Hora" required  value="<?php echo $Hora; ?>"> 
                                        <?php
                                        while($r = mysqli_fetch_array($s)){
                                            ?>
                                            <option> <?php echo $r['Horarios']; ?> </option> 
                                            <?php
                                        }
                                        ?>
                                    </select>
                                </div>
                                <br>

                                <!-- Nombre -->
                                <div class="form-group"> 
                                    <label for="Nombre">Ingrese su nombre:</label>
                                    <input type="text" class="form-control" id="Nombre" name="Nombre" required value="<?php echo $Nombre; ?>">
                                </div> 
                                <br>

                                <!-- Apellido -->
                                <div class="form-group"> 
                                    <label for="Apellido">Ingrese su apellido:</label>
                                    <input type="text" class="form-control" id="Apellido" name="Apellido" required value="<?php echo $Apellido; ?>">
                                </div>
                                <br>

                                <!-- Numero -->
                                <div class="form-group"> 
                                    <label for="Numero">Ingrese su numero de telefono:</label>
                                    <input type="text" class="form-control" id="Numero" name="Numero" required value="<?php echo $Numero; ?>">
                                </div>
                                <br>

                                <!-- Correo -->
                                <div class="form-group"> 
                                    <label for="Email">Ingrese su correo electronico: ( Se enviara una confirmacion )</label>
                                    <input type="text" class="form-control" id="Email" name="Email" required value="<?php echo $Email; ?>">
                                </div> 
                                <br>

                                <!-- Nombre Mascota -->
                                <div class="form-group">
                                    <label for="Nombre_Mascota">Ingrese el nombre de su mascota:</label>
                                    <input type="text" class="form-control" id="Nombre_Mascota" name="Nombre_Mascota" required value="<?php echo $Nombre_Mascota; ?>">
                                </div>
                                <br>

                                <!-- Especie Mascota -->
                                <div class="form-group">          
                                    <label for="Raza_Mascota">Seleccione la especie de su mascota</label> 
                                    <select class="form-control" id="Raza_Mascota" name="Raza_Mascota" required  value="<?php echo $Raza_Nombre; ?>"> 
                                        <option value="Perro">Perro</option> 
                                        <option value="Gato">Gato</option>
                                        <option value="Hamster">Hamster</option> 
                                        <option value="Tortuga">Tortuga</option>
                                        <option value="Conejo">Conejo</option>
                                        <option value="Otro">Otro</option> 
                                    </select> 
                                </div>
                                <br>

                                <!-- Sexo Mascota -->
                                <div class="form-group">          
                                    <label for="Sexo_Mascota">Seleccione el genero de su mascota</label> 
                                    <select class="form-control" id="Sexo_Mascota" name="Sexo_Mascota" required value="<?php echo $Sexo_Mascota; ?>"> 
                                        <option value="Masculino">Masculino</option> 
                                        <option value="Femenino">Femenino</option>
                                    </select> 
                                </div>

                            <br>
                            <hr>
                            <br>
                            <input type="SUBMIT" name="botonsubida" value="            Reservar Hora            " class="btn btn-danger">
                            </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Footer -->
<footer class="footer py-4">
    <div class="container">
        <div class="row align-items-center">
            <div class="col-lg-4 text-lg-start">Copyright &copy; VirtuaPet 2022</div>
            <div class="col-lg-4 my-3 my-lg-0">
                <a class="btn btn-dark btn-social mx-2" href="https://twitter.com/vetperrito" aria-label="Twitter"><i class="fab fa-twitter"></i></a>
                <a class="btn btn-dark btn-social mx-2" href="https://www.facebook.com/profile.php?id=100081358071030" aria-label="Facebook"><i class="fab fa-facebook-f"></i></a>
                <a class="btn btn-dark btn-social mx-2" href="http://www.instagram.com" aria-label="Instagram"><i class="fab fa-laptop"></i></a>
            </div>
            <div class="col-lg-4 text-lg-end">
                <a class="link-dark text-decoration-none me-3" href="contacto.php">Conoce Mas</a>
                <a class="link-dark text-decoration-none" href="uso.php">Terminos de Uso</a>
            </div>
        </div>
    </div>
</footer>

  <!--JS -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
  <script src="js/validar.js"></script>
  
</body>
</html>