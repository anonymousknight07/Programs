#All character in list of tuple checking 
# tuplist=[('GFG','IS','BEST'),('GFg','AVERAGE'),("GFG",),("Gfg","CS")]
# newlist=[]
# for sub in tuplist:
#     res=True
#     for ele in sub:
#         if not ele.isupper():
#             res=False
#             break
#     if res:
#         newlist.append(sub)
# print("THE ORIGINAL LIST WAS",tuplist)
# print("THE NEW LIST IS ",newlist)

'''METHOD 2 -COMPRENESATION OF List'''

tuplist=[('GFG','IS','BEST'),('GFg','AVERAGE'),("GFG",),("Gfg","CS")]
res=[sub for sub in tuplist if all(ele.isupper()for ele in sub)]
print("THE ORIGINAL LIST IS ",tuplist)
print("THE NEW LIST IS ",res)