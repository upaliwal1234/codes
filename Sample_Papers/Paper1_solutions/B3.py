'''
Implement the following mathematical expression using Python and display the value of x after taking values of a, b and c from the user.
𝑥 = −𝑏 ± √𝑏2 − 4𝑎𝑐 Consider a, b and c are number.
'''
a,b,c=map(int,(input("Enter the value of a, b, c: ")).split())
x1=(-b+(b**2-4*a*c)**0.5)/(2*a)
x2=(-b-(b**2-4*a*c)**0.5)/(2*a)
print(f"The values of x are: {x1} and {x2}")
