#EXCESSIVE NUMBER

n=int(input("Enter the number which is to be checked (excessive number or not )"))
sum=0
for i in range(1,n):
    if n%i==0:
       sum=sum+i

if sum>n:
    print(n, "is an excessive number")
else:
    print("Sorry" ,n, "it isnt an excessive number")
