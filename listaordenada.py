import random

numerosDesordenados = []
for i in range(10):
    numeroAleatorio = random.randint(0,10)
    numerosDesordenados.append(numeroAleatorio)
print ("Numeros aleatorios")
print(f" {numerosDesordenados} \n")


numerosDesordenados.sort()
print ("Numeros acendente")
print(f" {numerosDesordenados}\n")

numerosDesordenados.sort(reverse=True)
print ("Numeros decendente")
print (f" {numerosDesordenados} \n")