#1. Input list, sum all elements.
lst=[]
sum=0
for i in range(0,int(input("Enter length of list: "))):
    lst.append(int(input()))
for i in lst:
    sum=sum+i
print(sum)