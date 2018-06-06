# P3 BDD test Verificacion
## Enunciado
Crea una web sencilla usando [Django] o [Flask]

Esta web deberá de tener un formulario muy sencillo con:

-   Un charfield en el que podrás escribir la URL de la página que se quiere aplicar el contador
-   Dos botones:
    -   Reset: borra todo lo que haya en el charfield
    -   Execute: Arranca el proceso cálculo de palabras de todos los textos de la URL que sean elmentos html "p"
-   Un textfield/lista que muestra las palabras y el número de apariciones de las mismas
-   Un textfield/lista que muestra las palabras y el número de apariciones de las mismas que se encuentran en BBDD a lo largo del día

El funcionamiento de la web es sencillo:

-   Un usuario (no hace falta login/registro/etc) puede introducir una URL en el charfield
-   Si el usuario pulsa el botón Reset la URL que haya en charfield deberá de desaparecer. En caso de que no hubiera URL escrito el botón Reset no deberá de hacer nada.
-   Si el usuario pulsa el botón Execute y hay texto, la web deberá de mostrar por pantalla un listado con las palabras y el número de apariciones ordenadas de mayor a menor, por otro lado, mostrará por pantalla otro listado con las palabras y el número de apariciones ordenadas de mayor a menor que se encuentren en BBDD a lo largo de ese día y, de igual forma, deberá de borrarse la URL que aparece en el charfield. En caso de que no hubiera ninguna URL el botón no tendrá ningún efecto.
## Software
En esta practica hemos trabajado con Python 3.6, por este motivo, aunque se pedia que la automatización de los test se hiciera con [lettuce], debido a que este software ya no es soportado por Python3, hemos optado por utilizar [aloe]
## Base de datos
En cuanto a la base de datos hemos decidido implementar una base de datos no relacional, en este caso es Redis.
## Librerias necesarias:
 1. django 
 2. aloe 
 3. aloe-django
 4. nose 
 5. django-nose 
 6. django-nose-selenium 
 7. selenium
 8. beautifulsoup4
 9. redis
 10. DateTime
 11. requests
 12. numpy
    
## Para que funcione:
- Es necesario el archivo "chromedriver.exe", este archivo se encuentra ya incluido en el proyecto y corresponde a una arquitectura win32, si tu SO no es windows, entra en el [link], descarga la version que se ajuste a tu ordenador e incluye este archivo en la siguiente ruta
		
		 F:\*\Practica3_BDD_Verificacion-master\P3Verificacion\Apps\Web\test_automated\
- Ir a features/browser.py 
- Poner la ruta de chromedriver.exe
			
			e.g. driver = webdriver.Chrome(r'F:\*\Practica3_BDD_Verificacion-master\P3Verificacion\Apps\Web\test_automated\chromedriver.exe')
	
## Ejecución:

- Abrir la terminal e ir hasta el directorio del proyecto y escribir
		
		(venv) F:\*\Practica3_BDD_Verificacion-master> python manage.py runserver

### MANUALMENTE:
 - Abrir el navegador y escribir la ruta
 	 
		localhost:8000/Practica/contador
### AUTOMATIZADO: 
- Abrir otra terminal e ir hasta el directorio test_automated y escribir:

		(venv) F:\*\Practica3_BDD_Verificacion-master\P3Verificacion\Apps\Web\test_automated> aloe
### Test Unitarios:
- Abrir otra terminal e ir hasta este directorio y escribir:
		
		(venv) F:\*\P3_BDD-master\Practica3_BDD_Verificacion-master> python manage.py test P3Verificacion.Apps
        
## Equipo Desarrollo
1. [Sergio Blanco]
2. [Sergio Cuesta]
3. [Miguel Muñiz]
4. [Miguel Olmedo]

## Version
    V2.0

[Sergio Blanco]: https://github.com/sergioBMPN
[Sergio Cuesta]:https://github.com/scj300
[Miguel Muñiz]: https://github.com/miguelmuniz46
[Miguel Olmedo]: https://github.com/MiguelOlmedo
[Django]:https://www.djangoproject.com
[Flask]:http://flask.pocoo.org/
[link]:https://chromedriver.storage.googleapis.com/index.html?path=2.38/
[lettuce]:http://lettuce.it/
[Aloe]:https://pypi.org/project/aloe/
