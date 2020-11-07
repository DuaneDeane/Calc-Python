# imports
from os import system, name
from time import sleep

#global vars

# functions


def print_menu():
    print('********************')
    print(" Welcome - PyCalc")
    print('********************')

    print('[1] Add')
    print('[2] Substract')
    print('[3] Multiply')
    print('[4] Divide')

    print('[5] Calculate age')

    print('[x] Exit')
    print('-' * 20)


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


print('\n'*10)
sleep(2)
clear()
# HW: how to clear the console with python

# instructions
opc = ''

while(opc != 'x'):
    clear()
    print_menu()
    opc = input("Please select an option: ")

    if(opc == '1' or opc == '2' or opc == '3' or opc == '4'):
        num1 = float(input("Please enter first number: "))
        num2 = float(input("Please enter second number: "))
        if(opc == '4' and num2 == 0):
            while(num2 == 0):
                print("Error, not allowed")
                num2 = float(input("Please enter second number: "))
    if(opc == '5'):
        num1 = float(input("Please enter the year born: "))
        num2 = float(input("Please enter current year: "))

    if(opc == '1'):
        print("Result is: ", num1 + num2)
    elif(opc == '2'):
        print("Result is: ", num1 - num2)
    elif(opc == '3'):
        print("Result is: ", num1 * num2)
    elif(opc == '4'):
        print("Result is: ", num1 / num2)
    elif(opc == '5'):
        print("Result is: ", num2 - num1)

    input("Press Enter to continue...")

print("Good byte")
