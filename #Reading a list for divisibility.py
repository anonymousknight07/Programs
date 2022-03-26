#Reading a list for divisibility

x=int(input("Enter value to check for divisibility "))
y=int(input("Enter value to check for non divisibilty "))
listnum=[]
newlist=[]
n=int(input("Enter the number of elements in the list "))
for i in range(n):
    listnum.append(int(input("Enter list element ")))
print("The list of element are: ",listnum)

for i in listnum:
    if(i%x==0 and i%y!=0):
        newlist.append(i)
print("Element satisfying given condition;",newlist)