def printf(number):
    '''Print numbers from 0 to n given number'''

    if number==0:
       print(number, end = ",")
       return number
    else:
       printf(number-1)
       print(number, end = ",")
    
printf(10)
