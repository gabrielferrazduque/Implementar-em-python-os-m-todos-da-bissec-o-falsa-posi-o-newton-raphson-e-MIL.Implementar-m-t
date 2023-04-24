#exemplo 2.2 
import math 
math.random = math.random 
math.randomseed= math.random 
float(caculado_producto + 1 + float()) 
math.cos (carculado_percentage+)
math.sin (x - float(carculado+)) 
 
number_1 = input('Enter your first number: ')
number_2 = input('Enter your second number: ')
Enter your first number: 5
Enter your second number: 7 
  
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
print(A_2)
