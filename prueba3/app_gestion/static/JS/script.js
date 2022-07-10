function validar()
{
   var nombre = document.formulario_ingreso.txt_nombre.value
   var appaterno = document.formulario_ingreso.txt_appaterno.value
   var apmaterno = document.formulario_ingreso.txt_apmaterno.value
   var rut = document.formulario_ingreso.txt_rut.value
   var vacuna = document.formulario_ingreso.txt_vacuna.value
   var edad = document.formulario_ingreso.num_edad.value


    //NOMBRE

   if (nombre.length<3)
   {
       alert("Nombre debe tener al menos 3 caracteres")
       document.formulario_ingreso.txt_nombre.focus();
       return false;
   }

    //APELLIDOS

   if (appaterno.length<3)
   {
       alert("Apellido Paterno debe tener al menos 3 caracteres")
       document.formulario_ingreso.txt_appaterno.focus();
       return false;
   }

   if (apmaterno.length<3)
   {
       alert("Apellido materno debe tener al menos 3 caracteres")
       document.formulario_ingreso.txt_apmaterno.focus();
       return false;
   }


    //RUT

   if(document.formulario_ingreso.txt_rut.value.length<=8||document.formulario_ingreso.txt_rut.value.length>10)
   {
       alert("Rut debe tener entre 9 y 10 caracteres")
       document.formulario_ingreso.txt_rut.focus()
       return false
   }
   var rut = document.formulario_ingreso.txt_rut.value
   var rutInvertido = rut.split('').reverse().join('')
   if(rutInvertido.substring(2,1)!="-")
   {
       alert("Rut debe contener el guión")
       document.formulario_ingreso.txt_rut.focus()
       return false
   }


    //VACUNA

    if (vacuna.length<3)
    {
        alert("Vacuna debe tener al menos 3 caracteres")
        document.formulario_ingreso.txt_fecha.focus();
        return false;
    }

    //EDAD

    if(edad<3)
    {
     alert("Debe ser mayor a 3 años para vacunarse")
     document.formulario_ingreso.num_edad.focus()   
     return false
    }

    //DIRECCION




    document.formulario_ingreso.action = "/ingresoPersona/"
    document.formulario_ingreso.submit() = true
   alert("Todo correctamente ingresado");
   

}