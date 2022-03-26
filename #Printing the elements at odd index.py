#Printing the elements at odd index 

listnum=[]
newlist=[]
n=int(input("Enter number of elements in list "))
for i in range(n):
    listnum.append(int(input("Enter list element ")))
print("The elements of the list are ",listnum)

for i in range(n):
    if(i%2==1):
        newlist.append(listnum[i])
print("The element of the list at odd position are ",newlist)


