# Seguimiento 1: Repaso Python
# Nombre: Juliana Ramírez Molina
# Fecha: 17/11/24 
# Descripción: Este archivo contiene una serie de ejercicios prácticos sobre 
#              listas y funciones en Python. El objetivo es ayudarme, como 
#              estudiante con experiencia previa en Java, a comprender y aplicar 
#              los conceptos fundamentales de las listas en Python, destacando 
#              sus similitudes y diferencias con las estructuras en Java. 

# Ejercicio 1: Crear una lista con los nombres de 5 frutas colombianas favoritas y mostrarla por pantalla.
# Creamos una lista con cinco frutas de Colombia
frutas = ["Piña", "Coco", "Mango", "Chontaduro", "Banano"]
# Imprimimos la lista completa en pantalla
print("Lista de frutas colombianas favoritas:", frutas)


# Ejercicio 2: Acceder al segundo y cuarto elemento de la lista anterior e imprimirlos.
# Accedemos al segundo elemento de la lista
segunda_fruta = frutas[1]
# Accedemos al cuarto elemento de la lista (índice 3)
cuarta_fruta = frutas[3]
# Mostramos los elementos seleccionados
print("La segunda fruta es:", segunda_fruta)
print("La cuarta fruta es:", cuarta_fruta)


# Ejercicio 3: Crear una lista con los números del 1 al 10 y mostrar su longitud.
# Creamos una lista con los números del 1 al 10
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
# Calculamos la longitud de la lista utilizando la función `len()`
longitud = len(numeros)
# Mostramos la longitud de la lista
print("Lista de números del 1 al 10:", numeros)
print("La longitud de la lista es:", longitud)


# Ejercicio 4: Concatenar las dos listas creadas en los ejercicios 1 y 3.
lista_concatenada = frutas + numeros  # Usamos el operador + para concatenar las dos listas
print("Lista concatenada:", lista_concatenada)


# Ejercicio 5: Modificar el tercer elemento de la lista del ejercicio 4 al valor 100.
lista_concatenada[2] = 100  # Modificamos el elemento en el índice 2 (el tercer elemento)
print("Lista después de modificar el tercer elemento:", lista_concatenada)


# Ejercicio 6: Borrar el último elemento de la lista del ejercicio 4.
lista_concatenada.pop()  # El método pop elimina el último elemento de la lista
print("Lista después de borrar el último elemento:", lista_concatenada)


# Ejercicio 7: Crear una lista con 3 números enteros y multiplicar cada elemento por 5.
numeros_enteros = [1, 2, 3]  # Creamos una lista con 3 números enteros
numeros_multiplicados = [x * 5 for x in numeros_enteros]  # Usamos comprensión de listas para multiplicar por 5
print("Lista con elementos multiplicados por 5:", numeros_multiplicados)


# Ejercicio 8: Crear dos listas con 5 números enteros cada una y multiplicar los elementos correspondientes de ambas listas.
lista1 = [1, 2, 3, 4, 5]  # Primera lista con 5 números
lista2 = [6, 7, 8, 9, 10]  # Segunda lista con 5 números
resultado_multiplicacion = [a * b for a, b in zip(lista1, lista2)]  # Multiplicamos los elementos correspondientes de ambas listas
print("Resultado de multiplicar los elementos correspondientes de ambas listas:", resultado_multiplicacion)


# Ejercicio 9: Crear una lista de listas anidadas y acceder al segundo elemento de la segunda lista.
listas_anidadas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Lista de listas
segundo_elemento_segunda_lista = listas_anidadas[1][1]  # Accedemos al segundo elemento de la segunda lista
print("El segundo elemento de la segunda lista es:", segundo_elemento_segunda_lista)


# Ejercicio 10: Crear una lista a partir de la lista del ejercicio 3, tomando los elementos del índice 2 al 6.
sublista = numeros[2:7]  #Tomamos los elementos de los índices 2 a 6
print("Sublista de los elementos del índice 2 al 6:", sublista)


# Ejercicio 11: Usar el método `.append()` para agregar un nuevo elemento al final de la lista del ejercicio 1.
frutas.append("Guayaba Agria")  # Usamos el método append para agregar "Guayaba Agria" al final de la lista
print("Lista de frutas después de agregar un nuevo elemento:", frutas)


# Ejercicio 12: Usar el método `.insert()` para agregar un nuevo elemento en la posición 2 de la lista del ejercicio 3.
numeros.insert(2, 99)  # Usamos insert para agregar el número 99 en la posición 2
print("Lista de números después de insertar un nuevo elemento en la posición 2:", numeros)


# Ejercicio 13: Usar el método `.remove()` para eliminar un elemento específico de la lista del ejercicio 7.
numeros_multiplicados.remove(10)  # Usamos remove para eliminar el número 10 de la lista
print("Lista después de eliminar el número 10:", numeros_multiplicados)


# Ejercicio 14: Usar el método `.reverse()` para invertir el orden de la lista del ejercicio 4.
lista_concatenada.reverse()  # Usamos reverse para invertir el orden de la lista
print("Lista invertida:", lista_concatenada)


# Ejercicio 15: Usar el método `.sort()` para ordenar de forma ascendente la lista del ejercicio 7.
numeros_multiplicados.sort()  # Usamos sort para ordenar la lista de menor a mayor
print("Lista de números multiplicados ordenada:", numeros_multiplicados)


# Ejercicio 16: Usar el método `.pop()` para eliminar y obtener el último elemento de la lista del ejercicio 4.
ultimo_elemento = lista_concatenada.pop()  # Usamos pop para eliminar y guardar el último elemento
print("Último elemento eliminado:", ultimo_elemento)
print("Lista después de eliminar el último elemento:", lista_concatenada)


# Ejercicio 17: Usar el método `.count()` para contar cuántas veces aparece un elemento específico en la lista del ejercicio 7.
cantidad_de_15 = numeros_multiplicados.count(15)  # Usamos count para contar cuántas veces aparece 25
print("El número 15 aparece en la lista:", cantidad_de_15)


# Ejercicio 18: Usar el método `.index()` para obtener el índice de un elemento específico en la lista del ejercicio 4.
indice_elemento = lista_concatenada.index(1)  # Usamos index para obtener el índice del valor 1
print("El índice del elemento 1 es:", indice_elemento)


# Ejercicio 19: Usar el método `.clear()` para eliminar todos los elementos de la lista del ejercicio 1.
frutas.clear()  # Usamos clear para eliminar todos los elementos de la lista
print("Lista de frutas después de usar `.clear()`:", frutas)


# Ejercicio 20: Crear una lista vacía y utilizar un bucle `for` para agregar los números del 1 al 10.
numeros_vacios = []  # Creamos una lista vacía
for i in range(1, 11):  # Usamos un bucle for para agregar los números del 1 al 10
    numeros_vacios.append(i)
print("Lista con los números del 1 al 10:", numeros_vacios)


# Ejercicio 21: Crear una lista de números enteros y utilizar un bucle `while` para eliminar los elementos impares.
numeros_enteros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Lista de números
i = 0
while i < len(numeros_enteros):  # Usamos un bucle while para recorrer la lista
    if numeros_enteros[i] % 2 != 0:  # Si el número es impar
        numeros_enteros.remove(numeros_enteros[i])  # Lo eliminamos
    else:
        i += 1  # Si no es impar, seguimos con el siguiente número
print("Lista después de eliminar los números impares:", numeros_enteros)


# Ejercicio 22: Crear una lista con los nombres de 5 materias favoritas y ordenarlas alfabéticamente.
materias = ["Matemáticas", "Lengua", "Física", "Química", "Historia"]
materias.sort()  # Usamos sort para ordenar la lista alfabéticamente
print("Lista de materias ordenadas alfabéticamente:", materias)


# Ejercicio 23: Crear una lista con los números del 1 al 15 y mostrar solo los múltiplos de 3.
numeros_15 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]  # Creamos una lista con los números del 1 al 15
multiplos_de_3 = [x for x in numeros_15 if x % 3 == 0]  # Usamos comprensión de listas para filtrar múltiplos de 3
print("Múltiplos de 3 entre 1 y 15:", multiplos_de_3)


# Ejercicio 24: Crear una lista con los nombres de 10 artistas favoritos y utilizar un bucle `for` para imprimir cada nombre en mayúsculas.
artistas = ["Shakira", "Carlos Vives", "J Balvin", "Sofia Vergara", "Maluma", "Karol G", "Silvestre Dangond", "Joe Arroyo", "Marc Anthony", "Luis Fonsi"]
for artista in artistas:  # Usamos un bucle for para recorrer la lista de artistas
    print(artista.upper())  # Imprimimos cada nombre en mayúsculas


# Ejercicio 25: Crear una lista con los números del 1 al 20 y utilizar una comprensión de listas para crear una nueva lista con solo los números pares.
numeros_20 = list(range(1, 21))  # Lista de números del 1 al 20
pares = [x for x in numeros_20 if x % 2 == 0]  # Usamos comprensión de listas para filtrar los números pares
print("Números pares entre 1 y 20:", pares)


# Ejercicio 26: Crear una lista con los nombres de los municipios del departamento de Arauca y utilizar un bucle `for` para imprimir cada nombre en orden inverso.
municipios = ["Arauca", "Arauquita", "Tame", "Fortul", "Saravena", "Puerto Rondón", "Cravo Norte", "Cubará", "La Salina", "Soyos"]
for municipio in reversed(municipios):  # Usamos reversed para recorrer la lista en orden inverso
    print(municipio)


# Ejercicio 27: Crear una lista con los números del 1 al 12 y utilizar una comprensión de listas para crear una nueva lista con los cuadrados de cada número.
numeros_12 = list(range(1, 13))  # Creamos una lista con los números del 1 al 12
cuadrados = [x**2 for x in numeros_12]  # Usamos comprensión de listas para obtener los cuadrados de cada número
print("Cuadrados de los números del 1 al 12:", cuadrados)


# Ejercicio 28: Crear una lista con los meses del año y utilizar el método `.index()` para obtener el índice del mes "Junio".
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
indice_junio = meses.index("Junio")  # Usamos el método .index() para obtener el índice de "Junio"
print("El índice de 'Junio' es:", indice_junio)


# Ejercicio 29: Crear una lista con los nombres que usted le pondría a 6 mascotas y utilizar el método `.remove()` para eliminar una mascota de la lista.
mascotas = ["Tom", "Candy", "Lulu", "Mafalda", "Garfield", "Lupe"]
mascotas.remove("Garfield")  # Usamos .remove() para eliminar "Rocky" de la lista
print("Lista de mascotas después de eliminar 'Garfield':", mascotas)


# Ejercicio 30: Crear una lista con los números del 1 al 20 y utilizar el método `.sort(reverse=True)` para ordenarla de forma descendente.
numeros_20 = list(range(1, 21))  # Creamos una lista con los números del 1 al 20
numeros_20.sort(reverse=True)  # Usamos .sort(reverse=True) para ordenar la lista de forma descendente
print("Lista de números ordenada de forma descendente:", numeros_20)


# Ejercicio 31: Crear una lista con los nombres de 4 libros favoritos y utilizar el método `.append()` para agregar un nuevo libro al final de la lista.
libros_favoritos = ["Dejad que los niños vengan a mi", "Lo que no tiene nombre", "Paula", "Cien años de soledad"]
libros_favoritos.append("El principito")  # Usamos .append() para agregar un nuevo libro al final
print("Lista de libros después de agregar un nuevo libro:", libros_favoritos)


# Ejercicio 32: Crear una lista con los números del 1 al 15 y utilizar una comprensión de listas para crear una nueva lista con los números impares.
numeros_15 = list(range(1, 16))  # Lista de números del 1 al 15
impares = [x for x in numeros_15 if x % 2 != 0]  # Usamos comprensión de listas para filtrar los números impares
print("Números impares entre 1 y 15:", impares)


# Ejercicio 33: Crear una lista con los nombres de 7 comidas favoritas y utilizar el método `.insert()` para agregar una nueva comida en la posición 3.
comidas = ["Perro caliente", "Lentejas", "Empanadas", "Arroz chino", "Pollo asado", "Ensalada", "Arepa rellena"]
comidas.insert(3, "Sancocho")  # Usamos .insert() para agregar "Ramen" en la posición 3
print("Lista de comidas después de insertar 'Ramen':", comidas)


# Ejercicio 34: Crear una lista con los números del 1 al 10 y utilizar el método `.extend()` para agregar una segunda lista con los números del 11 al 15.
numeros_10 = list(range(1, 11))  # Lista de números del 1 al 10
numeros_15 = list(range(11, 16))  # Lista de números del 11 al 15
numeros_10.extend(numeros_15)  # Usamos .extend() para agregar los números del 11 al 15
print("Lista después de usar .extend():", numeros_10)


# Ejercicio 35: Crear una lista con los nombres de 6 compañeros y utilizar el método `.count()` para contar cuántas veces aparece un nombre específico en la lista.
companeros = ["Valentina", "Luis", "Daniel", "Juan Esteban", "Juan Manuel", "Juan José"]
cantidad_valentina = companeros.count("Valentina")  # Usamos .count() para contar cuántas veces aparece "Ana"
print("El nombre 'Valentina' aparece", cantidad_valentina, "veces en la lista.")


# Ejercicio 36: Crear una lista con los números del 1 al 12 y utilizar una comprensión de listas para crear una nueva lista con los números divisibles por 3.
numeros_12 = list(range(1, 13))  # Lista de números del 1 al 12
divisibles_por_3 = [x for x in numeros_12 if x % 3 == 0]  # Usamos comprensión de listas para filtrar divisibles por 3
print("Números divisibles por 3 entre 1 y 12:", divisibles_por_3)


# Ejercicio 37: Crear una lista con los nombres de 5 artistas musicales favoritos y utilizar el método `.reverse()` para invertir el orden de la lista.
artistas_favoritos = ["Yohio", "Camila", "Luis Miguel", "Maluma", "Karol G"]
artistas_favoritos.reverse()  # Usamos .reverse() para invertir el orden de la lista
print("Lista de artistas invertida:", artistas_favoritos)


# Ejercicio 38: Crear una lista con los números del 1 al 20 y utilizar una función lambda y el método `.sort()` para ordenar la lista de forma descendente.
numeros_20 = list(range(1, 21))  # Lista de números del 1 al 20
numeros_20.sort(key=lambda x: -x)  # Usamos lambda para ordenar de forma descendente
print("Lista de números ordenada de forma descendente con lambda:", numeros_20)


# Ejercicio 39: Crear una lista con las materias de la universidad y utilizar el método `.pop()` para eliminar y obtener el último elemento de la lista.
materias_universidad = ["Matemáticas Básicas", "Ingenieria de Software I", "Bases de Datos I", "Estadística I", "Cálculo diferencial"]
ultima_materia = materias_universidad.pop()  # Usamos .pop() para eliminar y obtener el último elemento
print("Última materia eliminada:", ultima_materia)
print("Lista de materias después de eliminar la última:", materias_universidad)


# Ejercicio 40: Crear una lista con los números del 1 al 25 y utilizar una comprensión de listas para crear una nueva lista con los números múltiplos de 5.
numeros_25 = list(range(1, 26))  # Lista de números del 1 al 25
multiplos_de_5 = [x for x in numeros_25 if x % 5 == 0]  # Usamos comprensión de listas para filtrar múltiplos de 5
print("Múltiplos de 5 entre 1 y 25:", multiplos_de_5)


# Ejercicio 41: Crear una lista con los nombres de 8 deportes y utilizar una función anónima y el método `.sort()` para ordenar la lista.
deportes = ["Fútbol", "Baloncesto", "Béisbol", "Tenis", "Natación", "Ciclismo", "Atletismo", "Voleibol"]
deportes.sort(key=lambda x: x.lower())  # Usamos una función lambda para ordenar la lista alfabéticamente
print("Lista de deportes ordenada:", deportes)


# Ejercicio 42: Crear una lista con los números del 1 al 15 y utilizar el método `.clear()` para eliminar todos los elementos de la lista.
numeros_15 = list(range(1, 16))  # Lista de números del 1 al 15
numeros_15.clear()  # Usamos .clear() para eliminar todos los elementos de la lista
print("Lista después de usar .clear():", numeros_15)


# Ejercicio 43: Crear una lista con los nombres de 6 países y utilizar un bucle `for` para imprimir cada nombre en minúsculas.
paises = ["Colombia", "México", "Argentina", "Chile", "Perú", "España"]
for pais in paises:  # Usamos un bucle for para recorrer la lista de países
    print(pais.lower())  # Imprimimos cada país en minúsculas


# Ejercicio 44: Crear una lista con los números del 1 al 20 y utilizar una comprensión de listas para crear una nueva lista con los cuadrados de los números pares.
numeros_20 = list(range(1, 21))  # Creamos una lista con los números del 1 al 20
cuadrados_pares = [x**2 for x in numeros_20 if x % 2 == 0]  # Usamos comprensión de listas para obtener los cuadrados de los números pares
print("Cuadrados de los números pares entre 1 y 20:", cuadrados_pares)


# Ejercicio 45: Crear una lista con los nombres de 10 videojuegos y utilizar el método `.index()` para obtener el índice de un juego específico.
videojuegos = ["Minecraft", "Fortnite", "The Witcher 3", "Super Mario Odyssey", "Zelda: Breath of the Wild", "GTA V", "FIFA 21", "Call of Duty", "Among Us", "Red Dead Redemption 2"]
indice_zelda = videojuegos.index("Zelda: Breath of the Wild")  # Usamos .index() para obtener el índice de "Zelda: Breath of the Wild"
print("El índice de 'Zelda: Breath of the Wild' es:", indice_zelda)


# Ejercicio 46: Crear una lista con los números del 1 al 12 y utilizar el método `.remove()` para eliminar un número específico de la lista.
numeros_12 = list(range(1, 13))  # Lista con los números del 1 al 12
numeros_12.remove(7)  # Usamos .remove() para eliminar el número 7 de la lista
print("Lista después de eliminar el número 7:", numeros_12)


# Ejercicio 47: Crear una lista con los nombres de 7 monumentos colombianos y utilizar una función lambda y el método `.sort(key=len)` para ordenar la lista por longitud de nombre.
monumentos_colombianos = ["Monserrate", "Torre de Guadalupe", "Ciudad Perdida", "Catedral de Sal", "Isla de San Andrés", "Parque Nacional Natural Tayrona", "La Candelaria"]
monumentos_colombianos.sort(key=lambda x: len(x))  # Usamos lambda y .sort() para ordenar los monumentos por la longitud de su nombre
print("Lista de monumentos ordenada por longitud de nombre:", monumentos_colombianos)


# Ejercicio 48: Crear una lista con los números del 1 al 18 y utilizar una comprensión de listas para crear una nueva lista con los números múltiplos de 3 y 5.
numeros_18 = list(range(1, 19))  # Lista con los números del 1 al 18
multiples_3_y_5 = [x for x in numeros_18 if x % 3 == 0 or x % 5 == 0]  # Usamos comprensión de listas para filtrar múltiplos de 3 y 5
print("Números múltiplos de 3 y 5 entre 1 y 18:", multiples_3_y_5)


# Ejercicio 49: Crear una lista con los nombres de 6 asignaturas que le parecen interesantes de la carrera y utilizar el método `.append()` para agregar un nuevo nombre al final de la lista.
asignaturas = ["Matemáticas Basicas", "Pruebas", "Bases de Datos", "Programación", "Analisis Numerico", "Inglés"]
asignaturas.append("Cálculo Diferencial")  # Usamos .append() para agregar "Cálculo Diferencial" al final de la lista
print("Lista de asignaturas después de agregar una nueva asignatura:", asignaturas)


# Ejercicio 50: Crear una lista con los números del 1 al 25 y utilizar el método `.pop()` para eliminar y obtener el elemento de la posición 7.
numeros_25 = list(range(1, 26))  # Lista con los números del 1 al 25
elemento_pos_7 = numeros_25.pop(7)  # Usamos .pop() para eliminar y obtener el elemento de la posición 7
print("Elemento eliminado de la posición 7:", elemento_pos_7)
print("Lista después de usar .pop() en la posición 7:", numeros_25)
