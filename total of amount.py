class ece:
    def __init__(self,amount):
        self.amount=amount
    def total(self,other):
        print(self.amount,other.amount,self.amount+other.amount)
        
        
deeksha=ece(11246)
pacchu=ece(340)
ece.total(deeksha,pacchu)