# Aquasoft
Aquasoft es una página web diseñada para una empresa purificadora de agua que se especializa en la venta de garrafones de agua. Esta plataforma permite a los clientes realizar pedidos en línea, contactarse con la empresa y obtener información sobre los puntos de venta. 

## Funcionalidades
### Sección de Clientes
-   **Inicio:** Página principal con información sobre la empresa y sus servicios.
-   **Contacto:** Formulario de contacto para que los clientes se comuniquen con la empresa.
-   **Puntos de Venta:** Información sobre los diferentes puntos de venta donde los clientes pueden adquirir los productos.
-   **Blog:** Sección con artículos relacionados con el agua purificada, salud y sostenibilidad.
-   **Productos:** Visualización de los productos disponibles (garrafones) y la opción de realizar pedidos.
-  **Mi Cuenta:** Los usuarios registrados pueden ver y gestionar sus pedidos desde esta sección.

### Módulo de Administración
-   **Gestión de Usuarios:** Control de las cuentas de usuarios registrados.
-   **Gestión de Ventas:** Visualización y administración de las ventas realizadas a través de la plataforma.

## Instalación
Para instalar y ejecutar Aquasoft localmente, sigue los siguientes pasos:
###   Requisitos Previos
- Python 3.x
-    Django 4.x
-    Base de datos (SQLite)
-    Pip para gestionar dependencias

### Instrucciones  
   1. Clona el repositorio:
		  git clone https://github.com/usuario/aquasoft.git
		  cd aquasoft
      
   2. Crea un entorno virtual e instala las dependencias:
		  python -m venv env
		  source env/bin/activate  # Para Linux/Mac
		  env\Scripts\activate  # Para Windows
		  pip install -r requirements.txt
      
   3. Configura la base de datos y realiza las migraciones:
      	python manage.py migrate
        
   4. Inicia el servidor de desarrollo:
      	python manage.py runserver
      
   5. Abre tu navegador y accede a http://127.0.0.1:8000 para ver la página.

## Uso
### Clientes
Los clientes pueden navegar por la página, ver los productos disponibles y realizar pedidos en la sección "Mi cuenta". Pueden ponerse en contacto con la empresa a través del formulario de contacto o consultar los puntos de venta.

### Administradores
Los administradores pueden acceder al módulo de administración para gestionar los usuarios y las ventas.

## Licencia
Este proyecto está licenciado bajo la Licencia Pública General Afero, versión 3 (AGPLv3). Esto significa que:
- Puedes utilizar, modificar y distribuir el código del proyecto siempre que respetes los términos de la licencia.
- Cualquier uso del código para proporcionar un servicio en línea debe compartir también el código fuente resultante, incluidos los cambios realizados.
- No está permitido el uso comercial del código sin cumplir con los términos de la AGPLv3.
- Para más detalles, puedes revisar el archivo LICENSE en este repositorio o visitar Licencia AGPLv3.
      
