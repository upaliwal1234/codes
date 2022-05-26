#WAP to filter a list of integers using a lambda function(Filter all even numbers)
fun=lambda n:n%2==0
l=list(map(int,input().split()))
l1=list(filter(fun,l))
print(l1)
