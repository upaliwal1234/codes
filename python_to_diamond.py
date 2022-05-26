row=int(input("Enter the numebr of rows :"))
for i in range(1,row+1):
    for j in range(row-i):
        print(" ",end='')
    for j in range(i):
        print("*",end='')
    for j in range(i-1):
        print("*",end='')
    print()
    for i in range(1,row+1):
        for j in range(i-1):
            print(" ",end='')
        for j in range(row+1-i):
            print("*",end='')
        #for j in range(row-i):
         #  print("*",end='')
    print()