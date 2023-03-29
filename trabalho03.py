from ctypes import c_float, c_int32,Union
import ctypes
import math
import time
import matplotlib.pyplot as plt

class union(Union):
    _fields_ = [("x", c_float),
                ("k", c_int32)]


def desenhar_ponto(ponto,color,text,i,j):
    plt.plot(ponto[0], ponto[1], marker="o", markersize=5, markeredgecolor=color, markerfacecolor=color,label=text,)#Posicao real
    # plt.set_title(text)
    plt.legend()

def raiz_quadrada_newton_rapson(A):
    x0 =aproximacao_da_raiz(A)
    xk = x0
    x_k_1 = 0.5*(xk+A/xk)
    xk  = x_k_1
    return xk

def raiz_inversa_newton_rapson(A):
    D = 0.5*A#constante
    C = 1/aproximacao_da_raiz(A)#constante
    x0 =C
    xk = x0
    x_k_1 = xk*(1.5 - D*(xk**2))
    xk  = x_k_1

    return xk

def raiz_inversa_tarolli(x):
    x2 = 0.5*x
    u = union()
    u.x  = x
    u.k = 0x5f3759df - (u.k >> 1)
    u.x = u.x *(1.5 - x2*u.x*u.x)
    return u.x

def raiz_calculadora(x):
    return math.sqrt(x)

def aproximacao_da_raiz(A):
        val= union()
        val.x = A
        val.k -= 1<<23
        val.k >>=1
        val.k += 1<<29
        return val.x
def main():
    N = 1000
    erro_list_calculadora_raiz_newton_rapson,erro_list_calculadora_inversa_taroli,erro_list_calculadora_inversa_direto_newton_rapson = [],[],[]
    x_list = []
    inversa_raiz_newton_rapson_list = []
    inversa_direto_newton_rapson_list = []
    inversa_taroli_list = []
    inversa_calculadora_list = []

    tempo_inversa_raiz_newton_rapson = []
    tempo_inversa_direto_newton_rapson = []
    tempo_inversa__tarolin = []
    tempo_inversa_calculadora = []
    for x in range(1,N,1):

        start_raiz_quadrada_newton_rapson = time.time()
        raiz = raiz_quadrada_newton_rapson(x)

        inversa_raiz_newton_rapson = 1/raiz
        fim_raiz_quadrada_newton_rapson = time.time()
        tempo_inversa_raiz_newton_rapson.append(fim_raiz_quadrada_newton_rapson-start_raiz_quadrada_newton_rapson)

        inversa_raiz_newton_rapson_list.append(inversa_raiz_newton_rapson)

        start_inversa_direto_newton_rapson =  time.time()
        inversa_direto_newton_rapson  = raiz_inversa_newton_rapson(x)
        fim_inversa_direto_newton_rapson = time.time()

        tempo_inversa_direto_newton_rapson.append(fim_inversa_direto_newton_rapson-start_inversa_direto_newton_rapson)
        inversa_direto_newton_rapson_list.append(inversa_direto_newton_rapson)


        start_inversa_taroli=  time.time()
        inversa_taroli = raiz_inversa_tarolli(x)
        fim_inversa_taroli =  time.time()

        tempo_inversa__tarolin.append(fim_inversa_taroli-start_inversa_taroli)
        inversa_taroli_list.append(inversa_taroli)

        start_inversa_calculadora = time.time()
        inversa_calculadora = 1/raiz_calculadora(x)
        fim_inversa_calculadora = time.time()

        tempo_inversa_calculadora.append(fim_inversa_calculadora-start_inversa_calculadora)
        inversa_calculadora_list.append(inversa_calculadora)

        #Calculo dos erros
        erro_calculadora_raiz_newton_rapson = abs(inversa_calculadora - inversa_raiz_newton_rapson)
        erro_calculadora_inversa_taroli = abs(inversa_calculadora - inversa_taroli  )
        erro_calculadora_inversa_direto_newton_rapson = abs(inversa_calculadora - inversa_direto_newton_rapson )

        erro_list_calculadora_raiz_newton_rapson.append(erro_calculadora_raiz_newton_rapson)
        erro_list_calculadora_inversa_taroli.append(erro_calculadora_inversa_taroli)
        erro_list_calculadora_inversa_direto_newton_rapson.append(erro_calculadora_inversa_direto_newton_rapson)
        x_list.append(x)

        # print(inversa_calculadora,inversa_raiz_newton_rapson,inversa_direto_newton_rapson,inversa_taroli)
    #Gráficos

    plt.plot(x_list,erro_list_calculadora_inversa_direto_newton_rapson,label='Calculadora X inversa_direto_newton_rapson ')
    plt.plot(x_list,erro_list_calculadora_inversa_taroli,label='Calculadora X Tarolli')
    plt.plot(x_list,erro_list_calculadora_raiz_newton_rapson,label='Calculadora X raiz_newton_rapson')

    plt.xlabel('Argumento')
    plt.ylabel('Erro')
    plt.legend()
    plt.show()

    plt.plot(x_list,inversa_raiz_newton_rapson_list,label = "1/newton_rapson")
    plt.plot(x_list,inversa_direto_newton_rapson_list,label = "direta newton_rapson")
    plt.plot(x_list,inversa_taroli_list,label = "Tarolli")
    plt.plot(x_list,inversa_calculadora_list,label = "Calculadora")

    plt.yscale('log')
    plt.xlabel('Argumento')
    plt.ylabel('Valores')
    plt.legend()
    plt.show()

    plt.plot(x_list,tempo_inversa_raiz_newton_rapson,label = "1/newton_rapson")
    plt.plot(x_list,tempo_inversa_direto_newton_rapson,label = "direta newton_rapson")
    plt.plot(x_list,tempo_inversa__tarolin,label = "Tarolli")
    plt.plot(x_list,tempo_inversa_calculadora,label = "Calculadora")

    plt.xlabel('Argumento')
    plt.ylabel('Tempo')
    plt.legend()
    plt.show()


main()
