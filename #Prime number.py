
#PRIME AND NON-PRIME NUMBER

n=int(input("Enter the number"))

for i in range(2,n):
       if (n%i)==0:
         print("it is not prime")
         break
else:
      print("it is prime")
