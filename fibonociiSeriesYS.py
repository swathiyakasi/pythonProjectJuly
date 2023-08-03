x = 100
a = 0
b = 1
strFib = str(a) + "," + str(b)
#print(a)
#print(b)
c = 1
while (c <= x):
   c = a+b
   if c <= x:
      strFib=strFib + "," + str(c)
      #print(c)
      a = b
      b = c
print ("Horizontal printing: ",strFib)





