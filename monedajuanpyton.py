#WHILE ES MIENTRAS
print ("A son 270,B son 340 y C son 390 \n")
#DICCIONARIOS
alimentos = {"A": 270,"B": 340,"C": 390}

#Pedimos la opcion
opcion = input("Ingrese A,B o C \n")
print("Debes sumar " + str(alimentos[opcion]))

#Sumar monedas
contador = 0


monedas = {"1": 10, "2": 50, "3":100}

print("1. $10 \n2. $50\n3. $100")

while contador < alimentos[opcion]:
    opcionMoneda = input("ingrese la opcion\n")
    contador += monedas[opcionMoneda]


if contador > alimentos[opcion]:
    vueltos = contador - alimentos[opcion] 
    total = vueltos
    
    if vueltos >= 50:
        print("1. $50")
        vueltos -= 50
    while vueltos > 0:
        print("1. $10")
        vueltos -= 10

# el texto mas el + y el str que es un numero hace que se ponga en texto el numero , y no salga error
    print("En total se le devolvio $" + str(total))
if contador == alimentos[opcion]:
   print("No se le devuelve nada")
