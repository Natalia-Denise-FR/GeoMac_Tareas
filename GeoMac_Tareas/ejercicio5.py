#Ejercicio 5
#Geofísica Matemática y Computacional
#Natalia Denise Fuentes Rubio
#Pre-examen

n = int(input('Escribe un numero'))
#print({n})

import numpy as np
import matplotlib.pyplot as plt


def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
    
#print(fibo(n))
#print(fibo(n-1))
#print(fibo(n-2))

lista = [1,1]
for i in range(n-1):
    lista.append(lista[i]+lista[i+1])
print(lista)

xn = fibo(n-1)/fibo(n-2)

#x = range(0,n)

listaxn = [lista[i]/float(lista[i-1])
           for i in range(2,len(lista))]
print(listaxn)

GR = (1 + np.sqrt(5))/2

Ea = np.fabs(xn - GR)
print ('Error absoluto:', Ea)
Er = Ea / np.fabs(xn) 
print ('Error relativo:', Er)

ticks = range(0,n,1)

#x = np.arange(0, n)
#y = np.arange(0, xn)

plt.plot(listaxn, lw=2, label='Secuencia Xn')
#plt.xticks(ticks)
plt.title('Gráfica de la secuencia $x$')
plt.xlabel('n-2')
plt.ylabel('Valor de $x_n$')
plt.legend()
plt.grid()
plt.show()