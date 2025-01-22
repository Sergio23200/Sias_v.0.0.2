// Validación del formulario de inicio de sesión
document
  .getElementById("login_Form")
  .addEventListener("submit", function (event) {
    event.preventDefault(); // Prevenir el envío del formulario antes de hacer la validación

    // Obtener los valores de los campos
    const tipoDocumento = document.getElementById("tipoDocumento").value;
    const numeroDocumento = document.getElementById("documento").value;
    const contraseña = document.getElementById("contraseña").value;

    const rememberMe = document.getElementById("rememberMe");

    // Variables del DOM PARA RECUPERACION DE CONTRASEÑA
    const forgotPasswordLink = document.getElementById("forgotPasswordLink");
    const forgotPasswordForm = document.getElementById("forgotPasswordForm");
    const recoverPasswordBtn = document.getElementById("recoverPasswordBtn");
    const emailInput = document.getElementById("email");
    const recoveryMessage = document.getElementById("recoveryMessage");
    const cancelRecoveryLink = document.getElementById("cancelRecoveryLink");

    // Validar el tipo de documento
    if (tipoDocumento === "CC") {
      console.log("Tipo de documento: Cédula de Ciudadanía");
    } else if (tipoDocumento === "TI") {
      console.log("Tipo de documento: Tarjeta de Identidad");
    } else if (tipoDocumento === "PAS") {
      console.log("Tipo de documento: Pasaporte");
    } else {
      alert("Por favor, selecciona un tipo de documento");
      return;
    }

    if (tipoDocumento == "seleccionar") {
      document.getElementById("tipo_documento_incorrecto").textContent =
        "Debe seleccionar tipo de documento";
      return;
    } else {
      document.getElementById("tipo_documento_incorrecto").textContent = "";
      console.log(tipoDocumento);
    }

    //Aceptacion de terminos y condiciones
    if (!rememberMe.checked) {
      document.getElementById("falta_terminos_y_condiciones").textContent =
        "Debe aceptar terminos y condiciones para continuar";
      return;
    } else {
      document.getElementById("falta_terminos_y_condiciones").textContent = "";
      console.log(rememberMe);
    }

    // Validar el número de documento
    if (numeroDocumento.length < 10 || numeroDocumento.length > 10) {
      document.getElementById("documentoIncorrecto").textContent =
        "Número de documento inválido";
      return;
    } else {
      document.getElementById("documentoIncorrecto").textContent = ""; // Limpiar mensaje de error si es válido
      console.log(numeroDocumento);
    }

    // Validar la contraseña
    if (contraseña.length < 8) {
      document.getElementById("contraseñaIncorrecta").textContent =
        "Recordar que la contraseña debe tener 8 digitos ";
      return;
    } else {
      document.getElementById("contraseñaIncorrecta").textContent = ""; // Limpiar mensaje de error si es válido
      console.log(contraseña);
    }

    // si el proceso de inicio de sesion es exitoso
    // Aquí podrías agregar el código para enviar el formulario o realizar una acción posterior
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

console.log(tipoDocumento);
console.log(numeroDocumento);
console.log(contraseña);
console.log(rememberMe);
