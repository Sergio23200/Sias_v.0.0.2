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


  let indice = 0;

function moverCarrusel(direccion) {
  const slides = document.querySelectorAll(".carrusel-slide");
  const totalSlides = slides.length;

  indice += direccion;

  if (indice < 0) {
    indice = totalSlides - 1;
  } else if (indice >= totalSlides) {
    indice = 0;
  }

  const desplazamiento = -indice * 100 + "%";
  document.querySelector(".carrusel-contenedor").style.transform = `translateX(${desplazamiento})`;
}


/* evento para realizar desplazamiento cada 3 segundos */
setInterval(() => moverCarrusel(1), 3000);