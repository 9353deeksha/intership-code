a=10
try:
    b= int(input("enter"))
except Exception as e:
    print(e)
else:
    print("else")
finally:
    print("finally")