def validity(a,b,c):
    if a+b>c and a+c>b and b+c>a :
        return 1
def define(a,b,c):
 if validity(a,b,c):
        if a==b==c:
           print("It's a Equilateral Triangle")
        elif a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a :
            print("It's Right Angled Triangle")
            if(a>b and b>c):
                radius=a/2
            elif(b>a and a>c):
                radius=b/2
            else : radius = c/2
            print(f'Radius of the circumcentre would be {radius}')
        elif a==b or b==c or a==c :
            print("It's a Isoceles Triangle")
        else :
            print('Scalene')
a=int(input('Enter the Side of the triangle :'))
b=int(input('Enter the Side of the triangle :'))
c=int(input('Enter the Side of the triangle :'))
define(a,b,c)
