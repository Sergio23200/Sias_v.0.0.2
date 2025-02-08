document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("form-medicamentos");

    // Referencias a los elementos del formulario y mensajes de error
    const medicamentosInput = document.getElementById("medicamentos");
    const medicamentosError = document.getElementById("orden_error");
    const emailInput = document.getElementById("email");
    const emailError = document.getElementById("emailError");
    const direccionInput = document.getElementById("direccion");
    const direccionError = document.getElementById("direccion_error");

    // Función para mostrar errores
    function mostrarError(elementoError, mensaje) {
        elementoError.textContent = mensaje;
    }

    function limpiarError(elementoError) {
        elementoError.textContent = "";
    }

    // Validar medicamentos
    function validarMedicamentos() {
        limpiarError(medicamentosError);
        if (medicamentosInput.value.trim() === "") {
            mostrarError(medicamentosError, "La orden de medicamentos es obligatoria.");
            return false;
        }
        return true;
    }

    // Validar email
    function validarEmail() {
        limpiarError(emailError);
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (emailInput.value.trim() === "") {
            mostrarError(emailError, "El correo electrónico es obligatorio.");
            return false;
        }
        if (!emailRegex.test(emailInput.value)) {
            mostrarError(emailError, "El formato del correo electrónico no es válido.");
            return false;
        }
        return true;
    }

    // Validar dirección
    function validarDireccion() {
        limpiarError(direccionError);
        const direccionRegex = /^[A-Za-z0-9ñÑáéíóúÁÉÍÓÚ#.,\s-]{5,100}$/;
        if (direccionInput.value.trim() === "") {
            mostrarError(direccionError, "La dirección no puede estar vacía.");
            return false;
        }
        if (!direccionRegex.test(direccionInput.value.trim())) {
            mostrarError(direccionError, "La dirección ingresada no es válida.");
            return false;
        }
        return true;
    }

    // Evento submit del formulario
    form.addEventListener("submit", async (event) => {
        event.preventDefault(); // Evitar el envío predeterminado

        // Ejecutar validaciones
        const medicamentosValidos = validarMedicamentos();
        const emailValido = validarEmail();
        const direccionValida = validarDireccion();

        if (!medicamentosValidos || !emailValido || !direccionValida) {
            return; // Si alguna validación falla, no se envía el formulario
        }

        // Crear objeto JSON con los datos del formulario
        const datosJSON = {
            medicamentos: medicamentosInput.value.trim(),
            email: emailInput.value.trim(),
            direccion: direccionInput.value.trim(),
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
            localStorage.setItem("medicamentos", datosJSON.medicamentos);
            localStorage.setItem("email", datosJSON.email);
            localStorage.setItem("direccion", datosJSON.direccion);

            alert("Orden enviada correctamente.");
            window.location.href = "confirmacion.html"; // Redirigir a página de confirmación

        } catch (error) {
            console.error("Error en la solicitud:", error);
            alert("Hubo un problema con el envio de la orden.");
        }
    });
});
