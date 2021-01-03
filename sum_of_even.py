#sum of even below a number

n=int(input("enter a number:"))
f=0

for i in range(1,n+1):
    if i%2==0:
        f=i+f
print(f)


