#check whether a number is Strong/Krishnamurthy/Robinson/Peterson or not
num=int(input('Enter a number to check whether it is is strong or not: '))
sum=0
n=num
while num>0:
    a=num%10
    num=num//10
    x=a
    fact=1
    while x>0:
    #for x in range(a,0):
        fact=fact*x
        x=x-1
    sum=sum+fact
if(sum==n):
    print('It is Strong')
else:
    print('It is not strong')