num=int(input("Enter a number to find it's factorial: "))
fact=1
while num>0:
    fact=fact*num
    num=num-1
print(fact)