#10 de Junio del 2022


print("   CHALLENGE - CONCURSO DE PREGUNTAS Y RESPUESTAS   ")
print("")
print("       Dinamica del concurso      ")
print("")
print("Concurso de preguntas y preguntas, seleccion multiple por categorizadas,")
print("Las preguntas van apareciendo a medida que la respuesta sea correcta,")
print("en total son 5 preguntas y cada pregunta corresponde a un nivel ó categoria")
print("Con cada respuesta correcta el jugador gana $100")
print("si consteta mal el amcumulado se pierde o si decide retirarse el acumulado se mantiene")
print("")

import random

#serie de preguntas
class Preguntas:
    
    categoriaMatematica = ["Para calcular cuánto es un tercio de 3996, ¿qué tienes que hacer? ",
                          "Un perro pesa 20 kilos y un cachorro pesa 10 kilos menos que él, ¿cuánto pesa la cría?",
                          "¿Cuál es el nombre del triángulo que tiene dos lados iguales y uno desigual?",
                          "Cuál es el número anterior a 1000? ",
                          "¿Qué cantidad expresa el número romano V?"]
    
    categoriaHistoria = ["¿Cuál fue el primer metal que el hombre empleó?",
                                 "¿Cómo se les llamaba a los primeros pobladores que se desplazaban en busca de alimento?",
                                 "¿En qué lugar del mundo se dio el origen de la humanidad?",
                                 "¿Cuál de estos cuatro hechos históricos es más antiguo?",
                                 "¿Por qué condenó la Iglesia a Galileo Galilei? "]

    categoriaAnimales = ["¿Cuál de los siguientes animales no es un marsupial?",
                                  "¿El estómago de cuál de estos animales está dividido en cuatro compartimentos?",
                                  "¿De qué color es la piel de un oso polar?",
                                  " ¿Cuál de estos animales puede dormir hasta 22 horas por día?",
                                  "¿Cuál es el carnívoro más grande del planeta?"]
    
    categoriaGeografia = ["¿Cuál es el rió más largo del mundo?",
                         "¿Qué país es el segundo más grande del mundo en términos de población?",
                         "¿Cuántos continentes hay en la Tierra?",
                         "¿Cuántos océanos hay en la Tierra?",
                         "¿Cuál es la parte más seca de la Tierra? "]
    
    categoriaProgramming = ["Cuando hablamos de java, hablamos de un lenguaje...",
                            "Cuando hablamos de python, hablamos de una lenguaje...",
                            "nodejs es un framework o tecnología para... ",
                            "si ves un método con mas de 45 lineas de código, ¿qué puede decir?",
                            "Un full-stack debe conocer... "]
    
    
#Opciones de las preguntas
class Opciones:
    
    opcionesMatematica = ["A. Multiplicar por tres  B. Dividir entre tres  C. Restar tres  D. Sumar tres ",
                         "A.  30kg  B.  5kg C.  8kg  D.	10kg",
                         "A.	isósceles B.	escaleno C.	equilátero D.	hexagono ",
                         "A.	1001 B.	990 C.	1010 D.	999",
                         "A.	ocho B.	diez C.	cinco D.	uno "]
    
    opcionesHistoria = ["A.	La plata B.	El cobre.	El bronce D.	El hierro",
                              "A.	Nómadas   B.	Sedentarios C.	Cavernicolas D.	Dinosaurios ",
                              "A.	America B.	Oceania  C.	20 Europa  D.	África",
                             "A.	Nacimiento de Jesucristo  B.	Nacimiento de Mahoma  C.	Nacimiento de Confucio  D.	Nacimiento de Buda ",
                            "A.	Por decir que la tierra giraba alrededor del sol B.	Por decir que la tierra era el centro del universo C.	Por negar la existencia de Dios D.	Por decir que la tierra era redonda "]
    
    opcionesAnimales = ["A. Koala B.	Oso perezoso C. Zarigueya D. Kanguro",
                                 "A. Cabra B.	Zorro C. Leopardo D. Gato",
                                 "A.	Rosa B. Blanca C.	Negra D. ninguna de las anteriores",
                                 "A.	Lechuza B. Koala C.	Murcielago D. Conejo ",
                                 "A.	Oso polar B.	Tigre C.	Elefante D.	Oso panda "]
    
    opcionesGeografia = ["A. Yangtse B. Rio amarillo C.	Amazonas  D. Nilo",
                        "A.	Rusia B.	China C.	India D. Indonesia ",
                        "A.	4 B.	5 C.	6 D.	11",
                        "A.	4 B.	5 C.	6 D.	2",
                        "A.	America del sur  B.	Africa C.	Asia D.	La Antartida"]
    
    opcionesProgramming = ["A.	Compilado B. No compilado C. Interpretado D. No interpretado",
                          "A.	Compilado B. No compilado C. Interpretado D. No interpretado",
                          "A.	Python B.	Java C.	JavaScript D.	SQL ",
                          "A.	Es un método con mucho código B.	Tiene alta complejidad ciclomática C. Hay malas practicas de programación D.	Tiene baja cohesión",
                          "A.	Solo frontend y backend B. Base de datos y backend C. Frontend y base de datos D. Frontend, backend y base de datos "]

#Respuestas correctas
class Respuestas:
    
    respuestaMatematica = ["B","D","A","D","C"]
    
    respuestaHistoria = ["B","A","D","C","A"]
    
    respuestaAnimales = ["B","A","C","B","A"]
    
    respuestaGeografia = ["D","C","C","B","D"]
    
    respuestaProgramming = ["A","C","C","C","D"]


def menu():
    
    
    print("1. Start Game")
    print("0. End Game")
    menu = input("Ingrese su opción: ")
    return menu

totalAcumulado = 0


while menu()=="1":

    #MATEMATICA
    if(totalAcumulado == 0):
       print("Nivel 1, Categoria - MATEMATICA")
       iten = random.randint(0, 4)
       print(Preguntas.categoriaMatematica[iten])
       print(Opciones.opcionesMatematica[iten])
       print("")
    
       respuesta = input("Ingrese su respuesta en MAYUSCULA: ")
       if(respuesta == Respuestas.respuestaMatematica[iten]):
           print("Respuesta correcta: ", Respuestas.respuestaMatematica[iten])
           totalAcumulado = 100
           print("Total Acumulado: ", totalAcumulado)
       else:
           print("Respuesta incorrecta:",Respuestas.respuestaMatematica[iten])
           totalAcumulado = 0
           break
       
    #HISTORIA
    if(totalAcumulado == 100):
       print("Nivel 2, Categoria - HISTORIA")
       iten = random.randint(0, 4)
       print(Preguntas.categoriaHistoria[iten])
       print(Opciones.opcionesHistoria[iten])
       print("")
    
       respuesta = input("Ingrese su respuesta en MAYUSCULA: ")
       if(respuesta ==  Respuestas.respuestaHistoria[iten]):
           print("Respuesta correcta: ",  Respuestas.respuestaHistoria[iten])
           totalAcumulado = totalAcumulado + 100
           print("Total Acumulado: ", totalAcumulado)
       else:
           print("Respuesta incorrecta:", Respuestas.respuestaHistoria[iten])
           totalAcumulado = 0
           break
       
    #ANIMALES
    if(totalAcumulado == 200):
       print("Nivel 3, Categoria - ANIMALES")
       iten = random.randint(0, 4)
       print(Preguntas.categoriaAnimales[iten])
       print(Opciones.opcionesAnimales[iten])
       print("")
    
       respuesta = input("Ingrese su respuesta en MAYUSCULA: ")
       if(respuesta ==  Respuestas.respuestaAnimales[iten]):
           print("Respuesta correcta: ", Respuestas.respuestaAnimales[iten])
           totalAcumulado = totalAcumulado + 100
           print("Total Acumulado: ", totalAcumulado)
       else:
           print("Respuesta incorrecta:", Respuestas.respuestaAnimales[iten])
           totalAcumulado = 0
           break
       
    #GEOGRAFIA
    if(totalAcumulado == 300):
       print("Nivel 4, Categoria - GEOGRAFIA")
       iten = random.randint(0, 4)
       print(Preguntas.categoriaGeografia[iten])
       print(Opciones.opcionesGeografia[iten])
       print("")
    
       respuesta = input("Ingrese su respuesta en MAYUSCULA: ")
       if(respuesta ==  Respuestas.respuestaGeografia[iten]):
           print("Respuesta correcta: ", Respuestas.respuestaGeografia[iten])
           totalAcumulado = totalAcumulado + 100
           print("Total Acumulado: ", totalAcumulado)
       else:
           print("Respuesta incorrecta:", Respuestas.respuestaGeografia[iten])
           totalAcumulado = 0
           break
       
    #PROGRAMMING
    if(totalAcumulado == 400):
       print("Nivel 5, Categoria - PROGRAMMING")
       iten = random.randint(0, 4)
       print(Preguntas.categoriaProgramming[iten])
       print(Opciones.opcionesProgramming[iten])
       print("")
    
       respuesta = input("Ingrese su respuesta en MAYUSCULA: ")
       if(respuesta ==  Respuestas.respuestaProgramming[iten]):
           print("Respuesta correcta: ", Respuestas.respuestaProgramming[iten])
           totalAcumulado = totalAcumulado + 100
           print("Total Acumulado: ", totalAcumulado)
           break
       else:
           print("Respuesta incorrecta:", Respuestas.respuestaProgramming[iten])
           totalAcumulado = 0
           break 

        
    if(menu()=="0"):
        totalAcumulado = totalAcumulado
        break
    menu()
    
print("Su acumulado fue de: ",totalAcumulado)

















