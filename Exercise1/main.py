from BankAccount import *

account1 = bankAccount("Mark",10.0)

contLoop = 0

print(5.0+1.0)

while contLoop == 0:
    print(account1.get_balance())
    inp = int(input("Press 1 to deposit, press 2 to withdraw, press 3 to end: "))
    if inp == 1:
        inp2 = float(input("How much do you want to deposit?: "))
        account1.deposit_balance(inp2)
    if inp == 2:
        inp2 = float(input("How much do you want to withdraw?: "))
        account1.withdraw_balance(inp2)
    if inp == 3:
        contLoop = 1