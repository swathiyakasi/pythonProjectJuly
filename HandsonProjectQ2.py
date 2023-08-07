N = [11,22,56,78,34,23,45,57,45,60]
print(N)
print("the first element in the list N- ",N[0])
print("the last three elements in the list ",N[-3:])

#Question: 3 (doubt)
#print(N)
print ("Question 3 Start")
a = range(50)
print(a)
for i in a:
   # print ("Before",i)
    if i%5 == 0:
        print(i)

print("Question 3 End")

#Question: 4
L = ["Apple",78,908.39]
N = int(input("enter a number : "))
L.append(N)
print(L)

#question: 5
list = [12,"a",34,7.8,"ball","car"]
x = int(input("enter a number:"))
for i in range(x):  #since the integer is not iterble we are using range function
    print(list)



