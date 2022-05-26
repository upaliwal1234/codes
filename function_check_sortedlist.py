#define a function to check whether the list is sorted or not.
def isSorted(L):
    l=L.copy()
    l.sort()
    if l==L:
        print("It is alread sorted")
    else:
        print("It is not sorted")

print("Enter a list: ",end="")
l=list(map(eval,input().split()))
isSorted(l)
