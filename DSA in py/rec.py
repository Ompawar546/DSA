#addition of n nums
def addN(n):
    if n==0:
        return 0
    else:
        return n+addN(n-1)

x = int(input("enter a number "))
z= addN(x)
print(z)

"""
when called second time inside itself the n value will be n-1
so
n*n-1
n*n-1*n-2
n*n-1*n-2*n-3.....
"""


# power of function using rec
def powerOf(n,p):
    if p==0:
        return 1
    else:
        for i in range(p):
            return n*powerOf(n,p-1)
    
num = int(input("enter a number "))
power = int(input("enter its power "))  

print(powerOf(num,power))
