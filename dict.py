mydict = {}

name= "eddykubwimana"
numbers = [1,1,0,0,4,8,9,9]

for i in range(len(name)):
    mydict[name[i]] = name[i]


print(mydict)
print(list(mydict.values()))
print(list(mydict.keys()))
print(list(set(numbers)))
print(name[:-1])
print(name[1:])


