# import os
# def addition(n1,n2):
#     return n1+n2
#
# def subtraction(n1,n2):
#     if n2>n1:
#         return n2-n1
#     else:
#         return n1-n2
#
# def multiply(n1,n2):
#     return n1*n2
#
# def divide(n1,n2):
#     return n1/n2
#
# def calculate(selection):
#     if selection=="+":
#         return addition(n1,n2)
#     elif selection=="-":
#         return subtraction(n1,n2)
#     elif selection=="*":
#         return multiply(n1,n2)
#     elif selection=="/":
#         return divide(n1,n2)
#     else:
#         print("wrong command")
# end=True
# n1=int(input("what is the first number: "))
# while end:
#     symbols=["+","-","*","/"]
#     for i in symbols:
#         print(i)
#     selection=input("pick an operation: ")
#     n2=int(input("what is the next number?: "))
#     result=calculate(selection)
#     print(f"{n1} {selection} {n2}= {result}")
#     reccur_question=input(f"Type 'y' to continue calculating with {result} , or type 'n' to start a new calculation and type 'e' to exit the calculator: ")
#     if reccur_question=='y':
#         n1=result
#     elif reccur_question=='n':
#         os.system('cls')
#         n1=int(input("what is the first number: "))
#     elif reccur_question=='e':
#         end=False

'''with dictionaries code below'''
import os
def addition(n1,n2):
    return n1+n2

def subtraction(n1,n2):
    if n2>n1:
        return n2-n1
    else:
        return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

def calculate(pick):
    for key in operator:
        if pick==key:
            return operator[key](n1,n2)
operator={
    "+":addition,
    "-":subtraction,
    "*":multiply,
    "/":divide
}
calculator = True
n1 = int(input("what is the first number: "))
while calculator:
    for i in operator:
        print(i)
    pick=input("pick an operator: ")
    n2=int(input("what is the next number?: "))
    result=calculate(pick)
    print(f"{n1} {pick} {n2}= {result}")
    ask=input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation and type 'e' to exit the calculator: ")
    if ask=='y':
        n1=result
    elif ask=='n':
        os.system('cls')
        n1 = int(input("what is the first number: "))
    elif ask=='e':
        calculator=False
    else:
        print("wrong command")
        calculator=False

