document.addEventListener('DOMContentLoaded', function() {
    const crearCuentaForm = document.getElementById('crear-cuenta');
    const confirmModal = document.getElementById('confirmModal');
    const orderConfirmedModal = document.getElementById('orderConfirmedModal');
    const confirmBtn = document.getElementById('confirmBtn');
    const cancelBtn = document.getElementById('cancelBtn');
    const closeOrderConfirmedModalBtn = document.getElementById('closeOrderConfirmedModalBtn');
    let orderID = ''; // Aquí deberías establecer el ID del pedido después de que se complete el envío del formulario

    crearCuentaForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Detener el envío del formulario por defecto
        
        // Mostrar la ventana emergente de confirmación de creación de cuenta
        confirmModal.style.display = 'block';
    });

    confirmBtn.addEventListener('click', function() {
        // Ocultar la ventana emergente de confirmación de creación de cuenta
        confirmModal.style.display = 'none';

        // Aquí deberías realizar el envío del formulario y obtener el ID de la cuenta creada
        // orderID = '123456'; // Supongamos que aquí obtenemos el ID de la cuenta creada

        // Mostrar la ventana emergente de confirmación de cuenta creada
        orderConfirmedModal.style.display = 'block';
        // document.getElementById('orderID').innerText = orderID;

    });

    cancelBtn.addEventListener('click', function() {
        // Ocultar la ventana emergente de confirmación de creación de cuenta si el usuario cancela
        confirmModal.style.display = 'none';
    });

    closeOrderConfirmedModalBtn.addEventListener('click', function() {
        // Ocultar la ventana emergente de confirmación de cuenta creada
        orderConfirmedModal.style.display = 'none';
         // Aquí deberías enviar el formulario de creación de cuenta
         crearCuentaForm.submit();
    });
});