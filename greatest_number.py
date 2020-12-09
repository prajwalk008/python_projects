# Programme to find largest of three numbers.

a,b,c= input("Enter three numbers(Leave a comma between them):").split(",")

if(int(a) > int(b) and int(a) > int(c)):
    l= a

elif(int(b) > int(a) and int(b) > int(c)):
    l= b

else:
    l= c

print("Largest of three numbers is-", l)
    




