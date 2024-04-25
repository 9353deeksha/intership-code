name=['deeksha','pacchu','laxmi']
password=[9353,9071,9901]
balance=[10000,25000,35000]


def withdraw(current):
    amount=int(input("enter the amount"))
    if amount<=balance[current]:
        balance[current]-=amount
        print("successfully")
    else:
        print("insufficent funds")
def c_balance(current):
    print("balance is",balance[current])

def default(current):
    print("enter correct option")
    
    
user_name=input("enter the name")
for i in range(len(name)):
    if user_name==name[i]:
        user_password=int(input("enter the password"))
        if user_password==password[i]:
            while True:
                print("1.withdraw\n2.balance")
                option=int(input("enter your option"))
                if option==0:
                    break
                data={1:withdraw,2:c_balance}
                result=data.get(option,default)
                result(i )