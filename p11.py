#Pattern 11
a=1
j=int(input("Enter no. of rows: "))
j=(j+1)//2
sp=j-1
for i in range(0,j):
    print("  "*sp+" *"*a,end='')
    sp-=1
    a+=2
    print("\n")
sp=1
a=a-4
for j in range(j-1,0,-1):
    print("  "*sp+" *"*a,end="")
    sp+=1
    a-=2
    print("\n")