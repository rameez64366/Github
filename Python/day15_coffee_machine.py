import os
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }
resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
def calculate():
    def repay(bala,tot):
        new_money=0
        ask_quarters = int(input("how many more quarters:$ "))
        ask_dimes = int(input("how many more dimes:$ "))
        ask_nickles = int(input("how many more nickles:$ "))
        ask_pennies = int(input("how many more pennies:$ "))
        new_money += ask_quarters * COIN_VALUES['quarters'] + ask_dimes * COIN_VALUES['dimes'] + ask_nickles * COIN_VALUES['nickles'] + ask_pennies * COIN_VALUES['pennies']
        total = tot + new_money
        print(f"You have paid total of:$ {total}")
        if new_money>bala:
            bala = round((new_money - bala), 2)
            print(f"Here is the balance: ${bala}")
            return bala
        else:
            new_bala=round((bala-new_money),2)
            print(f"Not enough money. Please pay ${new_bala}")
            repay(new_bala,total)

    money=0
    ask_quarters=int(input("how many quarters:$ "))
    ask_dimes = int(input("how many dimes:$ "))
    ask_nickles = int(input("how many nickles:$ "))
    ask_pennies = int(input("how many pennies:$ "))
    money+=ask_quarters*COIN_VALUES['quarters'] + ask_dimes*COIN_VALUES['dimes'] + ask_nickles*COIN_VALUES['nickles'] +ask_pennies*COIN_VALUES['pennies']
    print(f"You have paid total of:$ {money}")
    if money>MENU[ask_start]['cost']:
        balance=round((money-MENU[ask_start]['cost']),2)
        print(f"Here is the balance: ${balance}")
        return balance
    else:
        bala=round((MENU[ask_start]['cost']-money),2)
        print(f"Not enough money. Please pay ${bala}")
        repay(bala,money)



def resource_compare(resources):
        flag=0
        if ask_start=='espresso'or ask_start=='latte' or ask_start=='cappuccino':
            select=MENU[ask_start]['ingredients']
            for each in select:
                if select[each]<=resources[each]:
                    resources[each]-=select[each]
                else:
                    print(f"Not enough {each}")
                    flag=1
            if flag==1:
                return 0
            else:
                return resources
        elif ask_start=='report':
            return resources
def salary(profit):
    if ask_start=='espresso':
        profit+=MENU[ask_start]['cost']
    elif ask_start=='latte':
        profit += MENU[ask_start]['cost']
    elif ask_start == 'cappuccino':
        profit += MENU[ask_start]['cost']
    return profit
new_resources={}
count=0
profit=0
coffee_on=True
while coffee_on:
    machine_on=input("Type 'on' to switch on or continue ordering and 'off' to switch off coffee machine: ").lower()
    if machine_on=='on':
        os.system('cls')
        ask_start=input("what would you like espresso/latte/cappuccino or type report to get the inventory: ").lower()
        report=resource_compare(resources)
        if report==0:
            print("shortage of inventory")
        elif ask_start=='report' and count==0:
            print(f"The report is:{resources}")
        elif ask_start=='report' and count!=0:
            print(f"Available is {report}")
        elif ask_start=='espresso'or ask_start=='latte' or ask_start=='cappuccino' and report!=0:
            bal=calculate()
            profit=salary(profit)
    else:
        print(f"your total profit is {profit}")
        coffee_on=False









