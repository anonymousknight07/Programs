
'''Method one'''
# tuplist=[(6,24,12),(60,12,6),(12,18,21)]
# print("The intial list",tuplist)
# k=int(input("ENTER THE NUMBER TO CHECK THE DIVISIBILTY "))
# res_newlist=[]
# for sub in tuplist:
#     res=True
#     for ele in sub:
#         if ele%k!=0:
#             res=False
#             break
#     if res:
#         res_newlist.append(sub)

# print("List of element divisible by K is ",res_newlist)
        
'''Method two-using list comprehension'''

tuplist=[(6,24,12),(60,12,6),(12,18,21)]
k=int(input('Enter the number to be checked for divisibility '))
print("The original list is",tuplist)
newlist=[tup for tup in tuplist if all(values%k==0 for values in tup)]
print("The new list is ",newlist)

