#11.	Crea una pequeña encuesta con tres preguntas. Almacena las respuestas en variables de tipo string y 
# muestra un resumen final, donde cada línea esté numerada.

pregunta1 = input("Cual es tu color favorito? ")
pregunta2 = input("Cual es tu animal favorito? ")
pregunta3 = input("Cual es tu serie favorita? ")

print(f"""Resumen 
      1.- tu color favorito es: {pregunta1}
      2.- Tu animal favorito es: {pregunta2}
      3.- Tu serie favorita es: {pregunta3}
      """)