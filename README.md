# Proyecto Homebanking con Django

- [Configuración del proyecto](#instalación-del-proyecto)
- [Problematicas del Sprint](#problematicas-sprint-7)
  - [Crear Modelos](#1°-problemática---crear-modelo)
  - [Crear Vistas](#2°-problemática---crear-vistas)
  - [Autenticación](#3°-problemática---autenticación)
  - [Formularios](#4°-problemática---formulario)

## Instalación del proyecto

- Clonar el repositorio, acceder a la carpeta, y crear un entorno virtual.

```bash
  git clone https://github.com/AgusT613/itba_full_stack_django.git

  cd itba_full_stack_django

  python -m venv .venv
```

- Archivos del proyecto:

  - itbank_full_stack_django/

    - homebanking/
      - clientes/
      - cuentas/
      - empleado/
      - homebanking/ (main)
      - login/
      - movimientos/
      - prestamos/
      - tarjetas/
      - manage.py
    - .gitignore
    - README.md
    - requirements.txt

- Una vez hecho, acceder al instalador de paquetes de python (pip) desde el entorno virtual creado.

```bash
  source .venv/bin/activate
```

- Ahora se pueden instalar todos los paquetes necesarios para el proyecto desde el archivo `requirements.txt` usando el entorno virtual.

```bash
  pip install -r requirements.txt
```

- Acceder a la carpeta del proyecto `homebanking` y crear los modelos de Django y aplicarlos a la base de datos (sqlite3)

```bash
  cd homebanking

  python manage.py makemigrations

  python manage.py migrate
```

- Por último, arrancar el servidor de desarrollo:

```bash
  python manage.py runserver
```

## Problematicas Sprint 7

### 1° Problemática - Crear Modelo

Este sprint se basa en el modelo de bases datos desarrollado en el sprint 6

- Aplicaciones del proyecto:
  - Clientes
  - Cuentas
  - Tarjetas
  - Movimientos
  - Prestamos
  - Login
  - Otros...

### 2° Problemática - Crear Vistas

Luego de haber creado el modelo de nuestro home banking, nos vamos a
dedicar a crear las vistas que van a dar soporte cuando sean requeridas
por la interfaz de front-end

Teniendo en cuenta que las interacciones de la interfaz requerirán vistas,
desarrollar todas las necesarias, por ejemplo, una vista para mostrar datos
de un cliente, una vista para crear una cuenta bancaria, una vista para listar
todas las cuentas de un cliente, una vista para mostrar todas las tarjetas de
un cliente, etc.

### 3° Problemática - Autenticación

- Se necesita generar una relación entre el usuario que se autentica y
  la información de cliente almacenada. Debería haber una relación 1 a
  1 entre cliente y usuario.
- La construcción deberá permitir que se pueda agregar al menú del
  home banking la opción de salir o cerrar sesión
- Una vez autenticado el usuario, el home banking debe mostrar su
  nombre en algún lugar del sitio.
- Todas las páginas del sitio van a tener que chequear que el usuario
  esta autenticado.

### 4° Problemática - Formulario

- Crear aplicación prestamos en el proyecto.
- Crear un formulario solicitud de prestamos preaprobados con protección contra Cross Site Request Forgery
- El cliente debe autenticarse para precargar sus datos
- El cliente debe poder elegir el tipo de prestamo y la fecha de inicio
- Los montos de preaprobacion dependen del tipo de cliente
  - Black: $500.000
  - Gold: $300.000
  - Classic: $100.000
- Registrar la solicitud en la base de datos
- Notificar si la solicitud fue aprobada o rechazada
