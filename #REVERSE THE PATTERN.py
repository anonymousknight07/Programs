#REVERSE THE PATTERN

n=int(input("Enter the number of rows  "))
b=int(input("Enter the number of column  "))
for i in range(n+1,0,-1):
    for j in range(0,i-1):
        print("*",end="")
    print()