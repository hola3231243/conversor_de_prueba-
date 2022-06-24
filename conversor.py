def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿cuantos pesos" + tipo_pesos + "tiene?... ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2 )
    dolares = str(dolares)
    print("TIENE $" + dolares + " dolares")
    print("GASTELOS BIEN ;)")

menu = """
Bienvenido al conversor de monedas 

seleccione la moneda:
1 - 🟡🔵🔴pesos Colombianos🟡🔵🔴
2 - 🔵⚪️🔵pesos argentinos🔵⚪️🔵
3 - 🟢⚪️🔴pesos Mexicanos🟢⚪️🔴

seleccione una opcion...
"""
opcion = int(input(menu))

if opcion == 1:
    conversor(" Colombianos ", 4018.50)
elif opcion == 2:
    conversor(" Argentinos ", 123)
elif opcion == 3:
    conversor(" Mexicanos ", 20.20)
else:
    print("#####ERROR#####")
    print("ingrese una opcion correcta por favor")

menu2 ="""
DESEA CAMBIAR DE DOLARES A OTRA MONEDA
1 SI🟢
2 NO🔴
"""
opcion2 = int(input(menu2))

if opcion2 == 1:
    menu3 =""" ¿A que moneda desea convertir?
    1 - 🟡🔵🔴pesos Colombianos🟡🔵🔴
    2 - 🔵⚪️🔵pesos argentinos🔵⚪️🔵
    3 - 🟢⚪️🔴pesos Mexicanos🟢⚪️🔴
    """
    opcion3 = int(input(menu3))
    if opcion3 == 1:
        dolares = input("¿cuantos dolares tiene?")
        dolares = float(dolares)
        valor_pesos = 0.00025
        pesos = dolares / 0.00025
        pesos = round(pesos, 2)
        pesos = str(pesos)
        print("TIENE $" + pesos +" pesos")
        print("GASTELOS BIEN ;)")
    elif opcion3 == 2:
        dolares = input("¿cuantos dolares tiene?")
        dolares = float(dolares)
        valor_pesos = 0.0081
        pesos = dolares / 0.0081
        pesos = round(pesos, 2)
        pesos = str(pesos)
        print("TIENE $" + pesos +" pesos")
        print("GASTELOS BIEN ;)")
        
    elif opcion3 == 3:
        dolares = input("¿cuantos dolares tiene?")
        dolares = float(dolares)
        valor_pesos = 0.050
        pesos = dolares / 0.050
        pesos = round(pesos, 2)
        pesos = str(pesos)
        print("TIENE $" + pesos +" pesos")
        print("GASTELOS BIEN ;)")
    else:
        print("###ERROR###")
        print("por favor coloque una opcion logica")
    
elif opcion2 == 2:
    print("###Entendible tenga buen dia###")
else:
    print("###ERROR###")
    




