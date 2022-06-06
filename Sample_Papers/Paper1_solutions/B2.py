'''
Write a python program to find the maximum value in each row of a numpy 2D array and place it to the end of the each row?
Sample input
[[3 5 7]
[4 8 2]
[1 8 6]]
Sample Output 
[[3 5 7]
[4 2 8] 
[1 6 8]]
'''
import numpy as np
ar=eval(input("Enter a 2D array: "))
a=np.array(ar)
for i in range(len(a)):
    x=max(a[i])
    for j in range(len(a[i])):
        if x==a[i][j]:
            a[i][j]=a[i][(len(a[i])-1)]
            a[i][len(a[i])-1]=x
            break
print(a)
