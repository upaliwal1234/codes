'''
Write a Python program for the addition of two nested lists 4 (matrices) using List Comprehension.
'''
l1=[[1,2],[3,4]]
l2=[[5,6],[7,8]]
l3=[]
for i in range(len(l1)):
    l=[]
    [l.append(l1[i][j]+l2[i][j]) for j in range(len(l1))]
    l3.append(l)
print(l3)
