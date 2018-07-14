def resolver(q, s):
    if q == 1:
        return 1
    else:
        return (resolver(q - 1, s) + s-1) % q + 1


def main():
    casos = int(input()) + 1
    for i in range(1, casos):
        entrada = input()
        tratada = entrada.split()
        quantidade = int(tratada[0])
        salto = int(entrada[2])

        print("Case {}: {}".format(i, resolver(quantidade, salto)))
    
main()
