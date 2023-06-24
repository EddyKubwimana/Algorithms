def list_n(number):
    '''Print numbers from 0 to n given number'''

    if number==0:
       print(number, end = ",")
       return number
    else:
       list_n(number-1)
       print(number, end = ",")
    
list_n(10)
