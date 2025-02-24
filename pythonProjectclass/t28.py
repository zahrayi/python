
def fac(n,c):
    for i in range(1,n+1):
     c=c*i
    return c


n = int(input("enter a num: "))
a = fac(n,1)
print(a)