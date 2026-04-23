#Snake-Water-Gun Game
import random
'''
1 = snake
-1 = water 
0 = gun
'''

computer = random.choice([-1,0,1])
youstr = input("Enter your choice (s, w, g): ")
youdict = {"s": 1, "w": -1, "g": 0}
reverseddict = {1: "snake", -1: "water", 0: "gun"}

you = youdict[youstr]  

#now we have two number, you and computer
print(f"you choose {reverseddict[you]}\ncomputer choose {reverseddict[computer]}")

if(computer == you):
    print("It's Draw!")

else:
    if(computer == -1 and you == 1):
        print("You win!")

    elif(computer == -1 and you == 0):
        print("You lose!")

    elif(computer == 1 and you == 0):
        print("You win!")

    elif(computer == 1 and you == 1):
        print("You lose!")

    elif(computer == 0 and you == 1):
        print("You lose!")

    elif(computer == 0 and you == -1):
        print("You win!")

    else:
        print("Something wrong!")


