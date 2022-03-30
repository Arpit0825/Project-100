dollars = '$1000'

class Atm:

    def __init__(self,account,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin
        self.Account = account

    def check_balance(self):
        print("Your balance is :" + dollars)

    def withdrawl(self,dollars1):
        new_amount = dollars - dollars1
        print("You have withdrawn "+ dollars1  + ". Your current balance is "+ new_amount)
        
    def deposit(self,dollars2):
        new_amount1 = dollars + dollars2
        print("You have deposited amount "+dollars2+"Your current balance is "+ new_amount1)


def main():
    print("Welcome to American Express Bank!")
    Account = int(input("Please enter your account number: ")),
    Card_number = int(input("Please enter your key number: ")),
    pin_number  = int(input("Please enter your pin: "))

    new_user =  Atm(Account,Card_number,pin_number)

    print("Choose your activity ")
    print("1.Balance Enquriy   \n2.Withdrawl   \n3.Deposit")
    activity = int(input("Enter activity number : "))

    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):
        dollars_1 = input("Enter amount: ")
        new_user.withdrawl(dollars_1)
    elif (activity == 3):
        dollars_2 = input('Enter Amount:')
        new_user.deposit(dollars_2)
    else:
        print('Enter a valid number')    
        

if __name__ == "__main__":
    main()