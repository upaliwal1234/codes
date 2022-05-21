num=int(input("Emter a number: "))
rev=0
while num>0:
    a=num%10
    num=num//10
    rev=rev*10+a
print(rev)