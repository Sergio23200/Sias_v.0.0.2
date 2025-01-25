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

  // Función para manejar errores y mostrar mensajes
  function mostrarError(elementoError, mensaje) {
    elementoError.textContent = mensaje;
  }

  function limpiarError(elementoError) {
    elementoError.textContent = "";
  }

  // Función para validar nombre
  function validarNombre() {
    try {
      limpiarError(nombreError);
      if (nombreInput.value.trim() === "") {
        throw new Error("El nombre es obligatorio.");
      }
      if (!/^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$/.test(nombreInput.value)) {
        throw new Error("El nombre solo puede contener letras y espacios.");
      }
      console.log("Validación nombre correcta");  // validar que el formulario funcione e imprima por consola 
      return true;
    } catch (error) {
      mostrarError(nombreError, error.message);
      console.log("Error en nombre:", error.message);  //validar que el formulario funcione e imprima por consola 
      return false;
    }
  }

  // Función para validar tipo de documento
  function validarTipoDocumento() {
    try {
      limpiarError(tipoDocumentoError);
      if (tipoDocumentoInput.value === "") {
        throw new Error("Selecciona un tipo de documento.");
      }
      console.log("Seleccion correcta");  // validar que el formulario funcione e imprima por consola 
      return true;
    } catch (error) {
      mostrarError(tipoDocumentoError, error.message);
      console.log("Debe seleccionar alguna opcion", error.message);  //validar que el formulario funcione e imprima por consola 
      return false;
    }
  }

  // Función para validar número de documento
  function validarDocumento() {
    try {
      limpiarError(documentoError);
      if (documentoInput.value.trim() === "") {
        throw new Error("El número de documento es obligatorio.");
      }
      if (!/^[0-9]+$/.test(documentoInput.value)) {
        throw new Error("El número de documento debe contener solo números.");
      }
      console.log("Documento enviado correctamente");  // validar que el formulario funcione e imprima por consola 
      return true;
    } catch (error) {
      mostrarError(documentoError, error.message);
      console.log("Documento incorrecto ", error.message);  //validar que el formulario funcione e imprima por consola 
      return false;
    }
  }

  // Función para validar correo electrónico
  function validarEmail() {
    try {
      limpiarError(emailError);
      if (emailInput.value.trim() === "") {
        throw new Error("El correo electrónico es obligatorio.");
      }
      if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(emailInput.value)) {
        throw new Error("El formato del correo electrónico no es válido.");
      }
      console.log("Validación email correcta");  // validar que el formulario funcione e imprima por consola 
      return true;
    } catch (error) {
      mostrarError(emailError, error.message);
      console.log("Error email:", error.message);  //validar que el formulario funcione e imprima por consola 
      return false;
    }
  }

  // Función para validar medicamentos/orden
  function validarMedicamentos() {
    try {
      limpiarError(medicamentosError);
      if (medicamentosInput.value.trim() === "") {
        throw new Error("La orden de medicamentos es obligatoria.");
      }
      console.log("Validación ORDEN correcta");  // validar que el formulario funcione e imprima por consola 
      return true;
    } catch (error) {
      mostrarError(medicamentosError, error.message);
      console.log("Error numero de ORDEN", error.message);  //validar que el formulario funcione e imprima por consola 
      return false;
    }
  }

  // Validar el formulario al enviar
  form.addEventListener("submit", (event) => {
    const nombreValido = validarNombre();
    const tipoDocumentoValido = validarTipoDocumento();
    const documentoValido = validarDocumento();
    const emailValido = validarEmail();
    const medicamentosValidos = validarMedicamentos();

    // Prevenir el envío si alguna validación falla
    if (!nombreValido || !tipoDocumentoValido || !documentoValido || !emailValido || !medicamentosValidos) {
      event.preventDefault();
    }
    //validar por consola
    console.log("Formulario validado correctamente: ", {
      nombreValido,
      tipoDocumentoValido,
      documentoValido,
      emailValido,
      medicamentosValidos
    });
  });
});


