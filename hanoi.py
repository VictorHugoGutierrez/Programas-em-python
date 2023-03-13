def mover (n, a, c ,b):
    if n == 1:
        print("Mova o Disco 1 para a torre {}" .format(n))
        return
    else:
        mover(n-1,a,b,c)
        print("Mova o disco {} para a torre {}" .format(n,c))
        mover(n-1,b,c,a)

n =  int(input("Digite o numero de discos: "))

mover(n,1,3,2)