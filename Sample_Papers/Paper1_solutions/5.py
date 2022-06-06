'''
Write a Program to check whether given number is prime or not.
'''
a=int(input())
i=2
t=True
while i<=a//2:
    if a%i==0:
        t=False
        break
    i+=1
if t:
    print("It is prime")
else:
    print("It is not prime")
