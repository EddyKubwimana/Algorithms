def printif(number):
    if number == 0:
        return number
    else:
        number=  printif(number-1)
        print(number, end =" ")
        return number+1
        
    
print(printif(100))
        