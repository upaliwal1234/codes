#WAP to find whether a given string sarts with a given character or not using lambda funcion(Hint: use startswith() method.)
fun=lambda n,a:n.startswith(a)
st=input("Enter a string: ")
a=input("Enter a character: ")
if fun(st,a):
    print("True")
else:
    print("False")
