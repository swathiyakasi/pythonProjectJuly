#question : 6
list_letters = ["d","g","t","u","l"]
list_letters.insert(1,"k")
print(list_letters)
print(len(list_letters))


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
