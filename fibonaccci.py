n= int(input("Enter the fibonacci limit"))

s=0
a=1
b=1
print(s,a,end=" ")
while b<=n:
    print(b,end=" ")
    s=a
    a=b
    b=a+s


# to print fibonacci series to a number of terms
n= int(input("Enter no. of terms"))

s=0
a=1
b=1
i=1
print(s,a,end=" ")
while i<n:
    print(b,end=" ")
    s=a
    a=b
    b=a+s
    i=i+1
