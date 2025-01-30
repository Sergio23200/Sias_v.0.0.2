//funcion para manejo de menu hamburguesa 
function toggleMenu() {
    const menu = document.getElementById("menuOptions");
    if (menu.style.display === "block") {
        menu.style.display = "none"; // Oculta el menú si ya está visible
    } else {
        menu.style.display = "block"; // Muestra el menú si está oculto
    }
}