import random

def random_number_create():
    c=[]
    for i in range(101):
       c.append(i)
    return random.choice(c)

def compare(random_number,number_choice):
    if random_number==number_choice:
        return 0
    elif random_number>number_choice:
        return 1
    elif random_number<number_choice:
        return 2
print("welcome to the number guessing game!")
print("I am thinking of a number between 1 and 100!")
difficulty_choice=input("Choose a difficulty 'easy' or 'hard': ").lower()
level={
    "easy":10,
    "hard":5
       }
if difficulty_choice=='easy':
    life=level['easy']
elif difficulty_choice=='hard':
    life=level['hard']
else:
    print("wrong command")
print(f"you have {life} attempts remaining to guess the number!")
random_number=random_number_create()
game=True
count=0
while game:
    if life!=0:
        if count!=0:
            print("guess again")
        number_choice = int(input("make a guess between 1 and 100: "))
        number_closeness = compare(random_number, number_choice)

        if number_closeness==0:
            print(f"your guess was right!. you had remaining lives {life}")
            game=False
        elif number_closeness==1:
            life-=1
            print(f"wrong choice. Your guess was too low. you loose a life.{life} lives remaining")
        elif number_closeness==2:
            life -= 1
            print(f"wrong choice. Your guess was too high. you loose a life.{life} lives remaining")
    else:
        print("game over! you loose")
        game=False
    count+=1