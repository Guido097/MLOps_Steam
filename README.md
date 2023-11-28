# MLOps-ProyectoIndividual
##  Steam Games API 

Esta API proporciona información sobre los juegos de Steam, incluyendo géneros, especificaciones, fechas de lanzamiento, puntuaciones y más. Puedes utilizar esta API para obtener datos relevantes sobre los juegos lanzados en diferentes años.

## Endpoints Disponibles

/PlayTimeGenre/{genero} : Obtiene el año de lanzamiento de juegos con mayor cantidad de horas jugadas.

/UserForGenre/{genero} : Devuelve el nombre del jugador con mayor cantidad de horas jugadas para el genero ingresado.

/UsersRecommend/{anio} : Devuelve un listado con los 3 juegos mejor recomendados por los usuarios para el año ingresado.

/worst_developers/{year} : Devuelve un listado con los 3 desarrolladores con los juegos menos recomendados para el año ingresado.

/SentimentAnalysis/{developer} : Obtiene el sentimiento de las reviews de los usuarios para la empresa desarrolladora especificada.

/recomendacion_juego/{id_producto} : Devuelve los nombres de los juegos con similitudes al que se ingresó a través de su id de producto.

## Uso de la API

Para utilizar la API, simplemente realiza una solicitud GET a los diferentes endpoints mencionados anteriormente. Para esto deberás proporcionar, a través de la URL de la API o a través de su documentación, la información requerida para que se ejecuten los diferentes endpoints antes mencionados.

## Instalación y Ejecución en LocalHost.

-Clona el repositorio:

'git clone <https://github.com/Guido097/ProyectoInd_1>'

-Instala las dependencias con el comando:

'pip install -r requirements.txt'

-Ejecuta la aplicación con el comando:

'uvicorn main:app --reload'


# Notas

-Asegúrate de tener Python 3.x instalado.

-La API utiliza el paquete FastAPI y requiere la instalación de las dependencias especificadas en requirements.txt.

-Algunos endpoints pueden requerir un año válido como parámetro en la URL.


## Ejecución en el deploy en Render.

Para ejecutar la API y poder probar cada una de las funciones debes entrar en la URL <https://proyectoindividualnro1.onrender.com>.

## Video

Enlace del video <https://youtu.be/GdwTaNxkiQA>


