document.addEventListener("DOMContentLoaded", function() {
    const sections = document.querySelectorAll('section');
    sections.forEach((section) => {
        section.addEventListener('click', () => {
            section.classList.toggle('active');
            section.classList.contains('active') ? section.style.backgroundColor = '#d9f7ff' : section.style.backgroundColor = 'white';
        });
    });
});