#A neon number is a number where the sum of digits of square of the number is equal to the number
num=int(input('Enter a number: '))
sum=0
x=num**2
#for x in range(x,0):
while x>0:
    a=x%10
    x=x//10
    sum=sum+a
if sum==num:
    print('It is a neon number')
else:
    print('It is not a neon number')