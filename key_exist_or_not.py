'''Write a Python script to check if a given key already exists in a dictionary.'''
d={"a":12,"b":303,"c":323}
a=input("Enter a key to check: ")
x=0
for i in d:
    if a==i:
        x=1
        print(i)
        print("Key is present in dictionary")
        break
if x==0:
    print("key is not present in dictionary")
