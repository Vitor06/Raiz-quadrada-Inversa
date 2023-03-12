from cmath import sqrt
from ctypes import c_float, c_int32, cast, byref, POINTER,Union,c_int
import ctypes
from prettytable import PrettyTable
ERRO = 1000
D = 10
TOLERANCIA = 10**-D-1
A = 625#sqrt(A)
itmax =20
class union(Union):
    _fields_ = [("x", c_float),
                ("k", c_int)]


table_newton_rapson = PrettyTable()
table_inversa_newton_rapson = PrettyTable()


def raiz_quadrada_newton_rapson():
    global ERRO,TOLERANCIA,xk,A,itmax
    k ,x0 =0, 1+(fracao(A)/2)
    xk = x0
    xk_list,xk_1_list,erro_list = [],[],[]
    while ERRO>TOLERANCIA and k<itmax:
        x_k_1 = 0.5*(xk+A/xk)

        xk_list.append(xk)
        xk_1_list.append(x_k_1)

        ERRO  =abs(x_k_1 - xk)
        erro_list.append(ERRO)
        xk  = x_k_1

        k+=1
    return xk,xk_list,xk_1_list,erro_list

def raiz_inversa_newton_rapson():
    global ERRO,TOLERANCIA,xk,A,itmax,k
    k ,x0 =0, 0.02
    print(x0)
    xk = x0
    xk_list,xk_1_list,erro_list = [],[],[]
    while ERRO>TOLERANCIA and k<itmax:
        x_k_1 = xk*(1.5 - 0.5*A*(xk**2))
        xk_list.append(xk)
        xk_1_list.append(x_k_1)

        ERRO  =abs(x_k_1 - xk)
        erro_list.append(ERRO)

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

def fracao (A):
    x0 = list(bin(ctypes.c_uint32.from_buffer(ctypes.c_float(A)).value))
    x0 = x0[10:len(x0)]
    soma = 0
    k = -1
    for i in x0:
        if(i!="0"):
            soma  = soma +2**(k)
        k-=1
    print(soma)
    return soma

def main():


    print("--------SQRT(A)=>1/SQRT(A)--------\n")
    raiz,xk1,x_k_1_1,erro1 = raiz_quadrada_newton_rapson()
    table_newton_rapson.add_column("K",range(itmax))
    table_newton_rapson.add_column("xk",xk1)
    table_newton_rapson.add_column("xk+1",x_k_1_1)
    table_newton_rapson.add_column("Erro",erro1)
    print(table_newton_rapson)
    inversa = 1/raiz
    print('Inversa: '+str(inversa))

    print("--------1/SQRT(A)--------\n")
    inversa2,xk2,x_k_1_2,erro2  = raiz_inversa_newton_rapson()
    table_inversa_newton_rapson.add_column("K",range(itmax))
    table_inversa_newton_rapson.add_column("xk",xk2)
    table_inversa_newton_rapson.add_column("xk+1",x_k_1_2)
    table_inversa_newton_rapson.add_column("Erro",erro2)
    print(table_inversa_newton_rapson)
    print("Inversa:"+str(inversa2))


    print()
    print("Metodo de gary Tarolli")
    inversa3 = raiz_inversa_tarolli(A)
    print(inversa3)


main()
