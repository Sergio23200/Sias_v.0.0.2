// Se carga todo el DOM antes de comenzar a ejecutar el script
document.addEventListener("DOMContentLoaded", () => {
  // Se agrega un evento al formulario para manejar su envío
  document
    .getElementById("loginForm")
    .addEventListener("submit", async function (event) {
      event.preventDefault(); // Evita el envío predeterminado del formulario antes de la validación

      // Obtener los valores de los campos del formulario
      const tipoDocumento = document.getElementById("tipoDocumento").value;
      const numeroDocumento = document.getElementById("documento").value.trim();
      const contraseña = document.getElementById("contraseña").value.trim(); // Se usa .trim() para eliminar espacios innecesarios
      const rememberMe = document.getElementById("rememberMe");

      let valid = true; // Variable de control para determinar si todas las validaciones son correctas

      // Validación del tipo de documento
      if (tipoDocumento === "seleccionar") {
        document.getElementById("tipo_documento_incorrecto").textContent =
          "Debe seleccionar un tipo de documento";
        valid = false;
      } else {
        document.getElementById("tipo_documento_incorrecto").textContent = "";
      }

      // Validación del número de documento (debe contener exactamente 10 dígitos numéricos)
      if (!/^\d{10}$/.test(numeroDocumento)) {
        document.getElementById("documentoIncorrecto").textContent =
          "Número de documento inválido (debe tener 10 dígitos)";
        valid = false;
      } else {
        document.getElementById("documentoIncorrecto").textContent = "";
      }

      // Validación de la contraseña (mínimo 6 caracteres, máximo 12)
      if (contraseña.length < 6 || contraseña.length > 12) {
        document.getElementById("contraseñaIncorrecta").textContent =
          "La contraseña debe tener entre 6 y 12 caracteres";
        valid = false;
      } else {
        document.getElementById("contraseñaIncorrecta").textContent = "";
      }

      // Validación del correo electrónico utilizando una expresión regular
      const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

      // Validación de aceptación de términos y condiciones
      if (!rememberMe.checked) {
        document.getElementById("falta_terminos_y_condiciones").textContent =
          "Debe aceptar términos y condiciones para continuar";
        valid = false;
      } else {
        document.getElementById("falta_terminos_y_condiciones").textContent =
          "";
      }

      // Si todas las validaciones pasan, se envían los datos al backend en formato JSON
      if (valid) {
        const datosJSON = {
          tipo_documento: tipoDocumento,
          numero_documento: numeroDocumento,
          password: contraseña,
          remember_me: rememberMe.checked, // Indica si los términos y condiciones fueron aceptados
        };
        console.log(datosJSON);
        try {
          const response = await fetch("http://127.0.0.1:8000/login/", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify(datosJSON),
          });

          if (!response) {
            throw new Error("Error al enviar la solicitud al servidor");
          }

          const data = await response.json();
          console.log("Respuesta del servidor:", data);

          alert("Formulario enviado correctamente.");
        } catch (error) {
          console.error("Error en la solicitud:", error);
          alert("Hubo un problema con el envío de los datos.");
        }
      }
    });
});

    // Función para manejar menu desplegable
    function toggleMenu() {
      const menu = document.getElementById("menuOptions");
      menu.classList.toggle("active"); // Agrega o quita la clase "active"
  }