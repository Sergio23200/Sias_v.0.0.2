const ciudadesPorDepartamento = {
  Cundinamarca: ["Bogotá", "Soacha", "Chía", "Zipaquirá"],
  Antioquia: ["Medellín", "Bello", "Envigado", "Itagüí"],
  "Valle del Cauca": ["Cali", "Palmira", "Buenaventura", "Tuluá"],
};

// Seleccionamos los elementos del DOM
const departamentoSelect = document.getElementById("departamento");
const ciudadSelect = document.getElementById("ciudad");

// Evento cuando cambia el departamento
departamentoSelect.addEventListener("change", function () {
  const departamentoSeleccionado = this.value;

  // Limpiar ciudades anteriores
  ciudadSelect.innerHTML = '<option value="">Seleccionar</option>';

  // Verificar si el departamento tiene ciudades
  if (departamentoSeleccionado in ciudadesPorDepartamento) {
    // Agregar las nuevas opciones de ciudad
    ciudadesPorDepartamento[departamentoSeleccionado].forEach((ciudad) => {
      const option = document.createElement("option");
      option.value = ciudad;
      option.textContent = ciudad;
      ciudadSelect.appendChild(option);
    });
  }
});
