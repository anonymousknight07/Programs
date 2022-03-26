#Write program to find binomal coeffi. value (ncr) by taking n and r as input using a function for factorial of a number.



def factorial(n):
     f=1
     if n==0 or n==1:
         return f
    
     for i in range(2 , n+1):
            f=f*i
     return f

n1=int(input("Provide values of n "))
r1=int(input("Provide values for r "))
ncr=(factorial(n1))/(factorial(n1-r1)*factorial(r1))
print("Binomial coefficient ncr for n={} and r={} is:{}".format(n1,r1,ncr))

