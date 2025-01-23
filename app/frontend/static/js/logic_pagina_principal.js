//capturar elementos del DOM
const botonBuscar = document.getElementById("boton-ir");
const barraBusqueda = document.getElementById("search");

// Acción al hacer clic en el botón de búsqueda
botonBuscar.addEventListener("click", (e) => {
    e.preventDefault(); // Evita que el enlace recargue la página
    const query = barraBusqueda.value.trim(); // Obtén el valor de la barra de búsqueda
    if (query) {
      alert(`Buscando: ${query}`); // Muestra un mensaje con la búsqueda
    } else {
      alert("Por favor, escribe algo para buscar."); // Mensaje si la barra está vacía
    }
  });