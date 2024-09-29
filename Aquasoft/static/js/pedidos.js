function actualizarPrecio() {
    var productoId = document.getElementById('producto_id').value;
    fetch(`/obtener_precio/?producto_id=${productoId}`)
        .then(response => response.json())
        .then(data => {
            if (data.precio) {
                document.getElementById('precioUnitario').value = data.precio;
                calcularTotal();
            } else {
                console.error('No se pudo obtener el precio del producto');
            }
        })
        .catch(error => console.error('Error al obtener el precio:', error));
}

// Ejecutar la función actualizarPrecio cuando se cambie la selección del producto
document.getElementById('producto_id').addEventListener('change', actualizarPrecio);

// Ejecutar la función actualizarPrecio al cargar la página para obtener el precio inicial
window.onload = actualizarPrecio;


// Función para calcular el total en tiempo real mientras el usuario ingresa la cantidad o el precio unitario
function calcularTotal() {
    // Obtenemos el valor de cantidad y el factor (precio unitario)
    var factor = parseFloat(document.getElementById('precioUnitario').value);
    var cantidad = parseFloat(document.getElementById('cantidad').value);

    // Verificamos que ambos valores sean números válidos
    if (!isNaN(cantidad) && !isNaN(factor)) {
        // Multiplicamos cantidad por factor
        var total = cantidad * factor;

        // Mostramos el resultado en la etiqueta con id 'total'
        document.getElementById('total').value = total;
    } else {
        // Si alguno de los valores no es un número válido, mostramos un mensaje de error
        document.getElementById('total').value = 'Error: Valor no numérico';
    }
}

// Asignamos la función calcularTotal al evento input de los campos cantidad y precio unitario
document.getElementById('cantidad').addEventListener('input', calcularTotal);
document.getElementById('precioUnitario').addEventListener('input', calcularTotal);