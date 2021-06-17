menu = """
Bienvenido al conversor de moneda 💰💵

Elige tu opción 

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

"""
option = input(menu)

if option == "1":
    pesos = input("¿Cuantos pesos colombianos tiene? ")
    pesos = float(pesos)
    valor_dolar = 3875
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")
elif option == "2":
    pesos = input("¿Cuantos pesos argentinos tiene? ")
    pesos = float(pesos)
    valor_dolar = 65
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")
elif option == "3":
    pesos = input("¿Cuantos pesos mexicanos tiene? ")
    pesos = float(pesos)
    valor_dolar = 24
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")
else:
    print("Ingresa una opción valida")