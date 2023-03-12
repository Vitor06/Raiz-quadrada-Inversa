from ctypes import c_float, c_int32, cast, byref, POINTER
import struct
ERRO = 1000
D = 10
TOLERANCIA = 10**-D-1
A = 16#sqrt(A)
itmax = 20

def raiz_quadrada_newton_rapson():
    global ERRO,TOLERANCIA,xk,A,X0,itmax
    k ,x0 =0, 0.02
    xk = x0
    while ERRO>TOLERANCIA and k<itmax:
        x_k_1 = 0.5*(xk+A/xk)
        ERRO  =abs(x_k_1 - xk)
        xk  = x_k_1
        print('k = '+ str(k)+' ->  '+ str(xk))
        k+=1
    return xk
def raiz_inversa_newton_rapson():
    global ERRO,TOLERANCIA,xk,A,X0,itmax,k
    k ,x0 =0, 0.02
    xk = x0
    while ERRO>TOLERANCIA and k<itmax:
        x_k_1 = xk*(1.5 - 0.5*A*(xk**2))
        ERRO  =abs(x_k_1 - xk)
        xk  = x_k_1
        print('k = '+ str(k)+' ->  '+ str(xk))
        k+=1
    return xk
def raiz_inversa_tarolli(x):
    threehalfs = 1.5
    x2 = x * 0.5
    y = x
    packed_y = struct.pack('f', y)
    i = struct.unpack('i', packed_y)[0]
    i = 0x5f3759df - (i >> 1)
    packed_i = struct.pack('i', i)
    y = struct.unpack('f', packed_i)[0]

    y = y * (threehalfs - (x2 * y * y))
    return y

def main():

    print("--------SQRT(A)=>1/SQRT(A)--------\n")
    raiz = raiz_quadrada_newton_rapson()
    inversa = 1/raiz
    print('Inversa: '+str(inversa))
    print("----------------------------------")
    print("--------1/SQRT(A)--------\n")
    inversa2 = raiz_inversa_newton_rapson()

    print('Inversa formula: '+str(inversa2))
    print()
    print("Metodo de gary Tarolli")
    inversa3 = raiz_inversa_tarolli(A)
    print(inversa3)


main()
