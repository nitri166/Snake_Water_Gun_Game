# Snake Water Gun
# Use random module in python
# Let computer choose any thing
# Then you choose. Then decide who is the winner for the game
# Play this game 10 times
# count the no of times each person one
import random
import emoji 
print("Welcome to the Snake Water Gun Game")
print("You are against the Computer")
print("\nRules are simple: You have three choices")
print("S-Snake, W-Water, G-Gun")
print("\nIf you are ready, Lets Start", emoji.emojize(":snake: Game"))
i = 1
player_score =0
comp_score=0
print("Enter no of times you want to play")
n = int(input())
while i<=n:
    list = ["Snake","Water", "Gun"]
    comp_choice = random.choice(list)


    print("Its your turn")
    print("Choose from S,W,G")
    x= input()
    inp = x.upper()
    if inp == "S" or inp == "W" or inp== "G":

        if comp_choice == "Snake" and inp == "S" or comp_choice == "Water" and inp =="W" or comp_choice=="Gun" and inp=="G":
            print("Match Draw",emoji.emojize(":expressionless_face:"))
        elif comp_choice=="Snake" and inp=="W":
            print("Oops, Computer won", emoji.emojize(":crying_face:"))
            comp_score+=1
        elif comp_choice =="Snake" and inp =="G":
            print("Yeah, You won", emoji.emojize(":grinning_face_with_big_eyes:"))
            player_score+=1
        elif comp_choice == "Water" and inp =="S":
            print("Yeah, You won", emoji.emojize(":grinning_face_with_big_eyes:"))
            player_score+=1

        elif comp_choice =="Water" and inp =="G":
            print("Oops, Computer won", emoji.emojize(":crying_face:")) 
            comp_score+=1

        elif comp_choice =="Gun" and inp=="S":
            print("Oops, Computer won", emoji.emojize(":crying_face:")) 
            comp_score+=1
        elif comp_choice == "Gun" and inp == "W":
            print("Yeah, You won", emoji.emojize(":grinning_face_with_big_eyes:"))
            player_score+=1
        i =i+1
    else:
        print("Play Again, Wrong input")
print("\nGame Over\n")        
print("Computer Score is :", comp_score)    
print("Your Score is : ", player_score ) 




