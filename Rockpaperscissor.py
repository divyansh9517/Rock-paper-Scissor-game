import random
print("*********************************************")
print("LETS PLAY THE STONE PAPER SCISSOR GAME \n")
item_list=["Stone","Paper","Scissor"]
user_choice = input("Your choice = Stone , Paper , Scissor \n")
computer_choice=random.choice(item_list)

print("\nYour choice :- "+user_choice+", Computer choice :-"+computer_choice)
if user_choice==computer_choice:
    print("MATCH TIES")
elif user_choice=="Stone":
    if computer_choice=="Paper":
        print("\nPaper covers Stone , Computer wins\n")
    else:
        print("\nStone breaks Scissor , you wins\n")
elif user_choice=="Paper":
    if computer_choice=="Scissor":
        print("\nScissor cuts the paper, Computer wins\n")
    else:
        print("\nPaper covers the Stone, You wins\n")
elif user_choice=="Scissor":
    if computer_choice=="Stone":
        print("\nStone breaks scissor , computer wins\n")
    else:
        print("\nScissor cuts paper , you wins\n")
print("**********************************************")
