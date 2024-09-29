document.addEventListener('DOMContentLoaded', function() {
    const confirmModal = document.getElementById('confirmModalSesion');
    const confirmBtn = document.getElementById('confirmBtnSesion');
    const cancelBtn = document.getElementById('cancelBtnSesion');
    const navBar = document.querySelector('.nav-bar');
    const bars = document.querySelector('.bars');

    // Elementos de cierre de sesión
    const logoutLinks = document.querySelectorAll('#logoutLink, #logoutLinkSubmenu');

    // Función para mostrar el modal de confirmación
    function showConfirmModal(event) {
        event.preventDefault();
        confirmModal.style.display = 'block';

        // Minimizar el menú desplegable si está abierto
        if (navBar.classList.contains('active')) {
            navBar.classList.remove('active');
        }
    }

    // Agregar el evento de clic a los enlaces de cierre de sesión
    logoutLinks.forEach(link => {
        link.addEventListener('click', showConfirmModal);
    });

    // Confirmar el cierre de sesión
    confirmBtn.addEventListener('click', function() {
        confirmModal.style.display = 'none';
        window.location.href = logoutUrl; // Usar la variable de JavaScript con la URL de cierre de sesión
    });

    // Cancelar el cierre de sesión
    cancelBtn.addEventListener('click', function() {
        confirmModal.style.display = 'none';
    });

    // Cerrar el modal si se hace clic fuera de él
    window.addEventListener('click', function(event) {
        if (event.target == confirmModal) {
            confirmModal.style.display = 'none';
        }
    });
});
