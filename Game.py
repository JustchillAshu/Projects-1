from random import *
#Rock paper  scissor with comp
def game(comp, you):#making matches
    if comp==you:#in case of tie
        return None
    elif comp =='r':
        if you =='s':
            return False
        elif you =='p':
            return True
    elif comp =='p':
        if you=='r':
            return False
        elif you=='s':
            return True
    elif comp=='s':
        if you=='r':
            return True
        elif you=='p':
            return False


print("Computer Turn: Rock(r),Paper(p)and Scissors(s) ")
randno=randint(1,3)#assignning keys
if randno==1:
    comp="r"
elif randno==2:
    comp="p"
elif randno==3:
    comp="s"
player=input("player Enter your Name:")


you=input('''Your Turn:\nFor Rock type r\nFor Paper type p \nFor  Scissors type s:''')
you.lower()
a=game(comp,you)#using function

print(f"Computer Chose:{comp}")

print(f"{player} Chose:{you}")
if a is None:
    print("It is a tie")
elif a:
    print(f"{player} win")
else:
    print(f"{player} Lose")
