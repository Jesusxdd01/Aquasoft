
function alternarMapas() {
    const contenedorMapa = document.querySelector('.contenedor-mapa');
    const contenedorMapa2 = document.querySelector('.contenedor-mapa2');

    if (window.innerWidth >= 768) {
        contenedorMapa.style.display = 'block';
        contenedorMapa2.style.display = 'none';
    } else {
        contenedorMapa.style.display = 'none';
        contenedorMapa2.style.display = 'block';
    }
}

window.addEventListener('load', alternarMapas);
window.addEventListener('resize', alternarMapas);
