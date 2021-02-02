
amount =int(input("Enter withdraw amount"))
balance = int(input("Enter account balance"))
finalbal=int()
if(amount>balance):
    print("Insufficient funds",balance)
else:
    if(amount%5==0):
        finalbal=balance-(amount+0.5)
        print('%.2f'%finalbal)
    else:
        print(balance)
amount =int(input("Enter withdraw amount"))
balance = int(input("Enter account balance"))
finalbal=int()
if(amount>balance):
    print("Insufficient funds",balance)
else:
    if(amount%5==0):
        finalbal=balance-(amount+0.5)
        print('%.2f'%finalbal)
    else:
        print(balance)