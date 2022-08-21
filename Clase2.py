# Clase 2: Estructuras de datos basicas y condicionales basicos
#palabras reservadar= if= si condicional, siempre valida que la condicion sea true osea verdadera/ elif= es otro if es el if elegante else= cierre if: cabeza, else: tronco else: pies
# int = convierte algo en entero
edad = int(input("ingrese su edad \n") )
if edad > 20 and edad <= 200:
    print("la persona es mayor de 20 años, puede salir a farrear")
elif edad < 0:
    print("nadie tiene edad negativa genio")
elif edad > 200:
    print("Usted es una momia")
else:
    print("la persona no puede salir a farrear") 
    