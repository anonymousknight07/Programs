#SECOND LARGEST NUMBER-

n=int(input("ENTER THE NUMBER YOU WANT IN THE LIST "))
list=[]
for i in range(0,n):
    k=(input("ENTER THE NUMBER TO BE IN THE LIST "))
    list.append(k)
print("THE LIST IS",list)
newlist=set(list)
newlist.remove(max(newlist))
z=max(newlist)
print("The second largest element is",z)