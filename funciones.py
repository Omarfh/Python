"""

def imprimir_mensaje():
    print("Mensaje especial: ")
    print("¡Estoy aprendiendo a usar funciones")

imprimir_mensaje()
imprimir_mensaje()
imprimir_mensaje()

"""

"""
opcion = int(input("Elige una opción (1, 2, 3): "))
if opcion == 1:
    print("Hola")
    print("Cómo estás")
    print("Elegiste la opción 1")
    print("Adios")
elif opcion == 2:
    print("Hola")
    print("Cómo estás")
    print("Elegiste la opción 2")
    print("Adios")
elif opcion == 3:
    print("Hola")
    print("Cómo estás")
    print("Elegiste la opción 3")
    print("Adios")
else:
    print("Escribe la opción correcta")

"""

def conversacion(mensaje):
    print("Hola")
    print("Cómo estás")
    print(mensaje)
    print("Adios")

opcion = int(input("Elige una opción (1, 2, 3): "))
if opcion == 1:
    conversacion("Elegiste la opción 1")
elif opcion == 2:
    conversacion("Elegiste la opción 2")
elif opcion == 3:
    conversacion("Elegiste la opción 3")
else:
    print("Escribe la opción correcta")


