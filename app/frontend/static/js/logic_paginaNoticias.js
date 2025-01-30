let currentSlide = 0;

function moveSlide(step) {
    const items = document.querySelectorAll('.carousel-item');
    const totalSlides = items.length;

    currentSlide = (currentSlide + step + totalSlides) % totalSlides;
    const newTransformValue = -currentSlide * 100;
    
    document.querySelector('.carousel-container').style.transform = `translateX(${newTransformValue}%)`;
}
