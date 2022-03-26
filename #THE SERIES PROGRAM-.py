#THE SERIES PROGRAM-

n=int(input("Enter the number to start the series sum "))
sum=0
for i in range (1,n):
    sum=sum+(1/i)
print(round(sum,2))