P = 100 #Principal
t = 10 #time
i = 0.03
A = P * (1 + i)**t
print(A)

P = 1
t = 1
i = 1
n = 60*24*365
A = P * (1+i/n)**(t*n)
print(A)

from math import exp
print (exp(1))