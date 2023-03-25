var_peso = int(input("Digite seu peso atual em quilos: "))
var_altura = int(input("Digite sua altura em centimetros: "))

var_altura_metros = var_altura / 100

imc = var_peso / (var_altura_metros**2)

if imc < 18.5:
    print(f"IMC = {imc:,.1f}".format(imc))
    print("Peso baixo")
elif imc > 18.5 and imc < 24.9:
    print(f"IMC = {imc:,.1f}".format(imc))
    print("Peso normal ou adequado")
elif imc > 25.0 and imc < 29.9:
    print(f"IMC = {imc:,.1f}".format(imc))
    print("Sobrepeso")
elif imc > 30.0 and imc < 34.9:
    print(f"IMC = {imc:,.1f}".format(imc))
    print("Obesidade grau 1")
elif imc > 35.0 and imc < 39.9:
    print(f"IMC = {imc:,.1f}".format(imc))
    print("Obesidade grau 2")
else:
    print(f"IMC = {imc:,.1f}".format(imc))
    print("Obesidade grau 3 ou mórbida")
