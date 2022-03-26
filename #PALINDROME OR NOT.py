#PALINDROME OR NOT

n=int(input("Enter a number "))
output=0
reverse=0
du_n=n
while (n>0):
    number=n%10
    output=output+number
    reverse=(reverse*10)+n%10
    n=n//10
print("The sum of the digits of the given is,-",output)
print("The number that we get after reversing the digits are,-" ,reverse)
if (du_n==reverse):
    print(du_n, " is an palindrome")
else:
    print("Sorry this number isnt a palindrome.Enter  NEW NUMBER")