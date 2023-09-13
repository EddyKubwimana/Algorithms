def reverse(word):
    reversed = ""
    for i in range (len(word)-1,-1,-1):
        reversed=reversed+word[i]
    return reversed


# .....................testing.............................

name = 'Kubwimana    ***   333   hfhf  Eddy'
print(reverse(name))