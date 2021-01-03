import math

a= input("This is a programme to find area of any possible triangle!, Wanna try??")
if a==("Yes" or "yes"):
    i = int(input("What do u know about the triangle(Write only option number.) - 1. Three sides, 2. base and height, 3. 2-sides and 1-angle., 4. equilateral triangle, 5. Right triangle."))
    if i==1:
        a= float(input("enter side a:"))
        b= float(input("enter side b:"))
        c= float(input("enter side c:"))

        s= a+b+c/2

        Area1= (s)*(s-a)*(s-b)*(s-c)
        print("Area of this triangle is",math.sqrt(Area1))

    if i==2:
        a= float(input("Enter base:"))
        b= float(input("Enter height:"))

        Area = a*b/2
        print("Area is",Area)

    if i==3:
        a= float(input("Enter side a:"))
        b= float(input("Enter side b:"))
        c= float(input("Enter angle(in degree) which is between two sides:"))
        e= (c*math.pi)/180

        d= math.sqrt(a**2 + b**2 -2*a*b*(math.cos(e)))

        s= a+b+d/2

        Area1= (s)*(s-a)*(s-b)*(s-d)
        print("Area of this triangle is",math.sqrt(Area1))

    if i==4:
        a= float(input("Enter the side:"))

        Area= (math.sqrt(3)*(a**2))/4
        print("Area of this triangle is",Area)

    if i==5:
        a= float(input("Enter the hypotenuse:"))
        b= float(input("Enter the other side:"))

        c= math.sqrt((a**2)-(b**2))

        Area= (b*c)/2
        print("Area of this triangle is",Area)

else:
    print("All right more interesting programms on ur way!")


    


