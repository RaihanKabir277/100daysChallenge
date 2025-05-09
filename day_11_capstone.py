import random 


card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

again = True

while again:
    choice = input("Do you want to play the BlackJack game type 'y' for yes type 'n' for no : \n")
    user = []
    ai = []
    if choice == "y":
        for i in range(2):
            user.append(random.choice(card))
        for j in range(2):
            ai.append(random.choice(card))
    elif choice == "n":
        again = False
        
        
    else:
        input("You enter the wrong choice , please type either 'y' or 'n' : \n")
    
    answer = 0
    for i in user:
        answer += i
    print(f"Your cards : {user}, current score : {answer}")
    print(f"Computers first card : {ai[0]}")
