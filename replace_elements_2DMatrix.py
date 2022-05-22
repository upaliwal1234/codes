'''
Write a python program to replace the elements of given 2D numpy array (Matrix) by 0 if
elements is not divisible by constant number 3.
Sample Input
22 #RC
47 #RI
62 #R2
Sample Output
[[0 0]
[6 0]]
'''
import numpy as a
r,c=map(int,input().split())
l=[]
for i in range(r):
    l2=[]
    l2.extend(map(int,input().split()))
    l.append(l2)
print(l)
arr=a.array(l)
for i in range(r):
    for j in range(c):
        if arr[i,j]%3!=0:
            arr[i,j]=0
print(arr)
