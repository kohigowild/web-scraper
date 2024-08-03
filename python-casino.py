from random import randint

print("Welcome to Python Casino")

pc_choice = randint(1, 50)
user_choice = int(input("Choose Number: "))

if user_choice == pc_choice:
    print("You Won!")
elif user_choice > pc_choice:
    print("Lower!")
elif user_choice < pc_choice:
    print("Higher!")