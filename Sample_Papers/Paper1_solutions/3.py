'''Write a Python Program to find the frequency of each character in string using dictionary comprehension.
Sample input
banana
Sample Output
{'b': 1, 'a': 3, 'n': 2}
'''
a=input()
l=list(a)
d={}
[d.update({l[i]:l.count(l[i])}) for i in range(len(l))]    
print(d)
