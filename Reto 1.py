#Calculadora IMC
from tkinter.tix import InputOnly


peso = float(input("por favor ingresar su peso"))
altura = float(input("por favor ingresar su altura"))
imc = peso/altura**2
#float: numeros con decimales o de coma (,) flotante
if imc < 18.5:
    print("underweight")
elif imc >= 18.5 and imc <= 24.9:
    print("normal")
elif imc >= 25 and imc <= 29.9:
    print("overweight")
elif imc >=30:
    print("obesity")