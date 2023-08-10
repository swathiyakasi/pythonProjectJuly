#Handson Project1 question 2
N = [11,22,56,78,34,23,45,57,45,60]
print(N)
print("the first element in the list N- ",N[0])
print("the last three elements in the list ",N[-3:])

# Hands on Project 1 Question: 3
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

#Question 6
#list_letters = ["d","g","t","u","l"]
#list_letters.insert(1,"k")
#print(list_letters)
#print(len(list_letters))


# create empty list
x = []

#no of elements in the list
y = int(input("enter a number : "))

#input numbers into the list
for i in range(0,y):
    print("enter a number at index:" ,i)
    e = int(input())
    #adding elements to list

    x.append(e)
print(x)
q = int(input(":enter a  index number: ",))
print(x[q])



