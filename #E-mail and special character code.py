#E-mail and special character code

vowels = ['a', 'e', 'i', 'o', 'u']
str = input("Enter a string: ").lower()
v_ctr = 0
c_ctr = 0
spaces=0
number=0
for x in str:
    if x in vowels:
        v_ctr += 1
    elif x != ' ':
        c_ctr += 1
    elif x==' ':
        spaces+=1
    elif x==1:
        number+=1  
    elif x==2:
        number+=1
    elif x==3:
        number+=1
    elif x==4:
        number+=1
    elif x==5:
        number+=1
    elif x==6:
        number+=1
    elif x==7:
        number+=1
    elif x==8:
        number+=1
    elif x==9:
        number+=1
    
    
print("Vowels: ", v_ctr)
print("Consonants: ", c_ctr)
print("Spaces ", spaces)
print("Number ",number)