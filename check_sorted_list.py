'''Write the following function body that returns True if the list is already sorted in
ascending order'''
def isSorted(l):
    res=sorted(l)
    if res==L:
        return True
    else:
        return False
L=list(map(int,input().split()))
print(isSorted(L))
