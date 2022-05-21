num=int(input('Enter a number:'))
flag=False
for x in range(2,num):
    if num%x==0:
        flag=True
        break
if flag:
    print('It is not prime')
else:
    print('It is prime')