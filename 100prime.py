#print firstt 100 prime number.
i=1
for x in range(2,1000):
    flag=0
    if i>100:
        break
    for y in range(2,x):
        if x%y==0:
            flag=1
            break
    if flag==0:
        print(x)
        i=i+1