ERRO = 1000
D = 10
TOLERANCIA = 10**-D-1
A = 25#sqrt(A)
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

def main():

    print("--------SQRT(A)=>1/SQRT(A)--------\n")
    raiz = raiz_quadrada_newton_rapson()
    inversa = 1/raiz
    print("----------------------------------")
    print("--------1/SQRT(A)--------\n")
    inversa2 = raiz_inversa_newton_rapson()
    print('Inversa: '+str(inversa))
    print('Inversa formula: '+str(inversa2))


main()
