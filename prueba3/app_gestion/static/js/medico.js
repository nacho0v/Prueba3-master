const $formulario_medico = document.getElementById('formulario_medico');

const $txt_med_rut =document.getElementById('txt_med_rut');
const $txt_med_nombre =document.getElementById('txt_med_nombre');
const $txt_med_appaterno =document.getElementById('txt_med_appaterno');
const $txt_med_apmaterno =document.getElementById('txt_med_apmaterno');

(function (){

   $formulario_medico.addEventListener('submit', function(e){
    const $txt_med_rut =document.getElementById('txt_med_rut');
    const $txt_med_nombre =document.getElementById('txt_med_nombre');
    const $txt_med_appaterno =document.getElementById('txt_med_appaterno');
    const $txt_med_apmaterno =document.getElementById('txt_med_apmaterno');

          let nombre = String($txt_med_nombre.value).trim();
          let appaterno = String($txt_med_appaterno.value).trim();
          let apmaterno = String($txt_med_apmaterno.value).trim();
          let rut = String($txt_med_rut.value).trim();

           //Rut
           if(rut.length===0)
           {
              alert("El rut del médico no puede ir en blanco")
              e.preventDefault();
              return false;
           }
           if(rut.length<=8||rut.length>10)
           {
               alert("Rut del médico debe tener entre 9 y 10 caracteres")
               e.preventDefault();
               return false;
           }
           var rutInvertido = rut.split('').reverse().join('')
           if(rutInvertido.substring(2,1)!="-")
           {
               alert("Rut del médico debe contener el guión")
               e.preventDefault();
               return false;
           }

          //Nombre
           if(nombre.length===0)
           {
              alert("El nombre de médico no puede ir en blanco")
              e.preventDefault();
              return false;
           }
           if(nombre.length<3)
           {
              alert("Nombre del médico debe tener al menos 3 caracteres")
              e.preventDefault();
              return false;
           } 

           //Apellidos
           if(appaterno.length===0)
           {
              alert("El apellido paterno del médico no puede ir en blanco")
              e.preventDefault();
              return false;
           }    
           if (appaterno.length<3)
           {
               alert("Apellido Paterno del médico debe tener al menos 3 caracteres")
               e.preventDefault();
               return false;
           }

           if(apmaterno.length===0)
           {
              alert("El apellido materno del médico no puede ir en blanco")
              e.preventDefault();
              return false;
           }    

           if (apmaterno.length<3)
           {
               alert("Apellido materno del médico debe tener al menos 3 caracteres")
               e.preventDefault();
               return false;
           }
           

       });

})();
