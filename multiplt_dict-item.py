#Write a Python program to multiply all the items in a dictionary.
x={'a': 10, 'b': 20, 'c': 30}
s=1
for i in x.values():
    s=s*i
print("Sum of all the items is: ",s)
