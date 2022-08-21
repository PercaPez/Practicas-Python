#Ciclos: sirven para recorrer ciertos datos o lo que se requiere, hay ciclos extenso y cortos. Ciclo for: por o por cada
#Ciclo For
# for elemento in range(10):
#     print(f"esta es la iteracion del indice: {elemento} ")
# for i in range(1,20):
#     print(f"esta es la iteracion: {i}")
# for pepito in range(1,20,2):
#     print(f"esta es la iteracion: {pepito}")

#Ciclo While: va a evaluar una condicion, la evaluacion es para TRUE si es FALSE no ejecuta
limite = int(input("ingrese el limite"))
contador = 0 
while contador < 100: 
    contador = contador + 1
    print(f"esta fue la vez numero: {contador} que paso por aqui")