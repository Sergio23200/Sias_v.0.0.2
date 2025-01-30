// Función para manejar el menú hamburguesa
function toggleMenu() {
  const menu = document.getElementById("menuOptions");
  if (menu.style.display === "block") {
    menu.style.display = "none"; // Oculta el menú si ya está visible
  } else {
    menu.style.display = "block"; // Muestra el menú si está oculto
  }
}

// Ejecutar el código solo cuando el DOM esté completamente cargado
document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("register_form");

  // Acceso a elementos del formulario
  const nombre = document.getElementById("fullName");
  const error_nombre = document.getElementById("fullNameError");

  const tipo_documento = document.getElementById("documentType");
  const error_tipo_documento = document.getElementById("documentTypeError");

  const numero_documento = document.getElementById("documentNumber");
  const error_numero_documento = document.getElementById("documentNumberError");

  const email = document.getElementById("email");
  const error_email = document.getElementById("emailError");

  const telefono = document.getElementById("phone");
  const error_telefono = document.getElementById("phoneError");

  const genero = document.getElementById("gender");
  const error_genero = document.getElementById("genderError");

  const ciudad = document.getElementById("city");
  const error_ciudad = document.getElementById("cityError");

  const direccion = document.getElementById("address");
  const error_direccion = document.getElementById("addressError");

  const membresia = document.getElementById("membership");
  const error_membresia = document.getElementById("membershipError");

  const historial_clinico = document.getElementById("clinicalHistoryId");
  const error_historial_clinico = document.getElementById("clinicalHistoryIdError");

  const fecha_nacimiento = document.getElementById("birthDate");
  const error_fecha_nacimiento = document.getElementById("birthDateError");

  const contraseña = document.getElementById("contraseña");
  const error_contraseña = document.getElementById("contraseñaError");

  const terminos = document.getElementById("rememberMe");
  const error_terminos = document.getElementById("rememberMeError");

  // Funciones auxiliares para manejar errores
  function mostrarError(elementoError, mensaje) {
    elementoError.textContent = mensaje;
  }

  function limpiarError(elementoError) {
    elementoError.textContent = "";
  }

  // Función de validación para cada campo
  function validarNombre() {
    try {
      limpiarError(error_nombre);
      if (nombre.value.trim() === "") {
        throw new Error("El campo nombre es obligatorio.");
      }
      if (!/^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$/.test(nombre.value)) {
        throw new Error("El nombre solo puede contener letras y espacios.");
      }
      return true;
    } catch (error) {
      mostrarError(error_nombre, error.message);
      return false;
    }
  }

  function validarTipoDocumento() {
    try {
      limpiarError(error_tipo_documento);
      if (tipo_documento.value === "") {
        throw new Error("Selecciona un tipo de documento.");
      }
      return true;
    } catch (error) {
      mostrarError(error_tipo_documento, error.message);
      return false;
    }
  }

  function validarDocumento() {
    try {
      limpiarError(error_numero_documento);
      if (numero_documento.value.trim() === "") {
        throw new Error("El número de documento es obligatorio.");
      }
      if (!/^[0-9]+$/.test(numero_documento.value)) {
        throw new Error("El número de documento debe contener solo números.");
      }
      return true;
    } catch (error) {
      mostrarError(error_numero_documento, error.message);
      return false;
    }
  }

  function validarEmail() {
    try {
      limpiarError(error_email);
      if (email.value.trim() === "") {
        throw new Error("El correo electrónico es obligatorio.");
      }
      if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value)) {
        throw new Error("El formato del correo electrónico no es válido.");
      }
      return true;
    } catch (error) {
      mostrarError(error_email, error.message);
      return false;
    }
  }

  function validarTelefono() {
    try {
      limpiarError(error_telefono);
      if (telefono.value.trim() === "") {
        throw new Error("El número de teléfono es obligatorio.");
      }
      if (!/^[0-9]+$/.test(telefono.value)) {
        throw new Error("El número de teléfono debe contener solo números.");
      }
      return true;
    } catch (error) {
      mostrarError(error_telefono, error.message);
      return false;
    }
  }

  function validarGenero() {
    try {
      limpiarError(error_genero);
      if (genero.value === "") {
        throw new Error("Selecciona un tipo de documento.");
      }
      return true;
    } catch (error) {
      mostrarError(error_genero, error.message);
      return false;
    }
  }

  function validarCiudad() {
    try {
      limpiarError(error_ciudad);
      if (ciudad.value.trim() === "") {
        throw new Error("El campo ciudad es obligatorio.");
      }
      if (!/^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$/.test(ciudad.value)) {
        throw new Error("La ciudad solo puede contener letras y espacios.");
      }
      return true;
    } catch (error) {
      mostrarError(error_ciudad, error.message);
      return false;
    }
  }

  function validarDireccion() {
    try {
      limpiarError(error_direccion);
      if (direccion.value.trim() === "") {
        throw new Error("El campo dirección es obligatorio.");
      }
      if (direccion.value.length < 5 || direccion.value.length > 50) {
        throw new Error("La dirección debe tener entre 5 y 50 caracteres.");
      }
      return true;
    } catch (error) {
      mostrarError(error_direccion, error.message);
      return false;
    }
  }

  function validarMembresia() {
    try {
      limpiarError(error_membresia);
      if (membresia.value === "") {
        throw new Error("Selecciona un tipo de documento.");
      }
      return true;
    } catch (error) {
      mostrarError(error_membresia, error.message);
      return false;
    }
  }

  function validarHistorialClinico() {
    try {
      limpiarError(error_historial_clinico);
      if (historial_clinico.value.trim() === "") {
        throw new Error("El campo dirección es obligatorio.");
      }
      if (historial_clinico.value.length < 5 || direccion.value.length > 15) {
        throw new Error("El historial clinico debe tener entre 5 y 8 caracteres.");
      }
      return true;
    } catch (error) {
      mostrarError(error_historial_clinico, error.message);
      return false;
    }
  }

  function validarFechaNacimiento() {
    try {
      limpiarError(error_fecha_nacimiento);
      if (fecha_nacimiento.value.trim() === "") {
        throw new Error("El campo fecha de nacimiento es obligatorio.");
      }
      const fechaNacimiento = new Date(fecha_nacimiento.value);
      const fechaActual = new Date();
      if (fechaNacimiento >= fechaActual) {
        throw new Error("La fecha de nacimiento no puede ser mayor o igual a la fecha actual.");
      }
      return true;
    } catch (error) {
      mostrarError(error_fecha_nacimiento, error.message);
      return false;
    }
  }

  function validarContraseña() {
    try {
      limpiarError(error_contraseña);
      if (contraseña.value.trim() === "") {
        throw new Error("El campo dirección es obligatorio.");
      }
      if (contraseña.value.length < 5 || direccion.value.length > 10) {
        throw new Error("La contraseña debe tener entre 5 y 10 caracteres.");
      }
      return true;
    } catch (error) {
      mostrarError(error_contraseña, error.message);
      return false;
    }
  }

  function validarTerminosAceptados() {
    try {
      limpiarError(error_terminos);
      if (!terminos.checked) {
        throw new Error("Debes aceptar los términos y condiciones para continuar.");
      }
      return true;
    } catch (error) {
      mostrarError(error_terminos, error.message);
      return false;
    }
  }

  // Validar el formulario al enviar
  form.addEventListener("submit", (event) => {
    const validaciones = [
      validarNombre(),
      validarTipoDocumento(),
      validarDocumento(),
      validarEmail(),
      validarTelefono(),
      validarGenero(),
      validarCiudad(),
      validarDireccion(),
      validarMembresia(),
      validarHistorialClinico(),
      validarFechaNacimiento(),
      validarContraseña(),
      validarTerminosAceptados(),
    ];

    // Si alguna validación falla, se previene el envío
    if (!validaciones.every((validacion) => validacion)) {
      event.preventDefault();
    }
  });
});


/*para pruebas antes del return console.log("Nombre válido:", nombre.value); // Mostrar en consola si es válido */