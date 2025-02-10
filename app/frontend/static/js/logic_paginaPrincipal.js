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

/*funcion para funcionamiento front chatboot*/ 
document.getElementById("chatbot-icon").addEventListener("click", function() {
  let chatContainer = document.getElementById("chat-container");
  
  if (chatContainer.style.display === "flex") {
      chatContainer.style.display = "none";
      document.getElementById("chat-box").innerHTML = ""; // Borra los mensajes anteriores
  } else {
      chatContainer.style.display = "flex";
      
      // Mensaje de bienvenida cuando se vuelve a abrir el chat
      let chatBox = document.getElementById("chat-box");
      let botMessage = document.createElement("div");
      botMessage.classList.add("message", "bot");
      botMessage.textContent = "¡Hola! Soy tu asistente virtual. ¿En qué puedo ayudarte?";
      chatBox.appendChild(botMessage);
  }
});

document.getElementById("send-btn").addEventListener("click", function() {
  let userInput = document.getElementById("user-input").value;
  if (userInput.trim() !== "") {
      let chatBox = document.getElementById("chat-box");
      
      let userMessage = document.createElement("div");
      userMessage.classList.add("message", "user");
      userMessage.textContent = userInput;
      chatBox.appendChild(userMessage);

      let botMessage = document.createElement("div");
      botMessage.classList.add("message", "bot");
      botMessage.textContent = "Gracias por tu mensaje. Te responderé en breve.";
      chatBox.appendChild(botMessage);

      chatBox.scrollTop = chatBox.scrollHeight;
      document.getElementById("user-input").value = "";
  }
});