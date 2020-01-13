import random
def main_function():
    user_input = input("Choose any option (rock,paper,scissor):")
    if user_input.lower() == "rock" or user_input.lower()=="paper" or user_input.lower()=="scissor":

        store_value = ["rock", "paper", "scissor"]
        diplay_value = random.choice(store_value)
        print(f"oppnent select: {diplay_value}")

        if user_input == diplay_value:
            print("No result play again")
        elif user_input != diplay_value:
            if user_input.lower() == "rock" and diplay_value == "paper":
                print("You loss")
            elif user_input.lower() == "rock" and diplay_value == "scissor":
                print("You win")



            elif user_input.lower() == "paper" and diplay_value == "rock":
                print("You win")
            elif user_input.lower() == "paper" and diplay_value == "scissor":
                print("You loss")



            elif user_input.lower() == "scissor" and diplay_value == "paper":
                print("You win")
            elif user_input.lower() == "scissor" and diplay_value == "rock":
                print("You loss")
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
