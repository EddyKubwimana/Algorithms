def list_n(number):
    '''Print numbers from 0 to n given number'''

    if number==0:
       print(number, end = ",")
       return number
    else:
       list_n(number-1)
       print(number, end = ",")


def factoriel(number):
   ''' 
   Takes a number,
   return  a factoriel of that number


   '''
   if isinstance(number, int) and number >= 0:
      if number == 0:
         return 1
      else:
         return number*factoriel(number-1)
   else:
      ValueError("factoriel can be found on positive integer numbers")
      




#...........................................................................#  
#.....................Testing of the function...............................#
    
list_n(10)

print(factoriel(10))
