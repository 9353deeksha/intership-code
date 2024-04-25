def armstrong_by_lambda():
    num=int(input("enter the number :"))
    arms=str(num)
    result=list(map(lambda a:int(a)**len(arms),arms))
    final=0
    for i in result:final=final+1
    print(final)
    
armstrong_by_lambda()