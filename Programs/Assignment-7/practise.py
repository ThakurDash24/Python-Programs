a=int(input("enter the side of trinagle :"))
b=int(input("enter the side of trinagle :"))
c=int(input("enter the side of trinagle :"))
def validity(a, b, c):
    if a+b>c:
        return True
    elif b+c>a:
        return True
    elif c+a>b:
        return True
    else:
        return False

def circumcentreeadius(a, b, c):
    if (a>b and b>c):
        return a/2
    elif(b>a and a>c):
        return b/2
    else:
        return c/2

if(validity):
    if a==b and b==c:
        print("triangle is equilateral ")
    elif (a==b and b!=c )or (b==c and b!=a) or (a==c and a!=b) :
        print("triangle is isoscales")
    elif a**2==b**2+c**2 or b**2==a**2+c**2 or c**2==a**2+b**2 :
        print("it is a right angle triangle ")
        radius=circumcentreeadius(a, b, c)
        print(f"the radius of the circumcentre triangle is {radius}")
else:
    print("it is a scalene triangle ")