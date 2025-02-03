document
  .getElementById("loginForm") // Asegúrate de que el ID es correcto en tu HTML
  .addEventListener("submit", function (event) {
    event.preventDefault(); // Prevenir el envío del formulario antes de hacer la validación

    // Obtener los valores de los campos
    const tipoDocumento = document.getElementById("tipoDocumento").value;
    const numeroDocumento = document.getElementById("documento").value;
    const contraseña = document.getElementById("contraseña").value;
    const rememberMe = document.getElementById("rememberMe");

    let valid = true; // Bandera para saber si todas las validaciones pasaron

    // Validar el tipo de documento
    if (tipoDocumento == "seleccionar") {
      document.getElementById("tipo_documento_incorrecto").textContent =
        "Debe seleccionar tipo de documento";
      valid = false;
    } else {
      document.getElementById("tipo_documento_incorrecto").textContent = "";
    }

    // Aceptación de términos y condiciones
    if (!rememberMe.checked) {
      document.getElementById("falta_terminos_y_condiciones").textContent =
        "Debe aceptar términos y condiciones para continuar";
      valid = false;
    } else {
      document.getElementById("falta_terminos_y_condiciones").textContent = "";
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
    if (contraseña.length < 8) {
      document.getElementById("contraseñaIncorrecta").textContent =
        "La contraseña debe tener al menos 8 caracteres";
      valid = false;
    } else {
      document.getElementById("contraseñaIncorrecta").textContent = "";
    }

    // Si todas las validaciones pasan, enviar el formulario
    if (valid) {
      document.getElementById("loginForm").submit();
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
