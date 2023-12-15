# Solicitar al usuario ingresar el número de días
Numerodedias = int(input("Por favor ingrese el número de días: "))
if Numerodedias <= 0:
    print("ADVERTENCIA EN EL CASO DE QUE COLOQUE 0 DÍAS SE TERMINARÁ EL PROGRAMA")
else:
    # Crear una lista
    # vacía para almacenar los precios del dólar para cada día
    precios_dolares = []

    # Solicitar al usuario ingresar el precio del dólar para cada uno de los Numerodedias
    for Rango in range(Numerodedias):
        precio_dolar = float(input(f"Ingrese el precio del dólar para el día {Rango+1}: "))
        precios_dolares.append(precio_dolar)

    # Crear una lista vacía para almacenar las alzas de un día para el otro
    alzas = []
    advertencia = False  # Se establece una variable de control para las alzas iguales a 0.0

    # Calcular las alzas de un día para el otro
    for Rango in range(Numerodedias-1):
        alza = precios_dolares[Rango+1] - precios_dolares[Rango]
        alzas.append(alza)
        if alza == 0.0:
            advertencia = True  # Se activa la advertencia si alguna alza es 0.0

    # Luego de calcular todas las alzas
    if advertencia:  # Si se activó la advertencia en algún momento
        print("ADVERTENCIA: Una o más alzas han resultado en 0.0.")
    else:
        mayor_alza = max(alzas)
        print(f"La mayor alza fue de {mayor_alza}. bien hecho")

    # Mostrar la mayor alza
