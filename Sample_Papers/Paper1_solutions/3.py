'''Write a Python Program to find the frequency of each character in string using dictionary comprehension.
Sample input
banana
Sample Output
{'b': 1, 'a': 3, 'n': 2}
'''
a=input()
l=list(a)
e=list(set(l))
c=[i for i in l if i in e]
print(c)
d={}
[d.update({c[i]:l.count(c[i])}) for i in range(len(c))]    
print(d)
