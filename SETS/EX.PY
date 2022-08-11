# a = {2,3,4,5,2} #dont consider repeted items
# print(type(a))
# print(a)

# this syntex will be create only empty dictionary nat an set
# a = {}
# print(type(a))
# an empty set can be creted using this syntex
b = set()
print(type(b))

# set method
b.add(3)
b.add(6)
b.add(5)
print(b)
# b.add([2,3,4,5,]) #we cant add list in set
# b.add({4:5})  #we cant add dictionary in set
print(len(b))  #print the lenth of set
b.remove(5)
print(b)