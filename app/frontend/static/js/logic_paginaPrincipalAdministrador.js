document.addEventListener("DOMContentLoaded", function () {
  // Seleccionar elementos del DOM
  const adminName = document.getElementById("admin-name");
  const adminEmail = document.getElementById("admin-email");
  const adminRole = document.getElementById("admin-role");

  const cerrarSesionBtn = document.getElementById("cerrar-sesion");

  // Función para cerrar sesión
  if (cerrarSesionBtn) {
    cerrarSesionBtn.addEventListener("click", function (event) {
      event.preventDefault();
      if (confirm("¿Está seguro de que desea cerrar sesión?")) {
        alert("Cerrando sesión...");
        window.location.href = "inicio_sesion.html";
      }
    });
  } else {
    console.error("Botón de cerrar sesión no encontrado.");
  }

  // Función para cargar datos del administrador desde la API en la parte Nombre admin
  async function cargarDatosAdmin() {
    try {
      const response = await fetch("https://api.ejemplo.com/admin", {
        // Reemplaza con tu API real
        method: "GET",
        headers: { "Content-Type": "application/json" },
        credentials: "include", // Asegura que se envíen cookies de sesión si es necesario
      });

      if (!response.ok) {
        throw new Error("Error en la solicitud: " + response.status);
      }

      const datosAdmin = await response.json();
      adminName.textContent = datosAdmin.nombre || "Administrador Ejemplo";
      adminEmail.textContent =
        "Correo: " + (datosAdmin.correo || "admin@example.com");
      adminRole.textContent =
        "Rol: " + (datosAdmin.rol || "Super Administrador");
    } catch (error) {
      console.error("Error cargando datos del administrador:", error);
    }
  }

  cargarDatosAdmin();
});

/*manejo carrusel */
let index = 0;
function moverCarrusel(direction) {
  const slides = document.querySelectorAll(".carrusel-slide");
  index += direction;
  if (index < 0) index = slides.length - 1;
  if (index >= slides.length) index = 0;
  slides.forEach((slide, i) => {
    slide.style.display = i === index ? "block" : "none";
  });
}

// Iniciar carrusel en la primera imagen
document.addEventListener("DOMContentLoaded", () => {
  moverCarrusel(0);

  // Autoplay: cambiar de imagen cada 3 segundos
  setInterval(() => moverCarrusel(1), 3000);
});
