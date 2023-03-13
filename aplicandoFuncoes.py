from fibonacci import*

numero = int(input("Digite a quantidade de digitos: "))

for i in range(numero):
    print( "\033[033m%d" % fib(int(i+1)))
