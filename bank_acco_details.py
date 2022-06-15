class User () :
    def __init__ (self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def show_user_details(self):
        print("Personal_details")
        print("")
        print("Name :",self.name)
        print("age :",self.age)
        print("gender :",self.gender)

class Bank(User):
    def __init__(self,name,age,gender):
        super(). __init__ (name,age,gender)
        self.total_amount = 0

    def welcome(self):
        print('Welcome to your Bank Account  : {} '.format(self.name))

    def print_current_balance(self):
        self.show_user_details()
        print('Your Current balance : {}'.format(self.total_amount))
    
    def deposit(self):
    	self.total_amount += float(input('Hello {}, please enter amount to deposit : '.format(self.name)))
    	self.print_current_balance()

    def withdraw(self):
        amount_to_withdraw = float(input('Enter amount to withdraw : '))

        if amount_to_withdraw > self.total_amount:
            print('Insufficient Balance !!')
        else:
            self.total_amount -= amount_to_withdraw

        self.print_current_balance()

if __name__== "__main__":
	bank = Bank("Srinivas",25,"Male")
	bank.welcome()

	while True:
		input_value = int(input('Please Enter\n 1 to see your balance,\n 2 to deposit\n 3 to withdraw\n'))

		if input_value == 1:
			bank.print_current_balance()
		elif input_value == 2:
			bank.deposit()
		elif input_value == 3:
			bank.withdraw()
		else:
			print('Please enter a valid input.')