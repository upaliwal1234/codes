#Write a Python program to sum all the items in a dictionary.
x={'a': 10, 'b': 20, 'c': 30}
s=0
for i in x.values():
    s+=i
print("Sum of all the items is: ",s)
