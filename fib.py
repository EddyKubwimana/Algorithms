def fibonacci(number, found = {0:0, 1:1}):
    if number in found:
        return found[number]
    else :
       result= fibonacci(number-1,found)+fibonacci(number-2, found)
       found[number] =result
       return found[number]



#utilazation of memoization concept
def fib(n, d = {0:0, 1:1}):

    
    if n in d:
        return d[n]
    else:
        ans = fib(n-1,d)+ fib(n-2,d)
        d[n] = ans
        return d[n]
    




#....................test.........................#


print(fibonacci(200))