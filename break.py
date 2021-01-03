c= int(input("How many Candies:"))
av=10
for i in range(1,c+1):
    if i>av:
        print("Out of stock")
        break
    print("Candy")