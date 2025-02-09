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
      const email = document.getElementById("email").value.trim();
      const email_error = document.getElementById("email_incorrecto");

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
        email_error.textContent = ""; // Si no hay errores, se limpia el mensaje
      } catch (error) {
        email_error.textContent = error; // Se muestra el mensaje de error en el formulario
        valid = false;
      }

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
          email: email,
          remember_me: rememberMe.checked, // Indica si los términos y condiciones fueron aceptados
        };

        try {
          const response = await fetch("http://127.0.0.1:8000/login/", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify(datosJSON),
          });

          if (!response.ok) {
            throw new Error("Error al enviar la solicitud al servidor");
          }

          const data = await response.json();
          console.log("Respuesta del servidor:", data);

          alert("Formulario enviado correctamente.");

          // Redirigir a otra página tras el envío exitoso
          window.location.href = "/dashboard.html";
        } catch (error) {
          console.error("Error en la solicitud:", error);
          alert("Hubo un problema con el envío de los datos.");
        }
      }
    });
});

// Función para manejar el menú hamburguesa en dispositivos móviles
function toggleMenu() {
  const menu = document.getElementById("menuOptions");
  menu.classList.toggle("show"); // Alterna la visibilidad del menú
}
