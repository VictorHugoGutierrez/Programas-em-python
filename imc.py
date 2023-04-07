'''Programa que calcular o IMC'''
def calcula(massa, altura):
    '''Calcula IMC'''
    return massa / pow(altura, 2)

m = input("Entre com a sua massa: ")
a = input("Entre com sua altura: ")

imc = calcula(float(m), float(a))

if imc < 18.5:
    print("Seu IMC eh: {:.2f}" .format(imc))
    print("Seu indice eh Abaixo do Peso")

elif imc >= 18.5 and imc <= 24.9:
    print("Seu IMC eh: {:.2f}" .format(imc))
    print("Seu indice eh Peso Normal")

elif imc >= 25 and imc <= 29.9:
    print("Seu IMC eh: {:.2f}" .format(imc))
    print("Seu indice eh Execesso de Peso")

elif imc >= 30 and imc <= 34.9:
    print("Seu IMC eh: {:.2f}" .format(imc))
    print("Seu indice eh Obesidade")
else:
    print("Seu IMC eh: {:.2f}" .format(imc))
    print("Seu indice eh Obesidade Extrema")
