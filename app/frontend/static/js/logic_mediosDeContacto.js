function toggleCard(cardId) {
    // Capturar el DOM de cada cars
    const cardInfo = document.getElementById(cardId);

    // Alterna la visibilidad del contenido de la tarjeta
    if (cardInfo.classList.contains('hidden')) {
        cardInfo.classList.remove('hidden');
        cardInfo.innerHTML = getCardDetails(cardId);
    } else {
        cardInfo.classList.add('hidden');
        cardInfo.innerHTML = 'Haz clic para ver más...';
    }
}

// Detalles de cada tarjeta
function getCardDetails(cardId) {
    switch (cardId) {
        case 'telefono':
            return '<strong>comunicate al => </strong> <br> +57 604 01 01 <br> Horarios: Lunes a Viernes, 8:00 AM - 4:00 PM';
        case 'correo':
            return '<strong>Envíanos tus PQRS al email:</strong> <br> epsSura@gmail.com <br> Responderemos en un lapso de 48 horas maximo.';
        case 'social':
            return '<strong>Síguenos en nuestras redes sociales:</strong> <br> Facebook: @EPSSaludSura <br> Instagram: @EPSSaludSura_Oficial';
        default:
            return '';
    }
}
