#WAP to shuffle a list using random module
import random
l=input("Enter a space seperated list: ")
a=list(map(int,l.split()))
random.shuffle(a)
print(a)
