import random
def gameWin(comp,you):
    if comp == you:
        return None
    elif comp == 'r':
        if you == 'p':
            return True
        elif you == 's':
            return False
    elif comp == 'p':
        if you == 's':
            return False
        elif you == 'r':
            return False
    elif comp == 's':
        if you == 'P':
            return False
        elif you == 's':
            return True
print("comp Turn: Rock(r) Paper(p) Scissors(s): Selected")
RandomNo = random.randint(1,3)
if RandomNo == 1:
    comp ='r'
elif RandomNo == 2:
    comp = 'p'
elif RandomNo == 3:
    comp = 's'
you = input("Your Turn:Rock(r) Paper(p) Scissors(s): ")
a = gameWin(comp , you)
print(f"comp chosen {comp}")
print(f"You chosen {you}")
if a == None:
    print("Game is tie")
elif a:
    print("You won!")
else:
    print("You Lost!")    
