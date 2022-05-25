function validar(){
    var vnombre, vapellido, vnumero, vnombre_mascota, vraza_mascota, vsexo_mascota, dia, hora;

    vnombre = document.getElementById("Nombre").value;
    vapellido = document.getElementById("Apellido").value;
    vnumero = document.getElementById("Numero").value;
    vnombre_mascota = document.getElementById("Nombre_Mascota").value;
    vraza_mascota = document.getElementById("Raza_Mascota").value;
    vsexo_mascota = document.getElementById("Sexo_Mascota").value;
    dia = document.getElementsByName("Dia");
    hora = document.getElementById("Hora").value;

    validarApellido = /[a-z]/;
    validarNombre = /[a-z]/;
    validarNombre_Mascota = /[a-z]/;

    //Nombre
    if (vnombre == "") {
        alert("El nombre esta vacio");
        return false;
    }
    if (!validarNombre.test(vnombre)) {
        alert("El nombre ingresado no es valido")
        return false;
    }

    //Apellido
    if (vapellido == "") {
        alert("El apellido esta vacio");
        return false;
    }
    if (!validarApellido.test(vapellido)) {
        alert("El apellido ingresado no es valido")
        return false;
    }

    //Numero
    if (vnumero == "") {
        alert("El Numero de telefono esta vacio");
        return false;
    }
    if (isNaN(vnumero)) {
        alert("El Numero de telefono ingresado no es valido")
        return false;
    }
    if (vnumero.length != 9) {
        alert("El Numero de telefono ingresado no es valido ej: '123456789' ")
        return false;
    }
 
    //Nombre_Mascota
    if (vnombre_mascota == "") {
        alert("El nombre de la mascota esta vacio");
        return false;
    }
    if (!validarNombre_Mascota.test(vnombre_mascota)) {
        alert("El nombre de la mascota ingresado no es valido")
        return false;
    }

        
}