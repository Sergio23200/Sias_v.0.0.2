// Función para alternar la visibilidad del contenido del acordeón
function toggleAccordion(itemId) {
    const item = document.getElementById(itemId);
    const content = item.querySelector('.accordion-content');
    const isVisible = content.style.display === 'block';

    // Cerrar todos los elementos
    const allItems = document.querySelectorAll('.accordion-item');
    allItems.forEach((el) => {
        el.querySelector('.accordion-content').style.display = 'none';
    });

    // Si el elemento estaba cerrado, abrirlo
    if (!isVisible) {
        content.style.display = 'block';
    }
}
