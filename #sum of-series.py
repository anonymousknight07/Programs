#SUM OF SERIES (n!/n)

n=int(input("enter the number to find the sum of the series"))
factorial=1
sum=0
for i in range (1,n+1):
    factorial*=i
    sum=sum+i/factorial

print(sum)