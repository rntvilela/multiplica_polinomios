import numpy as np
import matplotlib.pyplot as plt

def multiplicaPolinomios(A, B):
    M = len(A)
    L = len(B)

    N = M+L-1

    Ak = np.fft.fft(A, N)
    Bk = np.fft.fft(B, N)

    Ck = Ak*Bk

    return np.real(np.fft.ifft(Ck))

def trataEntrada(x):
    y = []

    x = x.replace(',', '').replace('[', '').replace(']', '').replace('(', '').replace(')', '')
    x = x.replace('{', '').replace('}', '')

    for i in x.split(' '):
        if i:
            y.append(int(i))

    return np.array(y)

def trataSaida(y):
    n = len(y)

    r = []

    for i in range(n-1):
        if y[i]:
            r.append('{0}*x^{1}'.format(round(y[i],2), n-i-1))

    if y[-1]:
        r.append('{}'.format(round(y[-1],2)))

    return ' '.join(r)

def main():
    print("Programa que calcula a multiplicação de polinomios.")
    print("\nInforme os elementos dos polinomios. ex: x^3 + 2 => [1 0 2].")

    str = ''

    while not str:
        x = trataEntrada(input('\nPrimeiro: '))
        y = trataEntrada(input('\nSegundo: '))

        z = multiplicaPolinomios(x,y)

        resultado = trataSaida(z)
        print('\nResultado: '+resultado+'\n')

        str = print('Deseja realizar nova multiplicação? Sim: <Enter> e Não: <1> + <Enter>')
        str = input('>')
    
if __name__ == "__main__":
    main()