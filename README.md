# Recto-Sofka

CHALLENGE SOFKA

Para hacer la logica del concurso se hizo los siguientes pasos:

1. Se llamo la función random la cual me servira para selecionar de forma aleatorea las preguntas

2. Se crearon, las clases Preguntas, Opciones (opciones de respuestas) y Respuestas. Cada clase con su respectiva colección de datos

3. Se definio la funcion menu para dar inicio al juego con la ingresando opción "1"

4. Al seleccionar 1, se da inicio al concurso a traves del concional while.

5. Dentro del condional if se evaluan de forma aleatoria las preguntas con sus respectivas opciones (con random.randint) y si la respuesta es correcta el jugador gana $100 y pasa al siguiente nivel ó categoria de preguntas.

6. Asi continua el programa acorde el punto 5, siempre y cuando el jugador seleccione la respuesta correcta hasta y finaliza en el nivel 5 donde finaliza el juego. 

7. Si el jugador responde mal una pregunta durante el juego se retira sin ningun premio, ó si se quiere retirar de forma voluntaria en cualquier nivel se va con el totalAcumulado