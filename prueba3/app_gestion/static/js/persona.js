 const $formulario_ingreso = document.getElementById('formulario_ingreso');

 const $txt_rut =document.getElementById('txt_rut');
 const $txt_nombre =document.getElementById('txt_nombre');
 const $txt_appaterno =document.getElementById('txt_appaterno');
 const $txt_apmaterno =document.getElementById('txt_apmaterno');
 const $txt_vacuna =document.getElementById('txt_vacuna');

 (function (){

    $formulario_ingreso.addEventListener('submit', function(e){
        const $txt_rut =document.getElementById('txt_rut');
        const $txt_nombre =document.getElementById('txt_nombre');
        const $txt_appaterno =document.getElementById('txt_appaterno');
        const $txt_apmaterno =document.getElementById('txt_apmaterno');
        const $txt_vacuna =document.getElementById('txt_vacuna');

           let nombre = String($txt_nombre.value).trim();
           let appaterno = String($txt_appaterno.value).trim();
           let apmaterno = String($txt_apmaterno.value).trim();
           let vacuna = String($txt_vacuna.value).trim();
           let rut = String($txt_rut.value).trim();

            //Rut
            if(rut.length===0)
            {
               alert("El rut del paciente no puede ir en blanco")
               e.preventDefault();
               return false;
            }
            if(rut.length<=8||rut.length>10)
            {
                alert("Rut del paciente debe tener entre 9 y 10 caracteres")
                e.preventDefault();
                return false;
            }
            var rutInvertido = rut.split('').reverse().join('')
            if(rutInvertido.substring(2,1)!="-")
            {
                alert("Rut del paciente debe contener el guión")
                e.preventDefault();
                return false;
            }

           //Nombre
            if(nombre.length===0)
            {
               alert("El nombre de paciente no puede ir en blanco")
               e.preventDefault();
               return false;
            }
            if(nombre.length<3)
            {
               alert("Nombre del paciente debe tener al menos 3 caracteres")
               e.preventDefault();
               return false;
            } 

            //Apellidos
            if(appaterno.length===0)
            {
               alert("El apellido paterno del paciente no puede ir en blanco")
               e.preventDefault();
               return false;
            }    
            if (appaterno.length<3)
            {
                alert("Apellido Paterno del paciente debe tener al menos 3 caracteres")
                e.preventDefault();
                return false;
            }

            if(apmaterno.length===0)
            {
               alert("El apellido materno del paciente no puede ir en blanco")
               e.preventDefault();
               return false;
            }    

            if (apmaterno.length<3)
            {
                alert("Apellido materno del paciente debe tener al menos 3 caracteres")
                e.preventDefault();
                return false;
            }

            //Vacuna
            if(vacuna.length===0)
            {
               alert("Vacuna no puede ir en blanco")
               e.preventDefault();
               return false;
            }

            if (vacuna.length<3)
            {
                alert("Vacuna debe tener al menos 3 caracteres")
                e.preventDefault();
                return false;
                
            }
            

        });

 })();
