document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("register_form");

  form.addEventListener("submit", async function (event) {
    event.preventDefault(); // Evitar el envío tradicional del formulario

    // Obtener valores del formulario
    const formData = {
      fullName: document.getElementById("fullName").value.trim(),
      documentType: document.getElementById("documentType").value,
      documentNumber: document.getElementById("documentNumber").value.trim(),
      email: document.getElementById("email").value.trim(),
      phone: document.getElementById("phone").value.trim(),
      gender: document.getElementById("gender").value,
      city: document.getElementById("city").value.trim(),
      address: document.getElementById("address").value.trim(),
      membership: document.getElementById("membership").value,
      clinicalHistoryId: document
        .getElementById("clinicalHistoryId")
        .value.trim(),
      birthDate: document.getElementById("birthDate").value,
      contraseña: document.getElementById("contraseña").value,
      termsAccepted: document.getElementById("rememberMe").checked,
    };

    // Validaciones básicas
    let errors = {};

    if (!formData.fullName.match(/^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$/)) {
      errors.fullName = "El nombre solo puede contener letras y espacios";
    }

    if (!formData.documentType) {
      errors.documentType = "Debe seleccionar un tipo de documento";
    }

    if (!formData.documentNumber.match(/^\d{6,10}$/)) {
      errors.documentNumber = "Número de documento inválido (6-10 dígitos)";
    }

    if (!formData.email.match(/^[^\s@]+@[^\s@]+\.[^\s@]+$/)) {
      errors.email = "Correo electrónico inválido";
    }

    if (!formData.phone.match(/^\d{10}$/)) {
      errors.phone = "Número de celular inválido (10 dígitos)";
    }

    if (!formData.gender) {
      errors.gender = "Debe seleccionar un género";
    }

    if (!formData.city) {
      errors.city = "La ciudad no puede estar vacía";
    }

    if (!formData.address) {
      errors.address = "La dirección no puede estar vacía";
    }

    if (!formData.membership) {
      errors.membership = "Debe seleccionar un tipo de membresía";
    }

    if (!formData.clinicalHistoryId.match(/^\d{6,15}$/)) {
      errors.clinicalHistoryId =
        "ID de historial clínico inválido (6-15 dígitos)";
    }

    if (!formData.birthDate) {
      errors.birthDate = "Debe ingresar una fecha de nacimiento";
    }

    if (formData.contraseña.length < 8) {
      errors.contraseña = "La contraseña debe tener al menos 8 caracteres";
    }

    if (!formData.termsAccepted) {
      errors.termsAccepted = "Debe aceptar los términos y condiciones";
    }

    // Mostrar errores en el formulario
    document
      .querySelectorAll(".error-message")
      .forEach((e) => (e.textContent = ""));
    if (Object.keys(errors).length > 0) {
      for (const key in errors) {
        const errorElement = document.getElementById(`${key}Error`);
        if (errorElement) {
          errorElement.textContent = errors[key];
        }
      }
      return;
    }

    // Enviar datos al servidor en formato JSON
    try {
      const response = await fetch("/create/affiliate", {
        method: "GET",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData),
      });

      const result = await response.json();
      if (response.ok) {
        alert("Registro exitoso");
        form.reset();
      } else {
        alert("Error: " + result.message);
      }
    } catch (error) {
      alert("Error en la conexión con el servidor");
      console.error(error);
    }
  });
});
