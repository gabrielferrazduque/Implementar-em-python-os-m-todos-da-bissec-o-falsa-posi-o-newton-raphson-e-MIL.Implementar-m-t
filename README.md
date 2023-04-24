# Implementar-em-python-os-m-todos-da-bissec-o-falsa-posi-o-newton-raphson-e-MIL.Implementar-m-t
Implementar em python os métodos da bissecção, falsa-posição, newton-raphson e MIL.Implementar métodos para resolução de equações Algébricas  
 
import dask


Método def new_func():
dask

new_func() bissecção, falsa-posição, newton-raphson e MIL.
  import Math
  import Math
  Math.MIL()
  Math.MetodoNewtonRaphson().MIL ()
  math.sin()
  math.cos()
  import math 
  from sklearn.datasets import make_regressionmath
import matplotlib.pyplot as plt
import numpy as np

X, y= make_regression(n_samples=100, n_features=1, noise=0.4, bias=50)



def plotLine(theta0, theta1, X, y):
    max_x = np.max(X) + 100
    min_x = np.min(X) - 100


    xplot = np.linspace(min_x, max_x, 1000)
    yplot = theta0 + theta1 * xplot



    plt.plot(xplot, yplot, color='#58b970', label='Regression Line')

    plt.scatter(X,y)
    plt.axis([-10, 10, 0, 200])
    plt.show()



def hypothesis(theta0, theta1, x):
    return theta0 + (theta1*x) 

def cost(theta0, theta1, X, y):
    costValue = 0 
    for (xi, yi) in zip(X, y):
        costValue += 0.5 * ((hypothesis(theta0, theta1, xi) - yi)**2)
    return costValue




def derivatives(theta0, theta1, X, y):
    dtheta0 = 0
    dtheta1 = 0
    for (xi, yi) in zip(X, y):
        dtheta0 += hypothesis(theta0, theta1, xi) - yi
        dtheta1 += (hypothesis(theta0, theta1, xi) - yi)*xi

    dtheta0 /= len(X)
    dtheta1 /= len(X)

    return dtheta0, dtheta1

def updateParameters(theta0, theta1, X, y, alpha):
    dtheta0, dtheta1 = derivatives(theta0, theta1, X, y)
    theta0 = theta0 - (alpha * dtheta0)
    theta1 = theta1 - (alpha * dtheta1)

    return theta0, theta1
    

def LinearRegression(X, y):
    theta0 = np.random.rand()
    theta1 = np.random.rand()
    
    for i in range(0, 1000):
        if i % 100 == 0:
            plotLine(theta0, theta1, X, y)
        # print(cost(theta0, theta1, X, y))
        theta0, theta1 = updateParameters(theta0, theta1, X, y, 0.005)

from sklearn.datasets import make_regressionmath
import matplotlib.pyplot as plt
import numpy as np

X, y= make_regression(n_samples=100, n_features=1, noise=0.4, bias=50)




def plotLine(theta0, theta1, X, y):
    max_x = np.max(X) + 100
    min_x = np.min(X) - 100


    xplot = np.linspace(min_x, max_x, 1000)
    yplot = theta0 + theta1 * xplot



    plt.plot(xplot, yplot, color='#58b970', label='Regression Line')

    plt.scatter(X,y)
    plt.axis([-10, 10, 0, 200])
    plt.show()



def hypothesis(theta0, theta1, x):
    return theta0 + (theta1*x) 

def cost(theta0, theta1, X, y):
    costValue = 0 
    for (xi, yi) in zip(X, y):
        costValue += 0.5 * ((hypothesis(theta0, theta1, xi) - yi)**2)
    return costValue




def derivatives(theta0, theta1, X, y):
    dtheta0 = 0
    dtheta1 = 0
    for (xi, yi) in zip(X, y):
        dtheta0 += hypothesis(theta0, theta1, xi) - yi
        dtheta1 += (hypothesis(theta0, theta1, xi) - yi)*xi

    dtheta0 /= len(X)
    dtheta1 /= len(X)

    return dtheta0, dtheta1

def updateParameters(theta0, theta1, X, y, alpha):
    dtheta0, dtheta1 = derivatives(theta0, theta1, X, y)
    theta0 = theta0 - (alpha * dtheta0)
    theta1 = theta1 - (alpha * dtheta1)

    return theta0, theta1
    

def LinearRegression(X, y):
    theta0 = np.random.rand()
    theta1 = np.random.rand()
    
    for i in range(0, 1000):
        if i % 100 == 0:
            plotLine(theta0, theta1, X, y)
        # print(cost(theta0, theta1, X, y))
        theta0, theta1 = updateParameters(theta0, theta1, X, y, 0.005)


from sklearn.datasets import make_regressionmath
import matplotlib.pyplot as plt
import numpy as np

X, y= make_regression(n_samples=100, n_features=1, noise=0.4, bias=50)




def plotLine(theta0, theta1, X, y):
    max_x = np.max(X) + 100
    min_x = np.min(X) - 100


    xplot = np.linspace(min_x, max_x, 1000)
    yplot = theta0 + theta1 * xplot



    plt.plot(xplot, yplot, color='#58b970', label='Regression Line')

    plt.scatter(X,y)
    plt.axis([-10, 10, 0, 200])
    plt.show()



def hypothesis(theta0, theta1, x):
    return theta0 + (theta1*x) 

def cost(theta0, theta1, X, y):
    costValue = 0 
    for (xi, yi) in zip(X, y):
        costValue += 0.5 * ((hypothesis(theta0, theta1, xi) - yi)**2)
    return costValue




def derivatives(theta0, theta1, X, y):
    dtheta0 = 0
    dtheta1 = 0
    for (xi, yi) in zip(X, y):
        dtheta0 += hypothesis(theta0, theta1, xi) - yi
        dtheta1 += (hypothesis(theta0, theta1, xi) - yi)*xi

    dtheta0 /= len(X)
    dtheta1 /= len(X)

    return dtheta0, dtheta1

def updateParameters(theta0, theta1, X, y, alpha):
    dtheta0, dtheta1 = derivatives(theta0, theta1, X, y)
    theta0 = theta0 - (alpha * dtheta0)
    theta1 = theta1 - (alpha * dtheta1)

    return theta0, theta1
    

def LinearRegression(X, y):
    theta0 = np.random.rand()
    theta1 = np.random.rand()
    
    for i in range(0, 1000):
        if i % 100 == 0:
            plotLine(theta0, theta1, X, y)
        # print(cost(theta0, theta1, X, y))
        theta0, theta1 = updateParameters(theta0, theta1, X, y, 0.005)

from sklearn.datasets import make_regressionmath
import matplotlib.pyplot as plt
import numpy as np

X, y= make_regression(n_samples=100, n_features=1, noise=0.4, bias=50)




def plotLine(theta0, theta1, X, y):
    max_x = np.max(X) + 100
    min_x = np.min(X) - 100


    xplot = np.linspace(min_x, max_x, 1000)
    yplot = theta0 + theta1 * xplot



    plt.plot(xplot, yplot, color='#58b970', label='Regression Line')

    plt.scatter(X,y)
    plt.axis([-10, 10, 0, 200])
    plt.show()



def hypothesis(theta0, theta1, x):
    return theta0 + (theta1*x) 

def cost(theta0, theta1, X, y):
    costValue = 0 
    for (xi, yi) in zip(X, y):
        costValue += 0.5 * ((hypothesis(theta0, theta1, xi) - yi)**2)
    return costValue




def derivatives(theta0, theta1, X, y):
    dtheta0 = 0
    dtheta1 = 0
    for (xi, yi) in zip(X, y):
        dtheta0 += hypothesis(theta0, theta1, xi) - yi
        dtheta1 += (hypothesis(theta0, theta1, xi) - yi)*xi

    dtheta0 /= len(X)
    dtheta1 /= len(X)

    return dtheta0, dtheta1

def updateParameters(theta0, theta1, X, y, alpha):
    dtheta0, dtheta1 = derivatives(theta0, theta1, X, y)
    theta0 = theta0 - (alpha * dtheta0)
    theta1 = theta1 - (alpha * dtheta1)

    return theta0, theta1
    

def LinearRegression(X, y):
    theta0 = np.random.rand()
    theta1 = np.random.rand()
    
    for i in range(0, 1000):
        if i % 100 == 0:
            plotLine(theta0, theta1, X, y)
        # print(cost(theta0, theta1, X, y))
        theta0, theta1 = updateParameters(theta0, theta1, X, y, 0.005)


from sklearn.datasets import make_regressionmath
import matplotlib.pyplot as plt
import numpy as np

X, y= make_regression(n_samples=100, n_features=1, noise=0.4, bias=50)




def plotLine(theta0, theta1, X, y):
    max_x = np.max(X) + 100
    min_x = np.min(X) - 100


    xplot = np.linspace(min_x, max_x, 1000)
    yplot = theta0 + theta1 * xplot



    plt.plot(xplot, yplot, color='#58b970', label='Regression Line')

    plt.scatter(X,y)
    plt.axis([-10, 10, 0, 200])
    plt.show()



def hypothesis(theta0, theta1, x):
    return theta0 + (theta1*x) 

def cost(theta0, theta1, X, y):
    costValue = 0 
    for (xi, yi) in zip(X, y):
        costValue += 0.5 * ((hypothesis(theta0, theta1, xi) - yi)**2)
    return costValue




def derivatives(theta0, theta1, X, y):
    dtheta0 = 0
    dtheta1 = 0
    for (xi, yi) in zip(X, y):
        dtheta0 += hypothesis(theta0, theta1, xi) - yi
        dtheta1 += (hypothesis(theta0, theta1, xi) - yi)*xi

    dtheta0 /= len(X)
    dtheta1 /= len(X)

    return dtheta0, dtheta1

def updateParameters(theta0, theta1, X, y, alpha):
    dtheta0, dtheta1 = derivatives(theta0, theta1, X, y)
    theta0 = theta0 - (alpha * dtheta0)
    theta1 = theta1 - (alpha * dtheta1)

    return theta0, theta1
    

def LinearRegression(X, y):
    theta0 = np.random.rand()
    theta1 = np.random.rand()
    
    for i in range(0, 1000):
        if i % 100 == 0:
            plotLine(theta0, theta1, X, y)
        # print(cost(theta0, theta1, X, y))
        theta0, theta1 = updateParameters(theta0, theta1, X, y, 0.005)
from sklearn.datasets import make_regressionmath
import matplotlib.pyplot as plt
import numpy as np

X, y= make_regression(n_samples=100, n_features=1, noise=0.4, bias=50)




def plotLine(theta0, theta1, X, y):
    max_x = np.max(X) + 100
    min_x = np.min(X) - 100


    xplot = np.linspace(min_x, max_x, 1000)
    yplot = theta0 + theta1 * xplot



    plt.plot(xplot, yplot, color='#58b970', label='Regression Line')

    plt.scatter(X,y)
    plt.axis([-10, 10, 0, 200])
    plt.show()



def hypothesis(theta0, theta1, x):
    return theta0 + (theta1*x) 

def cost(theta0, theta1, X, y):
    costValue = 0 
    for (xi, yi) in zip(X, y):
        costValue += 0.5 * ((hypothesis(theta0, theta1, xi) - yi)**2)
    return costValue




def derivatives(theta0, theta1, X, y):
    dtheta0 = 0
    dtheta1 = 0
    for (xi, yi) in zip(X, y):
        dtheta0 += hypothesis(theta0, theta1, xi) - yi
        dtheta1 += (hypothesis(theta0, theta1, xi) - yi)*xi

    dtheta0 /= len(X)
    dtheta1 /= len(X)

    return dtheta0, dtheta1

def updateParameters(theta0, theta1, X, y, alpha):
    dtheta0, dtheta1 = derivatives(theta0, theta1, X, y)
    theta0 = theta0 - (alpha * dtheta0)
    theta1 = theta1 - (alpha * dtheta1)

    return theta0, theta1
    

def LinearRegression(X, y):
    theta0 = np.random.rand()
    theta1 = np.random.rand()
    
    for i in range(0, 1000):
        if i % 100 == 0:
            plotLine(theta0, theta1, X, y)
        # print(cost(theta0, theta1, X, y))
        theta0, theta1 = updateParameters(theta0, theta1, X, y, 0.005)


from sklearn.datasets import make_regressionmath
import matplotlib.pyplot as plt
import numpy as np

X, y= make_regression(n_samples=100, n_features=1, noise=0.4, bias=50)




def plotLine(theta0, theta1, X, y):
    max_x = np.max(X) + 100
    min_x = np.min(X) - 100


    xplot = np.linspace(min_x, max_x, 1000)
    yplot = theta0 + theta1 * xplot



    plt.plot(xplot, yplot, color='#58b970', label='Regression Line')

    plt.scatter(X,y)
    plt.axis([-10, 10, 0, 200])
    plt.show()



def hypothesis(theta0, theta1, x):
    return theta0 + (theta1*x) 

def cost(theta0, theta1, X, y):
    costValue = 0 
    for (xi, yi) in zip(X, y):
        costValue += 0.5 * ((hypothesis(theta0, theta1, xi) - yi)**2)
    return costValue




def derivatives(theta0, theta1, X, y):
    dtheta0 = 0
    dtheta1 = 0
    for (xi, yi) in zip(X, y):
        dtheta0 += hypothesis(theta0, theta1, xi) - yi
        dtheta1 += (hypothesis(theta0, theta1, xi) - yi)*xi

    dtheta0 /= len(X)
    dtheta1 /= len(X)

    return dtheta0, dtheta1

def updateParameters(theta0, theta1, X, y, alpha):
    dtheta0, dtheta1 = derivatives(theta0, theta1, X, y)
    theta0 = theta0 - (alpha * dtheta0)
    theta1 = theta1 - (alpha * dtheta1)

    return theta0, theta1
    

def LinearRegression(X, y):
    theta0 = np.random.rand()
    theta1 = np.random.rand()
    
    for i in range(0, 1000):
        if i % 100 == 0:
            plotLine(theta0, theta1, X, y)
        # print(cost(theta0, theta1, X, y))
        theta0, theta1 = updateParameters(theta0, theta1, X, y, 0.005)
from sklearn.datasets import make_regressionmath
import matplotlib.pyplot as plt
import numpy as np

X, y= make_regression(n_samples=100, n_features=1, noise=0.4, bias=50)




def plotLine(theta0, theta1, X, y):
    max_x = np.max(X) + 100
    min_x = np.min(X) - 100


    xplot = np.linspace(min_x, max_x, 1000)
    yplot = theta0 + theta1 * xplot



    plt.plot(xplot, yplot, color='#58b970', label='Regression Line')

    plt.scatter(X,y)
    plt.axis([-10, 10, 0, 200])
    plt.show()



def hypothesis(theta0, theta1, x):
    return theta0 + (theta1*x) 

def cost(theta0, theta1, X, y):
    costValue = 0 
    for (xi, yi) in zip(X, y):
        costValue += 0.5 * ((hypothesis(theta0, theta1, xi) - yi)**2)
    return costValue




def derivatives(theta0, theta1, X, y):
    dtheta0 = 0
    dtheta1 = 0
    for (xi, yi) in zip(X, y):
        dtheta0 += hypothesis(theta0, theta1, xi) - yi
        dtheta1 += (hypothesis(theta0, theta1, xi) - yi)*xi

    dtheta0 /= len(X)
    dtheta1 /= len(X)

    return dtheta0, dtheta1

def updateParameters(theta0, theta1, X, y, alpha):
    dtheta0, dtheta1 = derivatives(theta0, theta1, X, y)
    theta0 = theta0 - (alpha * dtheta0)
    theta1 = theta1 - (alpha * dtheta1)

    return theta0, theta1
    

def LinearRegression(X, y):
    theta0 = np.random.rand()
    theta1 = np.random.rand()
    
    for i in range(0, 1000):
        if i % 100 == 0:
            plotLine(theta0, theta1, X, y)
        # print(cost(theta0, theta1, X, y))
        theta0, theta1 = updateParameters(theta0, theta1, X, y, 0.005)



    


LinearRegression(X, y) 
 
 def LinearRegression (theta1,hypothesis, x ,y , alpha) 
  theta0,hypothesis = derivatives(x,y alpha)  
noise
   LinearRegression(x,y,numpy)


    


LinearRegression(X, y) 
 
 def LinearRegression (theta1,hypothesis, x ,y , alpha) 
  theta0,hypothesis = derivatives(x,y alpha)  
noise
   LinearRegression(x,y,numpy)
    


LinearRegression(X, y) 
 
 def LinearRegression (theta1,hypothesis, x ,y , alpha) 
  theta0,hypothesis = derivatives(x,y alpha)  
noise
   LinearRegression(x,y,numpy)


    


LinearRegression(X, y) 
 
 def LinearRegression (theta1,hypothesis, x ,y , alpha) 
  theta0,hypothesis = derivatives(x,y alpha)  
noise
   LinearRegression(x,y,numpy)
    


LinearRegression(X, y) 
 
 def LinearRegression (theta1,hypothesis, x ,y , alpha) 
  theta0,hypothesis = derivatives(x,y alpha)  
noise
   LinearRegression(x,y,numpy)

    


LinearRegression(X, y) 
 
 def LinearRegression (theta1,hypothesis, x ,y , alpha) 
  theta0,hypothesis = derivatives(x,y alpha)  
noise
   LinearRegression(x,y,numpy)
    


LinearRegression(X, y) 
 
 def LinearRegression (theta1,hypothesis, x ,y , alpha) 
  theta0,hypothesis = derivatives(x,y alpha)  
noise
   LinearRegression(x,y,numpy)

    


LinearRegression(X, y) 
 
 def LinearRegression (theta1,hypothesis, x ,y , alpha) 
  theta0,hypothesis = derivatives(x,y alpha)  
noise
   LinearRegression(x,y,numpy)
xi()
e() 
from math import sqrt
a=-1.;b=88550000.;c=-1.;
y1=(-b+sqrt(b*b-4*a*c))/(2*a) y2=(-b-sqrt(b*b-4*a*c))/(2*a) y1a=2*c/(-b-sqrt(b*b-4*a*c)) y2a=2*c/(-b+sqrt(b*b-4*a*c))
print('Raiz 1 standard=',y1,' Raiz 1 Alternativa=',y1a) print('Raiz 2 standard=',y2,' Raiz 2 Alternativa=',y2a)
>>Raiz 1 = 1.4901161193847656e-08 Sol Alternativa= 1.1293054771315643e-08 >>Raiz 2 = 88549999.99999999 Sol Alternativa= 67108864.0
Tratando-se do primeiro script PYTHON utilizado NamedExpr

f(x1) = (pi/3)*x1*x1*(3*1-x1)-0.5 Valores Iniciais
x1 = 2.500000
x2 = 3.000000
Tolerâncias do Critério de Paragem
   e1 = 1.000000e-02
   e2 = 1.000000e-02
  Número Máximo de NMAX = 3
Iteração 1
xn = 2.923606
fxn = 0.183798 Iteração 2
   xn = 2.944140
  fxn = 0.007048
Iterações
Número de Iterações Realizadas = 2 Solução
   xn = 2.944140
  fxn = 0.007048
f(x1) = 20000*(x1*pot(1+x1,6))/(pot(1+x1,6)-1)-4000 Valores Iniciais
x1 = 0.050000
x2 = 0.150000
Tolerâncias do Critério de Paragem
   e1 = 5.000000e-02
e2 = 5.000000e-02
Número Máximo de Iterações
   NMAX = 4
 Iteração 1
    xn = 0.054437
   fxn = -3.562855
 Iteração 2
    xn = 0.054701
   fxn = -0.210997
 Iteração 3
    xn = 0.054718
   fxn = 0.000042
Número de Iterações Realizadas = 3 Solução
    xn = 0.054718
   fxn = 0.000042
SECANT
Solução de uma Equação Não Linear - Método da Secante Função
f(x1) = pi*pot((300/cos(x1)),2)*0.8/(0.5*pi*14*14*(1+sen(x1)-0.5*cos(x1)))-1200 Valores Iniciais
x1 = 0.000000
x2 = 0.125664
Tolerâncias do Critério de Paragem
   e1 = 1.000000e-03
e2 = 1.000000e-03
Número Máximo de Iterações
NMAX = 4 Iteração 1
    xn = 0.119521
   fxn = -3.331278
... Iteração 3
    xn = 0.117609
   fxn = -0.000252
Número de Iterações Realizadas = 3 Solução
    xn = 0.117609
   fxn = -0.000252
+ Unipo (E do Rio, Do)
E E +1
X = Xo
Lyhile ( c'ac).
OG
Le(9)
for)
friario
contador
def teste(x):
Ex = -1.157407407*10**(-13) * ***4 + 5*10** (-8) *x**2 -3*10**-
12
fdx (-1.157407407*10** (-13)) * 4 * x**3 (5*10** (-8)) *2*x
divisao = fx/fdx
6
return()divisao
while ()(abs ( (xk-xi) /xk)) > e or contador == 500:
= xi
xi = (x).
teste(x)
18
x = xi
19
xk = (%),
teste(x)
20
 funcao (e ,xo ,f(x),p(x));
 e = e + 1
 X = x 0
 while(e > e);
 x  = xo
 while newton raphson
  x = e (x);
  e  = f(x);
x = [1,2,3]
y = [num*2 for num in x]
print(y)
 print(arg1) print(arg1,arg2)
 print(arg1,file=)
 print(arg1,arg2,arg3)
print()
 print(arg1,end=)
 print(arg1,arg2,arg3,arg4)
 print(arg1,arg2,arg3,arg4,arg5)
 print(arg1,flush=)
print(arg1,arg2,arg3,arg4,arg5,arg6)
def f():
    global a
    print(a)
    a = 23

def dummy():
    i=0
    print(i)
    i+=1
     def f():
         global x
         x = 3
         print(x)
#exemplo 2.2
f(x)





k

Bissecção

2,816916

-2,882940x10-5

19

Posição Falsa
class ClassName(object):
    """docstring for ClassName"""
    def __init__(self, arg):
        super(ClassName, self).__init__()
        self.arg = arg
         [a,b], f(xk) e f´(xk)
2,816914
class MetodoNewtonRaphson
def funcionDada(x)
fd = Math.cos(x)
(×**3)
end
def derivadaFuncionDada(x)
d+
=-Math.sin(x)-(3.0*
* x)
end
def solucion()
1 =0
print
"Favor ingresar el valor de x:
x = Integer (gets.chomp)
tempo = 6
while x != tempo && i < 100
tempo
EX
=(
(x
funcionDada(x)/derivadaFuncionDada(x)
tempo)
/ x ).abs
print
, i,
,X,
I=rror
end
if (i == 100)
print
"IninNo converge"
else
end print "Ininsolucion *: .
33
35
36
37
38
39
40
end
end
obj
= MetodoNewtonRaphson.new
obj. solucion()
-7,806591x10-7

24

Newton-Raphson

2,816914

-7,806591x10-7

4

 função f(x)  intervalo [a,b]  [a,b]. Desde que f(x)
  [a,b], f(xk) e f´(xk)

Tabela 2: Zero aproximado da função da equação (7)

f(x)







Bissecção

-0,999999

-2,098612x10-8

20

Posição Falsa

-1,000001

-2,098612x10-8

17

Newton-Rapshon

-1,000000

0

5

S = [
    [ 2,  1, -3],
    [ 1, -2,  1],
    [-1,  1, -2]
]
b =  [ [-3.11], [8.07], [-6.18]]

A = np.column_stack((S, b)).astype(float) # matriz ampliada

print(A)


A_1 = np.copy(A)
A_1[1] = np.round(A[0] * (-0.5) + A[1], 3)
A_1[2] = np.round(A[0] * (0.5) + A[2], 3)

print("A_1")
print(A_1)

A_2 = np.copy(A_1)
A_2[2] = np.round(A_1[1] * (0.6) + A_1[2], 3)

print("A_2")
print(A_2); 
 
 return ()
