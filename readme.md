# Proyecto Final Bootcamp "Aprende a Programar desde 0" por Cristina Rodríguez
## Información General
***
A continuación, presento mi prototipo de aplicación para la consulta y compra de criptomonedas con dinero ficticio.

El balance del que dispones es indefinido y este es en euros(€). Podrás intercambiar criptos entre ellas si la moneda de origen ha sido comprada con euros previamente. 


## Instalación 

```
1. Tendrás que clonar el repositorio de GitHub para que aparezca tu terminal. Puedes hacerlo de dos formas:
```
Opción 1: Creando un nuevo repositorio en remoto en GitHub:
> git remote add origin https://github.com/Crispy96/Project.git
```
```
Opción 2 Copiandolo directamente:
> git clone https://github.com/Crispy96/Project.git
```


2. En el fichero requierments.txt encontraras los programas necesarios para su ejecución. Estos los podrás installar directamente a través del siguente comando.
```
> pip install -r requierments.txt
```


## Ejecución
*** 
Tras instalar todo lo dicho arriba deberás cambiar algunos fichero y añadir otros para el correcto funcionamiento de la aplicación.
1. Tendrás que modificar el nombre del archivo config_template.py por **config.py**. También deberás de modifciar su contenido segun lo que explico más abajo.

![Image text](project/static/image/config.PNG)
***
Además deberás de modificar los siguentes campos:

>ROUTE_DATA_BASE--> Deberás escribir la ruta para acceder a tu base de datos

>SECRET_KEY --> Clave secreta (la que tu quieras)

>apikey --> Tendrás que escribir tu apikey, si todavía no dispones de una la puedes obtener en el siguente enlace: https://www.coinapi.io/pricing?apikey

2. El archivo .env_template deberá de ser renombrado a **.env** y modificado así:
![Image text](project/static/image/.env.PNG)
>FLASK_ENV--> deberá modificar su contenido por **development**.
