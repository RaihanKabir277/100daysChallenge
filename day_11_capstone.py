import random 

def black_jack():

    card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    again = True

    while again:
        choice = input("Do you want to play the BlackJack game type 'y' for yes type 'n' for no : \n").lower()
        user = []
        ai = []
        if choice == "y":
            for i in range(2):
                user.append(random.choice(card))
            for j in range(2):
                ai.append(random.choice(card))
        elif choice == "n":
            return
        
        else:
            print("\nYou enter the wrong choice , please type either 'y' or 'n' \n")
            continue
        
        # answer = 0
        # for i in user:
        #     answer += i
        answer = sum(user)
        answer1 = sum(ai)
        print(f"Your cards : {user}, current score : {answer}")
        print(f"Computers first card : {ai[0]}")
        
        while answer <= 21:
            take_card = input("Type 'y' to get another card, type 'n' to pass : \n").lower()
            if take_card == "y":
                user.append(random.choice(card))
                answer = sum(user)
                print(f"Your cards : {user}, current score : {answer}")
                print(f"Computers first card : {ai[0]}")

                if answer > 21:
                    print(f"Your final cards : {user}, final score : {answer}")
                    print(f"Computers final card : {ai[1]}, final score : {answer1}")
                    print("Game over . You lose")
                    break
                elif answer1 > 21:
                    print(f"Your final cards : {user}, final score : {answer}")
                    print(f"Computers final card : {ai[1]}, final score : {answer1}")
                    print("Game over . You Win")
                    break
                elif answer <= 21:
                    print(f"Your final cards : {user}, final score : {answer}")
                    print(f"Computers final card : {ai[1]}, final score : {answer1}")
                    if answer > answer1: 
                        print("Game over . You Win")
                        break
                    else:
                        print("Game over . You Loss")
                        break
            elif take_card == "n":
                print(f"Your final cards : {user}, final score : {answer}")
                print(f"Computers final card : {ai[1]}, final score : {answer1}")
                if answer > answer1: 
                    print("Game over . You Win")
                    break
                else:
                    print("Game over . You Loss")
                    break


black_jack()

