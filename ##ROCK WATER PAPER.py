##ROCK WATER PAPER


import random

def game(comp , You):
    if comp==You:
        return None
    elif comp=='Rock':
         if You=='Paper':
             return True
         elif You=='Scissor':
             return False 
    elif comp=='Scissor':
         if You=='Paper':
             return False
         elif You=='Rock':
             return True 
    elif comp=='Paper':
         if You=='Rock':
             return False
         elif You=='Scissor':
             return True 
print("COMPUTER-Rock, Paper or Scissor")
num = random.randint(1 , 3)
if num==1:
    comp='Rock'
elif num==2:
    comp='Scissor'
elif num==3:
    comp='Paper'

You=input("ENTER Rock, Paper OR Scissor  ")
x=game(comp , You)

print(f"Computer choose {comp}")
print(f"You choose{You}")

if x==None:
    print("GAME IS TIED")
elif x:
    print("YOU HAVE WON!!")
else:
    print("Sorry, You lose!! Try again")
