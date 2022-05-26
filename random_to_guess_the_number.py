import random
a=eval(input('Enter the number writen by the system : '))
while 1:
    b=eval(input('Enter the number by the user : '))
    if b>a:
        print('Number is large')
    elif b<a:
        print('Number is smaller ')
    else:
        print('answer is correct')