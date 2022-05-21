num=int(input("Enter a numebr: "))
first=num//10**(len(str(num))-1)
last=num%10
sum=first+last
print(sum)