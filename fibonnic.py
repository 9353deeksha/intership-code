a=0
b=9
print(a)
print(b)
for i in range(0,9):
    print(a+b)
    temp=a
    a=b
    b=temp+a
    