#Use a list comprehension to square of each odd number in a kist. The list in input by user in a sequence of space-separated numbers.
l=list(map(int,input().split()))
l1=[]
for i in l:
    if i%2!=0:
        l1.append(i**2)
print(l1)
