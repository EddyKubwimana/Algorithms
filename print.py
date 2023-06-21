def printif(number):
    '''
    print a number given a certain limit
    return
    '''
    if number == 0:
        return number
        
    else:
        printif(number-1)
        print(number-1, end = ",")
        return number
        
print(printif(100))
        