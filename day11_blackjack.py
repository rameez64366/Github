import os
import random
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
def deal_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card

def sum(cards):
    sum=0
    for i in cards:
        sum+=i
    if sum==21 and len(cards)==2:
        return 21
    if 11 in cards and sum>21:
        cards.remove(11)
        cards.append(1)
    return sum

def calculate(user_sum,computer_sum):
    if user_sum==21 and computer_sum==21:
        print("It is a draw")
    elif user_sum==21 and computer_sum!=21:
        print("user wins with a black jack")
    elif computer_sum==21 and user_sum!=21:
        print("computer wins with a black jack")
    elif user_sum>21 and computer_sum>21:
        print("Both computer and user loose")
    elif user_sum>21 and computer_sum<21:
        print("computer wins")
    elif computer_sum>21 and user_sum<21:
        print("user wins")
    elif computer_sum>user_sum:
        print("computer wins")
    elif user_sum>computer_sum:
        print("user wins")
    elif user_sum==computer_sum:
        print("draw")

def play_game():
    print(logo)
    user_card=[]
    computer_card=[]
    for i in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())

    is_game=True
    while is_game:
        user_sum = sum(user_card)
        computer_sum = sum(computer_card)
        print(f"your cards:{user_card} and user sum: {user_sum}")
        print(f"computer cards: {computer_card} and computer sum: {computer_sum}")
        if user_sum==21 or computer_sum==21 or user_sum>21:
            is_game=False
        else:
            ask_card=input("Type y for another card and n for pass: ")
            if ask_card=='y':
                user_card.append(deal_card())
                user_sum = sum(user_card)
            else:
                is_game=False
    user_sum = sum(user_card)
    computer_sum = sum(computer_card)
    while computer_sum!=21 and computer_sum<=17:
        computer_card.append(deal_card())
        computer_sum = sum(computer_card)
    print(f"user cards: {user_card} and user sum: {user_sum}")
    print(f"computer cards: {computer_card} and user sum: {computer_sum}")
    calculate(user_sum, computer_sum)
while input("Type y to start black jack game and type n to exit the game: ")=='y':
    os.system('cls')
    play_game()

