#ARMSTRONG NUMBER

n=int(input("Enter the number to check"))
sum=0
order=len(str(n))
du_n=n
while(n>0):
    digit=n%10
    sum+=digit**order
    n=n//10
if (sum==du_n):
    then:print("it is an armstrong number")
else:
    print ("Not an Armstrong number")
   
