/*  Versión con timer para segunda ventana emergente 
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('formularioPedidos');
    const confirmModal = document.getElementById('confirmModal');
    const orderConfirmedModal = document.getElementById('orderConfirmedModal');
    const confirmBtn = document.getElementById('confirmBtn');
    const cancelBtn = document.getElementById('cancelBtn');
    const closeOrderConfirmedModalBtn = document.getElementById('closeOrderConfirmedModalBtn');
    let orderID = ''; // Aquí deberías establecer el ID del pedido después de que se complete el envío del formulario

    // Controlar el envío del formulario
    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Detener el envío del formulario por defecto
    });

    // Mostrar la ventana emergente de confirmación del pedido al hacer clic en el botón "Pedir"
    form.addEventListener('submit', function(event) {
        confirmModal.style.display = 'block';
    });

    // Si el usuario confirma el pedido, ocultar la ventana de confirmación y mostrar la ventana de confirmación del pedido
    confirmBtn.addEventListener('click', function() {
        confirmModal.style.display = 'none';

        // Aquí deberías realizar el envío del formulario y obtener el ID del pedido
        orderID = '123456'; // Supongamos que aquí obtenemos el ID del pedido

        // Mostrar la ventana emergente de confirmación del pedido
        orderConfirmedModal.style.display = 'block';
        document.getElementById('orderID').innerText = orderID;

        // Envío del formulario después de que el usuario confirma
        setTimeout(function() {
            form.submit();
        }, 3000); // Ajusta el tiempo de espera según sea necesario
    });

    // Si el usuario cancela, simplemente ocultar la ventana de confirmación
    cancelBtn.addEventListener('click', function() {
        confirmModal.style.display = 'none';
    });

    // Si el usuario cierra la ventana de confirmación del pedido, ocultarla
    closeOrderConfirmedModalBtn.addEventListener('click', function() {
        orderConfirmedModal.style.display = 'none';
    });
});

*/

/* Segunda version que es para que quites el redirecionar */
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('formularioPedidos');
    const confirmModal = document.getElementById('confirmModal');
    const orderConfirmedModal = document.getElementById('orderConfirmedModal');
    const confirmBtn = document.getElementById('confirmBtn');
    const cancelBtn = document.getElementById('cancelBtn');
    const closeOrderConfirmedModalBtn = document.getElementById('closeOrderConfirmedModalBtn');
    let orderID = ''; // Aquí deberías establecer el ID del pedido después de que se complete el envío del formulario

    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Detener el envío del formulario por defecto
        
        // Mostrar la ventana emergente de confirmación del pedido
        confirmModal.style.display = 'block';
    });

    confirmBtn.addEventListener('click', function() {
        // Ocultar la ventana emergente de confirmación del pedido
        confirmModal.style.display = 'none';

        // Aquí deberías realizar el envío del formulario y obtener el ID del pedido
        orderID = '123456'; // Supongamos que aquí obtenemos el ID del pedido

        // Mostrar la ventana emergente de confirmación del pedido
        orderConfirmedModal.style.display = 'block';
        document.getElementById('orderID').innerText = orderID;

        

    });

    cancelBtn.addEventListener('click', function() {
        // Ocultar la ventana emergente de confirmación del pedido si el usuario cancela
        confirmModal.style.display = 'none';
    });

    closeOrderConfirmedModalBtn.addEventListener('click', function() {
        // Ocultar la ventana emergente de confirmación del pedido una vez que se confirma el pedido
        orderConfirmedModal.style.display = 'none';
         
        // Aquí deberías enviar el formulario
        form.submit();
    });
});
