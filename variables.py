x = 5
y = "john"
print(x)
print(y)
x  = 4 #x is of type int
x = "salary" #y is string data type

print(x)
x = str(3)    #x will be '3'
y = int(3)    #y will be 3
z = float(3)  #z will 3.0
print(x)
print(y)
print(z)

x = 45
y = 606.78
z = True
a = "i am a good girl"
print(type(x))
print(type(y))
print(type(z))
print(type(a))

x = "john"
# is the same as
x = 'john'
print(x)
carname = 'Volvo'
print(carname)
x = 5
print(type(x))
print(type(5))
x = "Hello World"
print(type(x))
x = 20
print(type(20))
x = 20.5
print(type(x))
x = 1j
print(type(x))

x = ["apple","banana","cherry"]
print(type(x))

x = ("apple","banana","cherry")
print(type(x))

x = range(6)
print(type(x))

x = frozenset({"apple","banana","cherry"})
print(type(x))

x = True
print(type(x))

x = b"hello"
print(type(x))

x = 1
#y = "tel:1233677889">566909900990000
z = -34567898

print(type(x))
print(type(y))
print(type(z))

import random
print(random.randrange(1,10))

x = 5
x = float(x)
print(type(x))

thislist = ["apple","banana","cherry"]
print(thislist)

#list values are ordered,changeble and allow duplicate values
#list items are indexed

thislist = ["apple","banana","cherry","apple","cherry"]
print(thislist)
print(len(thislist))

list = ["apple","banana","cherry"]
list2 = [1,2,3,4,5]
list3 = [True,False,False]
print(list)
print(list2)
print(list3)

mylist = ['pan cakes',"dosa","vada","idly"]
print(mylist)
print(type(mylist))

thislist = ["app","soft","theory","null"]
print(thislist[1])
print(thislist[3])
thislist = {1,3,4,56,78,43,12,56}
print(thislist)
#print(thislist[1])
fruitlist = ["apple","banana","grapes","orange","cherry","mango","cucumber"]
print(fruitlist[2:5])

print(fruitlist[:4])
if "apple" in fruitlist:
    print("yes")
if "grapes" in fruitlist:
    print("ok")
list = [1,2,3,4,5,7,8,9]
list[1:3]=[0,11,12]
print(list)
list.insert(3,"a")
print(list)
list.append(111)
print(list)
list.pop()
print(list)



thistuple = ("apple", "banana","orange",1,2,3,4,2,1)
print(thistuple)
print(type(thistuple))
print(len(thistuple))
print(thistuple[0])
print(thistuple[0:4])
print(thistuple[-4:-2])
if 5 in thistuple:
    print("yes")
else:
    print("no")

for x in range(6):
    print(x)
else:
    print("finised")

for x in range(6):
    print(x)


adj = ["red","big","tasty"]
fruits = ["apple","banana","orange"]
for x in adj:
 for y in fruits:
   print(x,y)


for x in [0,1,2]:
    pass
