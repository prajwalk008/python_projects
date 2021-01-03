for i in range(1,5):
    for j in range(1,6-i):
        print(j,end="")
    print()

''' Here i is in the range 1-->5. then j is the range
1-->6-1,1-->6-2 etc. 
so j is in the range (1,4); (1,3)
then we print j with end ="", that leaves no space in 
j. finally  print() completely prints i.'''

for i in range(1,20):
    for j in range(1,i+1):
        print("*",end="")
    print()

