# write a function that find the largest string that start with a and end b

def findpolindrome(word):
    if len(word)==1 or len(word)==0:
        return True
    else:
        return findpolindrome(word[1:])==findpolindrome(word[:-1])
    

#..................................testing...........................................#
name = "rjddk"

print(findpolindrome(name))

    

