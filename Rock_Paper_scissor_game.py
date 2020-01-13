import random
def main_function():
    user_input = input("Choose any option (rock,paper,scissor):")
    new_input=user_input.lower()
    store_value = ["rock", "paper", "scissor"]
    diplay_value = random.choice(store_value)
    print(f"oppnent select: {diplay_value}")
    if new_input==diplay_value:
        print("No result play again")
    elif new_input == "rock":
         if diplay_value=="paper":
                print("You loss")
         else:
                print("you win")
    elif new_input=="paper":
        if diplay_value=="rock":
            print("you win")
        else:
            print("you loss")
    elif new_input=="scissor":
       if diplay_value=="rock":
           print("you loss")
       else:
           print("you win")
    else:
        print("Wrong input" )
main_function()
while True:
 play_again= input("Do you wanna play again(y/n): ")
 if play_again.lower()=="y" :
    main_function()
 elif play_again.lower()=="n":
    exit("Game Over")
 else:
     print("Wrong input")
