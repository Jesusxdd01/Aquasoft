document.addEventListener('DOMContentLoaded', () => {
    const toggles = document.querySelectorAll('.toggle');

    toggles.forEach(toggle => {
        toggle.addEventListener('click', () => {
            const respuesta = toggle.parentNode.nextElementSibling;
            const isVisible = respuesta.style.display === 'block';

            // Cambia la visibilidad de la respuesta
            respuesta.style.display = isVisible ? 'none' : 'block';

            // Obtén la referencia al elemento <img> dentro del botón
            const imgElement = toggle.querySelector('img');

            if (imgElement) {
                // Si hay una imagen dentro del botón, cambia la imagen según la visibilidad
                if (isVisible) {
                    imgElement.src = "../static/img/abajo.png";
                    imgElement.alt = 'Desplegar';
                } else {
                    imgElement.src = "../static/img/arriba.png";
                    imgElement.alt = 'Minimizar';
                }
            }
        });
    });
});

