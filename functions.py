#functions are block of codes we can use them when ever we want ,by calling the function

# functions with variables



def marks():
    english = 80
    math = 89
    print("totalmmarks : ",english+math)

marks()

def sub():
    a = 45
    b = 34
    c = a-b
    print("the subtraction of 45 and 34:",c)

sub()


#function with parameters a,b

def add(a,b):
    c = a+b
    print("the sum of a,b =",c)

def sub(a,b):
    c = a-b
    print("the subtraction of a,b :", c)

add(2,3)
sub(2,3)

#function with return value

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(2))

def add2(a,b):
    return(a+b)

out = add2(2,5)
print(out+40)

def mul(a,b):
    return(a*b)

c = mul(45,2)
print(c)
