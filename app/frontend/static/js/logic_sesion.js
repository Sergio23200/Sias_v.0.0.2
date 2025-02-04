//se carga todo el DOM antes de comenzar a ejecutar
document
  .getElementById("loginForm")
  .addEventListener("submit", function (event) {
    event.preventDefault(); // Prevenir el envío del formulario antes de hacer la validación

    // Obtener los valores de los campos del DOM
    const tipoDocumento = document.getElementById("tipoDocumento").value;
    const numeroDocumento = document.getElementById("documento").value.trim();
    const contraseña = document.getElementById("contraseña").value.trim();//con .trim nos aseguramos de quitar espacios. 
    const rememberMe = document.getElementById("rememberMe");
    const email = document.getElementById("email").value.trim();
    const email_error = document.getElementById("email_incorrecto");

    let valid = true; // Bandera para saber si todas las validaciones pasaron

    // Validar el tipo de documento
    if (tipoDocumento == "seleccionar") {
      document.getElementById("tipo_documento_incorrecto").textContent =
        "Debe seleccionar tipo de documento";
      valid = false;
    } else {
      document.getElementById("tipo_documento_incorrecto").textContent = "";
    }
    // Validar el número de documento
    if (numeroDocumento.length !== 10) {
      document.getElementById("documentoIncorrecto").textContent =
        "Número de documento inválido (debe tener 10 dígitos)";
      valid = false;
    } else {
      document.getElementById("documentoIncorrecto").textContent = "";
    }

    // Validar la contraseña
    if (contraseña.length < 6 || contraseña.length > 12) {
      document.getElementById("contraseñaIncorrecta").textContent =
        "La contraseña debe tener entre 6 y 12 caracteres";
      valid = false;
    } else {
      document.getElementById("contraseñaIncorrecta").textContent = "";
    }

    //validar correo electronico 
    // Expresión regular para validar el email
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

    try {
        if (email === "") {
            throw "El campo email es obligatorio.";
        }
        if (!emailRegex.test(email)) {
            throw "Debe ingresar un email válido (usuario@dominio.com)";
        }
        if (email.includes("..")) {
            throw "El email no puede contener '..' en el dominio.";
        }
        if ((email.match(/@/g) || []).length > 1) {
            throw "El email no puede contener más de un '@'.";
        }
        if (/[^a-zA-Z0-9@._-]/.test(email)) {
            throw "El email contiene caracteres no válidos.";
        }

    } catch (error) {
      email_error.textContent = error; // Mostrar error en el formulario
  }


    // Aceptación de términos y condiciones
    if (!rememberMe.checked) {
      document.getElementById("falta_terminos_y_condiciones").textContent =
        "Debe aceptar términos y condiciones para continuar";
      valid = false;
    } else {
      document.getElementById("falta_terminos_y_condiciones").textContent = "";
    }



    // Si todas las validaciones pasan, enviar el formulario
    /*if (valid) {
      document.getElementById("loginForm").submit();
    }
  });*/
    // Si todas las validaciones pasan, enviar el formulario , crean el JSON y se envia.
    if (valid) {
      const datosJSON = {
        tipo_documento: tipoDocumento,
        numero_documento: numeroDocumento,
        password: contraseña,
        email : email,
        remember_me: rememberMe.checked, // Guardar si se aceptaron términos y condiciones
      };
      // Convertir a JSON
      const jsonString = JSON.stringify(datosJSON);
      console.log("Datos en JSON:", jsonString);

      // Enviar los datos con fetch 
      fetch("http://127.0.0.1:8000/login/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: jsonString,
      })
        .then((response) => response.json())
        .then((data) => console.log("Respuesta del servidor:", data))
        .catch((error) => console.error("Error:", error));

      // mensaje de exito
      alert("Formulario enviado correctamente.");
    }
  });

//funcion para manejo de menu hamburguesa
function toggleMenu() {
  const menu = document.getElementById("menuOptions");
  if (menu.style.display === "block") {
    menu.style.display = "none"; // Oculta el menú si ya está visible
  } else {
    menu.style.display = "block"; // Muestra el menú si está oculto
  }
}

//la variable numero_documento debe colocarse en el schema de login ya que no se encuentra .