n=int(input("Enter the number of rows  "))
b=int(input("Enter the number of column  "))
for i in range(n):
    for j in range(b):
        if (j%2==0):
            print('0',end="")
        else:
            print('1',end="")
    print()