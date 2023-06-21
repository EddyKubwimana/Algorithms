def printif(number):
    if number == 0:
        return number
    else:
        return  printif(number-1)
        
    
print(printif(10))
        