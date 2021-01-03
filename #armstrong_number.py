#armstrong_number

a= int(input("Enter a three digit number:"))

i= a//100
j= (a%100)//10
k= a%10

sum= (i**3)+(j**3)+(k**3)

if a==sum:
    print(a,"is a armstrong number")
else:
    print(a,"is not a armstrong number")