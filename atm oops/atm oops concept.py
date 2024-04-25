class atm:
    def __init__(self):
        self.pin=9353
        self.balance=25000
        self.option()
    
    def option(self):
        print(""" what you like to do
              1.check balance
              2. withdraw balance
              3.deposit balance 
              4. exit""")
              
        option=int(input("enter your option"))
        if option==1:
             self.check_balance()
             
        elif option==2:
           self.withdraw_balance()
        
        elif option ==3:
            self.deposit_balance()
            
        elif option==4:
            self.exit()
        
    
    def check_balance(self):
        input_pin =int(input("enter the pin"))
        if input_pin==self.pin:
           print(f"your balance is {self.balance}")
        else:
            print("youe pin is iscorrect")
        self.option()
    def withdraw_balance(self):
        input_pin =int(input("enter the pin"))
        if input_pin==self.pin:
            input_balance=int(input("enter your withdraw amount"))
            if input_balance<=self.balance:
                self.balance=self.balance-input_balance
                print(f"your updated balance is{self.balance}")
            else:
                print("you dnot have a that much of balance")
        else:
            print("your pin is incorret")
        self.option()
            
    def deposit_balance(self):
        input_pin =int(input("enter the pin"))
        if input_pin==self.pin:
            input_deposit=int(input("enter the deposit amount"))
            self.balance=self.balance+input_deposit
            
        else:
            print("your pin is incorrect")
        self.option()
    def _exit_(self):
        print("you have been exit")
            
                   
obi=atm()