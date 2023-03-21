from cmath import sqrt
from ctypes import c_float, c_int32, cast, byref, POINTER,Union,c_int
import ctypes
import math
import time
from prettytable import PrettyTable
import matplotlib.pyplot as plt

D = 3
TOLERANCIA = 10**-D-1
itmax =20
class union(Union):
    _fields_ = [("x", c_float),
                ("k", c_int32)]


table_newton_rapson = PrettyTable()
table_inversa_newton_rapson = PrettyTable()

def desenhar_ponto(ponto,color,text,i,j):
    plt.plot(ponto[0], ponto[1], marker="o", markersize=5, markeredgecolor=color, markerfacecolor=color,label=text,)#Posicao real
    # plt.set_title(text)
    plt.legend()

def raiz_quadrada_newton_rapson(A):
    global TOLERANCIA,xk,itmax
    erro =1000
    k ,x0 =0, 1+(fracao(A)/2)
    xk = x0
    xk_list,xk_1_list,erro_list = [],[],[]
    while erro>TOLERANCIA and k<itmax:
        x_k_1 = 0.5*(xk+A/xk)

        xk_list.append(xk)
        xk_1_list.append(x_k_1)

        erro  =abs(x_k_1 - xk)
        erro_list.append(erro)
        xk  = x_k_1

        k+=1
    return xk,xk_list,xk_1_list,erro_list

def raiz_inversa_newton_rapson(A):
    global TOLERANCIA,xk,itmax,k
    erro =1000
    k ,x0 =0, 0.002
    xk = x0
    xk_list,xk_1_list,erro_list = [],[],[]
    while erro>TOLERANCIA and k<itmax:
        x_k_1 = xk*(1.5 - 0.5*A*(xk**2))
        xk_list.append(xk)
        xk_1_list.append(x_k_1)
        erro  =abs(x_k_1 - xk)
        erro_list.append(erro)
        xk  = x_k_1

        k+=1
    return xk,xk_list,xk_1_list,erro_list
def raiz_inversa_tarolli(x):
    x2 = 0.5*x
    u = union()
    u.x  = x
    u.k = 0x5f3759df - (u.k >> 1)
    u.x = u.x *(1.5 - x2*u.x*u.x)
    return u.x

def raiz_calculadora(x):
    return math.sqrt(x)

def fracao (A):
    x0 = list(bin(ctypes.c_uint32.from_buffer(ctypes.c_float(A)).value))
    x0 = x0[10:len(x0)]
    soma = 0
    k = -1
    for i in x0:
        if(i!="0"):
            soma  = soma +2**(k)
        k-=1
    return soma

def main():
    N = 10000
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
        print()
        # print("X = "+str(x))
        # print("SQRT(A)=>1/SQRT(A)")
        start_raiz_quadrada_newton_rapson = time.time()
        raiz,xk1,x_k_1_1,erro1 = raiz_quadrada_newton_rapson(x)
        # table_newton_rapson.add_column("K",range(itmax))
        # table_newton_rapson.add_column("xk",xk1)
        # table_newton_rapson.add_column("xk+1",x_k_1_1)
        # table_newton_rapson.add_column("Erro",erro1)
        # print(table_newton_rapson)

        inversa_raiz_newton_rapson = 1/raiz
        fim_raiz_quadrada_newton_rapson = time.time()
        tempo_inversa_raiz_newton_rapson.append(fim_raiz_quadrada_newton_rapson-start_raiz_quadrada_newton_rapson)

        inversa_raiz_newton_rapson_list.append(inversa_raiz_newton_rapson)


        # print('Inversa: '+str(inversa_raiz_newton_rapson)+'\n')
        # desenhar_ponto((range(itmax),erro1),"green","Erro SQRT(A)=>1/SQRT(A)",0,0)
        # plt.show()

        # print("1/SQRT(A)")

        start_inversa_direto_newton_rapson =  time.time()
        inversa_direto_newton_rapson,xk2,x_k_1_2,erro2  = raiz_inversa_newton_rapson(x)
        fim_inversa_direto_newton_rapson = time.time()

        tempo_inversa_direto_newton_rapson.append(fim_inversa_direto_newton_rapson-start_inversa_direto_newton_rapson)
        inversa_direto_newton_rapson_list.append(inversa_direto_newton_rapson)

        # table_inversa_newton_rapson.add_column("K",range(itmax))
        # table_inversa_newton_rapson.add_column("xk",xk2)
        # table_inversa_newton_rapson.add_column("xk+1",x_k_1_2)
        # table_inversa_newton_rapson.add_column("Erro",erro2)
        # print(table_inversa_newton_rapson)
        # print("Inversa:"+str(inversa_direto_newton_rapson)+'\n')
        # desenhar_ponto((range(itmax),erro2),"red","Erro SQRT(A)=>1/SQRT(A)",0,0)

        # print()
        # print("Metodo de gary Tarolli")

        start_inversa_taroli=  time.time()
        inversa_taroli = raiz_inversa_tarolli(x)
        fim_inversa_taroli =  time.time()

        tempo_inversa__tarolin.append(fim_inversa_taroli-start_inversa_taroli)
        inversa_taroli_list.append(inversa_taroli)

        # print(inversa_taroli)

        start_inversa_calculadora = time.time()
        inversa_calculadora = 1/raiz_calculadora(x)
        fim_inversa_calculadora = time.time()

        tempo_inversa_calculadora.append(fim_inversa_calculadora-start_inversa_calculadora)
        inversa_calculadora_list.append(inversa_calculadora)

        # print("\nCalculadora -> "+str(inversa_calculadora))

        #Calculo dos erros
        erro_calculadora_raiz_newton_rapson = abs(inversa_raiz_newton_rapson - inversa_calculadora)
        erro_calculadora_inversa_taroli = abs(inversa_taroli - inversa_calculadora)
        erro_calculadora_inversa_direto_newton_rapson = abs(inversa_direto_newton_rapson - inversa_calculadora)

        erro_list_calculadora_raiz_newton_rapson.append(erro_calculadora_raiz_newton_rapson)
        erro_list_calculadora_inversa_taroli.append(erro_calculadora_inversa_taroli)
        erro_list_calculadora_inversa_direto_newton_rapson.append(erro_calculadora_inversa_direto_newton_rapson)
        x_list.append(x)

        # print()
        # print("Erro Calculadora X 1/raiz_newton_rapson -> " + str(erro_calculadora_raiz_newton_rapson) )
        # print("Erro Calculadora X Tarolli -> " + str(erro_calculadora_inversa_taroli) )
        # print("Erro Calculadora X inversa_newton_rapson -> " +str(erro_calculadora_inversa_direto_newton_rapson) )
        # print("---------------------------------------------------")

    #Gráficos
    plt.plot(x_list,erro_list_calculadora_raiz_newton_rapson,label='Calculadora X raiz_newton_rapson')
    plt.plot(x_list,erro_list_calculadora_inversa_taroli,label='Calculadora X Tarolli')
    plt.plot(x_list,erro_list_calculadora_inversa_direto_newton_rapson,label='Calculadora X inversa_direto_newton_rapson ')

    plt.xlabel('X')
    plt.ylabel('Erro')
    plt.legend()
    plt.show()

    plt.plot(x_list,inversa_raiz_newton_rapson_list,label = "1/newton_rapson")
    plt.plot(x_list,inversa_direto_newton_rapson_list,label = "direta newton_rapson")
    plt.plot(x_list,inversa_taroli_list,label = "Tarolli")
    plt.plot(x_list,inversa_calculadora_list,label = "Calculadora")

    plt.xlabel('X')
    plt.ylabel('Valores')
    plt.legend()
    plt.show()

    plt.plot(x_list,tempo_inversa_raiz_newton_rapson,label = "1/newton_rapson")
    plt.plot(x_list,tempo_inversa_direto_newton_rapson,label = "direta newton_rapson")
    plt.plot(x_list,tempo_inversa__tarolin,label = "Tarolli")
    plt.plot(x_list,tempo_inversa_calculadora,label = "Calculadora")

    plt.xlabel('X')
    plt.ylabel('Tempo')
    plt.legend()
    plt.show()

main()
