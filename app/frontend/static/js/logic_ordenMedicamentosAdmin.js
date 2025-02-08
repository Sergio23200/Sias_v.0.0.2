document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("form-medicamentos");

  // Referencias a los elementos del formulario y mensajes de error
  const nombreInput = document.getElementById("nombre");
  const nombreError = document.getElementById("nombre_incorrecto");

  const tipoDocumentoInput = document.getElementById("tipoDocumento");
  const tipoDocumentoError = document.getElementById("tipo_documento_incorrecto");

  const documentoInput = document.getElementById("documento");
  const documentoError = document.getElementById("numero_documento_incorrecto");

  const emailInput = document.getElementById("email");
  const emailError = document.getElementById("emailError");

  const medicamentosInput = document.getElementById("medicamentos");
  const medicamentosError = document.getElementById("orden_error");

  // Función para mostrar errores
  function mostrarError(elementoError, mensaje) {
      elementoError.textContent = mensaje;
  }

  function limpiarError(elementoError) {
      elementoError.textContent = "";
  }

  // Funciones de validación
  function validarNombre() {
      limpiarError(nombreError);
      if (nombreInput.value.trim() === "") {
          mostrarError(nombreError, "El nombre es obligatorio.");
          return false;
      }
      if (!/^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$/.test(nombreInput.value)) {
          mostrarError(nombreError, "El nombre solo puede contener letras y espacios.");
          return false;
      }
      return true;
  }

  function validarTipoDocumento() {
      limpiarError(tipoDocumentoError);
      if (tipoDocumentoInput.value === "") {
          mostrarError(tipoDocumentoError, "Selecciona un tipo de documento.");
          return false;
      }
      return true;
  }

  function validarDocumento() {
      limpiarError(documentoError);
      if (documentoInput.value.trim() === "") {
          mostrarError(documentoError, "El número de documento es obligatorio.");
          return false;
      }
      if (!/^\d+$/.test(documentoInput.value)) {
          mostrarError(documentoError, "El número de documento debe contener solo números.");
          return false;
      }
      return true;
  }

  function validarEmail() {
      limpiarError(emailError);
      if (emailInput.value.trim() === "") {
          mostrarError(emailError, "El correo electrónico es obligatorio.");
          return false;
      }
      if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(emailInput.value)) {
          mostrarError(emailError, "El formato del correo electrónico no es válido.");
          return false;
      }
      return true;
  }

  function validarMedicamentos() {
      limpiarError(medicamentosError);
      if (medicamentosInput.value.trim() === "") {
          mostrarError(medicamentosError, "La orden de medicamentos es obligatoria.");
          return false;
      }
      return true;
  }

  // Evento submit del formulario
  form.addEventListener("submit", async (event) => {
      event.preventDefault(); // Evitar el envío predeterminado

      // Ejecutar validaciones
      const nombreValido = validarNombre();
      const tipoDocumentoValido = validarTipoDocumento();
      const documentoValido = validarDocumento();
      const emailValido = validarEmail();
      const medicamentosValidos = validarMedicamentos();

      if (!nombreValido || !tipoDocumentoValido || !documentoValido || !emailValido || !medicamentosValidos) {
          return; // Si alguna validación falla, no se envía el formulario
      }

      // Crear objeto JSON con los datos del formulario
      const datosJSON = {
          nombre: nombreInput.value.trim(),
          tipo_documento: tipoDocumentoInput.value.trim(),
          numero_documento: documentoInput.value.trim(),
          email: emailInput.value.trim(),
          medicamentos: medicamentosInput.value.trim()
      };

      console.log("Datos a enviar:", datosJSON); // Verificar en consola antes de enviar

      try {
          const response = await fetch("http://127.0.0.1:8000/api/ordenes", {
              method: "POST",
              headers: {
                  "Content-Type": "application/json",
              },
              body: JSON.stringify(datosJSON),
          });

          if (!response.ok) {
              throw new Error("Error al enviar los datos.");
          }

          const data = await response.json();
          console.log("Respuesta del servidor:", data);

          // Guardar datos en localStorage
          localStorage.setItem("nombre", datosJSON.nombre);
          localStorage.setItem("tipo_documento", datosJSON.tipo_documento);
          localStorage.setItem("numero_documento", datosJSON.numero_documento);
          localStorage.setItem("email", datosJSON.email);
          localStorage.setItem("medicamentos", datosJSON.medicamentos);

          alert("Orden enviada correctamente.");
          window.location.href = "mensajeConfirmacionMedicamentos.html"; // Redirigir a página de confirmación

      } catch (error) {
          console.error("Error en la solicitud:", error);
          alert("Hubo un problema al enviar la orden.");
      }
  });
});