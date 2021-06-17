def calculo_conversion(tipo_pesos, valor_dolar):
    pesos = input("¿Cuantos pesos " + tipo_pesos + " tiene? ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")


def run():
    menu = """
    Bienvenido al conversor de moneda 💰💵

    Elige tu opción 

    1 - Pesos Colombianos
    2 - Pesos Argentinos
    3 - Pesos Mexicanos

    """
    option = input(menu)

    if option == "1":
        calculo_conversion("colombianos", 3875)
    elif option == "2":
        calculo_conversion("argentinos", 65)
    elif option == "3":
        calculo_conversion("mexicanos", 24)
    else:
        print("Ingresa una opción valida")


if __name__ == '__main__':
    run()