#Removing duplicate object from list

listnum=[]
n=int(input("Enter number of elements in list "))
for i in range(n):
    listnum.append(int(input("Enter list element ")))
print("The list of elements are ,",listnum)

finallist=[]
for num in listnum:
    if num not in finallist:
        finallist.append(num)
print("List after deleting the duplicate element is ", finallist )