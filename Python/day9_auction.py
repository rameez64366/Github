logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
import os
print(logo)
bidding={}
def highest_bidder(bidding):
    highest_bid=0
    winner=""
    for key in bidding:
        if bidding[key]>highest_bid:
            highest_bid=bidding[key]
            winner=key
    print(f"The winner is:{winner} with winning bid amount:${highest_bid}")
game_on=True
while game_on:
    name=input("input name: ").lower()
    bid=int(input("input bid amount:$ "))
    bidding[name]=bid
    ask=input("are there more bidders (yes/no): ").lower()
    if ask=='yes':
        os.system('cls')
    else:
        print(bidding)
        highest_bidder(bidding)
        game_on=False

