def fib(n) :
    a = 0
    b = 1
    print(a)
    print(b)

    for i in range(0, n):

        c = a + b
        a = b
        b = c
        print(c)

fib(n)




#fib with if else statement:
def fib(n) :
    a = 0
    b = 1

    if n == 1:
        print(a)

    else:
        print(a)
        print(b)

        for i in range(2, n):

            c = a + b
            a = b
            b = c
            print(c)
            
            
            
            
           
        
 
#is it fibbinocci num or not:
import math
def perfectsquare(x) :
    s = int (math.sqrt(x))
    return s*s==x
n = int(input('enter the number:'))
result1 = 5*(n*n)+ 4
result2 = 5*(n*n)+ 4

if perfectsquare(result1) or perfectsquare(result2):
    print(n, 'is fibonacci number')
else:
    print(n, 'is not fibonacci number')
        
