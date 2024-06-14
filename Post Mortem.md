# Post Mortem: La sombra del Imperio - Guardianes de la paz

## Resumen del Proyecto

**Título del Juego:** La sombra del Imperio - Guardianes de la paz
**Género:** Arcade  
**Plataformas:** PC  
**Fecha de Lanzamiento:** 29/05/2024
**Duración del Proyecto:** 2 meses
**Equipo:** Javier Rubio Roca (programador), ChatGPT (guionista), Dall-E (diseñador gráfico)

## Objetivos Iniciales

- Realizar un videojuego arcade
- Construir una historia divertida

## Logros

### 1. Diseño y Jugabilidad
- **Logro:** Diferentes niveles jugables

### 2. Gráficos y Arte
- **Logro:** Tematica espacial
- **Detalles:** Todos los elementos gráficos encajan con una historia centrada en naves espaciales y estan bien cohesionados entre si.

### 3. Rendimiento y Estabilidad
- **Logro:** Fluidez
- **Detalles:** Se logró un juego fluido en algunos aspectos críticos, como la creación en tiempo real de los enemigos en los primeros niveles estilo space invaders, precargando en la escena anterior todos los objetos de la nave enemiga o en la misma escena si se ha saltado la escena anterior de introducción y habilitando los objetos ya precreados. 

## Desafíos y Problemas

### 1. Gestión del Tiempo
- **Problema:** Poco tiempo para todas las tareas previstas
- **Detalles:** Objetivos demasiado ambiciosos
- **Solución/Acción Tomada:** Se recortaron niveles previstos y no se desarrollo el multijugador.

### 2. Problemas Técnicos
- **Problema:** Dificultad de realizar en multihilo tareas en pygame
- **Detalles:** Crear objetos en tiempo real en programación mononucleo debido a las limitaciones de pygame causaba un juego poco fluido.
- **Solución/Acción Tomada:** Precargar los objetos que realentizan el juego.

- - **Problema:** Rotar las imagenes rotadas en pygame provoca distorsión y realentiza el juego
- **Detalles:** Al rotar multiples veces la imagen rotada, una y otra vez, se van acumulando deformidades y el juego se va realentizando.
- **Solución/Acción Tomada:** Rotar siempre la imagen original a los grados correspondientes.


## Conclusión

En general ha sido una tarea muy divertida y en la que se hace muy visible cuando algo esta programado suboptimamente causando disminución del framerate del juego.


---

Javier Rubio Roca
Estudiante
14/06/2024
