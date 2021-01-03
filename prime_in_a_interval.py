a= int(input("Enter the initial number:"))
b= int(input("Enter the final number:"))

print("prime numbers between",a,"and",b,"-")


for i in range(a,b+1):
    for j in range(2,i):
        if i%j == 0:
           break
    else:
        print(i)
        
