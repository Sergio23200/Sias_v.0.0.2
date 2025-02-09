//capturar elementos del DOM
const botonBuscar = document.getElementById("boton-ir");
const barraBusqueda = document.getElementById("search");

// Acción al hacer clic en el botón de búsqueda
function buscarPalabra(event) {
  event.preventDefault(); // Evita que la página se recargue
  let palabra = document.getElementById("search").value.trim();
  if (palabra === "") return;

  // Remover resaltado previo
  let elementosResaltados = document.querySelectorAll(".resaltado");
  elementosResaltados.forEach(el => el.classList.remove("resaltado"));
  
  let regex = new RegExp("(" + palabra + ")", "gi");
  let encontrado = false;

  document.querySelectorAll("p, h1, h2, h3, h4, h5, h6, li, span, div").forEach(el => {
      if (el.textContent.match(regex)) {
          el.innerHTML = el.innerHTML.replace(regex, "<span class='resaltado'>$1</span>");
          if (!encontrado) {
              encontrado = true;
              el.scrollIntoView({ behavior: "smooth", block: "center" });
          }
      }
  });
}


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