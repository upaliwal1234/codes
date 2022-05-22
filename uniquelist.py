#Write a Python function that takes a list and returns a new lost with unique elements of the first list.
def unique(l):
    l1=list(set(l))
    return l1

l=list(map(int,input().split()))
print(unique(l))
