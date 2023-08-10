#Critical if condition program


x = int(input("enter number of units = "))
for i in  range(0 , x):
    if (x <= 50):
      charges1 = 50 * 2
      print("charges= ",charges1)
    if(x> 50 and x <=150 ):
       remaning_units1 = x-50
       if (remaining_units1 > 100):
           charges2 = 100*3
       else:
           charge2 = remaining_units1 * 3
    total = (charges1 + charges2 ) * 0.2
    print("total")
    #if (units >150 and units <=250):
     #   remaining_units2 = units - 150
     #   if(remaining_units):
