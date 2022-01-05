menu = """
Bienvenido al covertidor de moneda 
1- Pesos colombianos
2- Pesos argentinos
3- Pesos Mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    pesos = input("¿Cuántos pesos colombinos tiene?: ")
    pesos = float(pesos)
    valor_dolar =  3875
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes  $" + dolares + " dólares")
elif opcion == 2:
    pesos = input("¿Cuántos pesos argentinos tiene?: ")
    pesos = float(pesos)
    valor_dolar =  103.15
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes  $" + dolares + " dólares")
elif opcion == 3:
    pesos = input("¿Cuántos pesos Mexicanos tiene?: ")
    pesos = float(pesos)
    valor_dolar =  20.45
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes  $" + dolares + " dólares")
else:
    print("Ingresa una opción correcta por favor")

