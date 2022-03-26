#PATTERN 0 12 345 

n=int(input("Enter the rows "))
num=0
for i in range(1,n+1):
    for j in range(1,i+1):
        print(num ,end=" ")
        num=num+1

    print()